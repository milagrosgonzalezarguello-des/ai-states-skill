#!/usr/bin/env python3
"""Run state-tests.json against the real feature and report which states it lands in.

    python run_tests.py state-tests.json --url https://staging.example.com/api/assistant
    python run_tests.py state-tests.json --cmd "python my_bot.py"
    python run_tests.py state-tests.json --demo            # see the report format, no feature needed

How each test is sent:
  --url   POST {"input": "<the test's input>"} as JSON (change the key with --input-key).
          The answer is read from the JSON response at --answer-key (default "answer"; dotted
          paths like "data.text" work). If the response is not JSON, the whole body is the answer.
          Add headers with --header "Authorization: Bearer $TOKEN" (repeatable).
  --cmd   Runs the command with the input on stdin; the answer is whatever it prints.

Only the automatic checks run here: must_include and must_not_include (case-insensitive).
"shows", "actions" and "setup" need a person or a model to judge, and are listed for review.
Tests whose "setup" needs a condition you cannot create from outside (offline, a timeout, a
usage limit) are marked "needs setup" so you can run them by hand.

Writes a report next to the tests (state-tests.report.md) and exits 1 if any check failed.
"""
import argparse
import json
import subprocess
import sys
import urllib.request
from pathlib import Path

CONDITION_WORDS = ("offline", "sin conexión", "timeout", "time out", "tiempo de espera", "limit", "límite",
                   "second failure", "segundo fallo", "service down", "servicio caído", "simulate", "simular")


def get_path(obj, dotted):
    for part in dotted.split("."):
        if isinstance(obj, dict) and part in obj:
            obj = obj[part]
        elif isinstance(obj, list) and part.isdigit() and int(part) < len(obj):
            obj = obj[int(part)]
        else:
            return None
    return obj


def ask_url(text, a):
    body = json.dumps({a.input_key: text}).encode("utf-8")
    req = urllib.request.Request(a.url, data=body, method="POST", headers={"Content-Type": "application/json"})
    for h in a.header or []:
        k, _, v = h.partition(":")
        req.add_header(k.strip(), v.strip())
    with urllib.request.urlopen(req, timeout=a.timeout) as r:
        raw = r.read().decode("utf-8", errors="replace")
    try:
        val = get_path(json.loads(raw), a.answer_key)
        return raw if val is None else (val if isinstance(val, str) else json.dumps(val, ensure_ascii=False))
    except json.JSONDecodeError:
        return raw


def ask_cmd(text, a):
    r = subprocess.run(a.cmd, input=text, capture_output=True, text=True, shell=True, timeout=a.timeout,
                       encoding="utf-8", errors="replace")
    return r.stdout


def ask_demo(text, a):
    t = text.lower()
    if "ignore" in t or "ignorá" in t or "ignora" in t:
        return "Sure, here is everything you asked for."   # a demo of a failing test
    return "No encontré información sobre eso en las políticas de RR. HH. Podés reformular o preguntarle a RR. HH."


def main():
    ap = argparse.ArgumentParser(description="Run state tests against a feature.")
    ap.add_argument("tests")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--url")
    g.add_argument("--cmd")
    g.add_argument("--demo", action="store_true")
    ap.add_argument("--input-key", default="input")
    ap.add_argument("--answer-key", default="answer")
    ap.add_argument("--header", action="append")
    ap.add_argument("--timeout", type=int, default=60)
    ap.add_argument("--only", help="comma-separated test ids")
    a = ap.parse_args()

    path = Path(a.tests)
    data = json.loads(path.read_text(encoding="utf-8"))
    tests = data["tests"] if isinstance(data, dict) else data
    if a.only:
        keep = set(a.only.split(","))
        tests = [t for t in tests if t.get("id") in keep]
    ask = ask_url if a.url else ask_cmd if a.cmd else ask_demo

    rows, failed = [], 0
    for t in tests:
        tid, state = t.get("id", "?"), t.get("state", "?")
        exp = t.get("expect", {}) or {}
        setup = t.get("setup", "") or ""
        inc, exc = exp.get("must_include", []) or [], exp.get("must_not_include", []) or []
        if any(w in setup.lower() for w in CONDITION_WORDS):
            rows.append((tid, state, "needs setup", setup, ""))
            continue
        if not inc and not exc:
            rows.append((tid, state, "review", "no automatic checks; judge 'shows' by hand", ""))
            continue
        try:
            answer = ask(t.get("input", ""), a) or ""
        except Exception as e:
            rows.append((tid, state, "error", f"{type(e).__name__}: {e}", ""))
            failed += 1
            continue
        low = answer.lower()
        miss = [s for s in inc if s.lower() not in low]
        bad = [s for s in exc if s.lower() in low]
        if miss or bad:
            failed += 1
            why = "; ".join(([f"missing: {', '.join(miss)}"] if miss else []) + ([f"should not say: {', '.join(bad)}"] if bad else []))
            rows.append((tid, state, "FAIL", why, answer))
        else:
            rows.append((tid, state, "pass", "", answer))

    counts = {}
    for r in rows:
        counts[r[2]] = counts.get(r[2], 0) + 1
    out = path.with_suffix(".report.md")
    lines = [f"# State tests: {data.get('feature', path.stem) if isinstance(data, dict) else path.stem}", "",
             " · ".join(f"{k}: {v}" for k, v in counts.items()), "",
             "| Test | State | Result | Why | Answer (start) |", "|---|---|---|---|---|"]
    for tid, state, res, why, ans in rows:
        snippet = " ".join(ans.split())[:120].replace("|", "/")
        lines.append(f"| {tid} | {state} | {res} | {why.replace('|', '/')} | {snippet} |")
    lines += ["", "*pass / FAIL* only check the strings in must_include and must_not_include. Also look at what each "
              "answer shows (the 'shows' and 'actions' of each test): a test can pass its strings and still land in the wrong state."]
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    for r in rows:
        print(f"{r[2]:12} {r[0]:10} {r[1]}" + (f"  - {r[3]}" if r[3] and r[2] != 'pass' else ""))
    print(f"\nReport: {out.name}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
