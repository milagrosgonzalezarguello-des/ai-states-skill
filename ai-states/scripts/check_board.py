#!/usr/bin/env python3
"""Check a state board before delivering it.

    python check_board.py board.html [--tests state-tests.json]

Reports, without a browser:
  - flow:        buttons that lead to a screen that does not exist, screens with no way out,
                 screens nothing leads to
  - leftovers:   template text, placeholders and brackets left in the copy
  - coverage:    states marked designed in the coverage strip that have no card
  - contrast:    text/background colour pairs from :root below 4.5:1
  - tests:       (with --tests) every test names a state that has a card, and every card has a test

Exit code 1 if there is anything under "Fix"; warnings do not fail.
"""
import argparse
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

VOID = {"br", "img", "input", "hr", "meta", "link", "col", "source", "wbr", "area", "base"}


class Board(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []          # (tag, attrs)
        self.screens = {}        # id -> {"gos": [], "end": bool, "text": [], "buttons": int}
        self.dupes = []
        self.order = []
        self.start = None
        self.cur = None          # (screen id, stack depth)
        self.in_player = 0
        self.cards = []          # state numbers that have a card
        self.cells = []          # (class, text) of the coverage strip
        self._n = None
        self._cell = None
        self.comments = []
        self.skip = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        cls = (a.get("class") or "").split()
        if tag in ("script", "style"):
            self.skip += 1
        if a.get("id") == "player":
            self.in_player = len(self.stack) + 1
        if tag not in VOID:
            self.stack.append(tag)
        if self.in_player:
            return
        if "data-screen" in a and self.cur is None:
            sid = a["data-screen"]
            if sid in self.screens:
                self.dupes.append(sid)
            self.screens[sid] = {"gos": [], "end": "data-end" in a, "entry": "data-entry" in a, "text": [], "buttons": 0}
            self.order.append(sid)
            if "data-start" in a and self.start is None:
                self.start = sid
            self.cur = (sid, len(self.stack))
        if self.cur:
            s = self.screens[self.cur[0]]
            if "data-go" in a:
                s["gos"].append(a["data-go"])
            if tag == "button" or (tag == "a" and "btn" in cls):
                s["buttons"] += 1
        if tag == "span" and "n" in cls:
            self._n = ""
        if tag == "li" and self.stack[-3:-1] and "ul" in self.stack[-2:]:
            if any(c in cls for c in ("designed", "incomplete", "generic", "missing", "if", "na", "review", "covered")):
                self._cell = [cls, ""]

    def handle_endtag(self, tag):
        if tag in ("script", "style") and self.skip:
            self.skip -= 1
        if self._n is not None and tag == "span":
            self.cards.append(self._n.strip())
            self._n = None
        if self._cell is not None and tag == "li":
            self.cells.append((self._cell[0], " ".join(self._cell[1].split())))
            self._cell = None
        if tag in VOID:
            return
        while self.stack:
            t = self.stack.pop()
            if t == tag:
                break
        if self.cur and len(self.stack) < self.cur[1]:
            self.cur = None
        if self.in_player and len(self.stack) < self.in_player:
            self.in_player = 0

    def handle_data(self, data):
        if self.skip or self.in_player:
            return
        if self._n is not None:
            self._n += data
        if self._cell is not None:
            self._cell[1] += data
        if self.cur:
            self.screens[self.cur[0]]["text"].append(data)

    def handle_comment(self, data):
        self.comments.append(data)


def lum(hexcol):
    h = hexcol.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    r, g, b = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
    f = lambda c: c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)


def ratio(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


PAIRS = [("ink", "bg"), ("ink", "card"), ("muted", "card"), ("muted", "bg"), ("brand", "card"),
         ("info", "info-bg"), ("rule", "rule-bg"), ("fail", "fail-bg"), ("warn", "warn-bg"), ("ok", "card"),
         ("care", "care-bg")]
LEFTOVER = [r"FEATURE NAME", r"lorem ipsum", r"\bTODO\b", r"\bTBD\b", r"message here", r"texto aqu[ií]", r"\bxxx+\b"]


def main():
    ap = argparse.ArgumentParser(description="Check a state board.")
    ap.add_argument("html")
    ap.add_argument("--tests", help="state-tests.json to check against the board")
    a = ap.parse_args()
    src = Path(a.html).read_text(encoding="utf-8", errors="replace")
    b = Board()
    b.feed(src)
    fix, warn = [], []

    # flow
    if b.order:
        start = b.start or b.order[0]
        incoming = set()
        for sid in b.order:
            for g in b.screens[sid]["gos"]:
                if g in b.screens:
                    incoming.add(g)
                else:
                    fix.append(f"flow: screen {sid} has a button that leads to '{g}', which does not exist")
        for sid in b.order:
            s = b.screens[sid]
            if not s["gos"] and not s["end"]:
                fix.append(f"flow: screen {sid} has no way out (wire a button with data-go, or mark it data-end if the flow rightly ends there)")
            if sid != start and sid not in incoming and not s["entry"]:
                warn.append(f"flow: nothing leads to screen {sid}")
    else:
        warn.append("flow: no screen has data-screen, so the board cannot be played or checked as a flow")

    for d in b.dupes:
        fix.append(f"flow: two screens share the id '{d}'; give each screen its own data-screen")

    # leftovers
    if "STATE BOARD TEMPLATE" in " ".join(b.comments):
        fix.append("leftovers: the template's instruction comment is still in the file")
    if "EXAMPLES START" in " ".join(b.comments):
        fix.append("leftovers: the EXAMPLES START / END markers are still in the file")
    for sid in b.order:
        text = " ".join(" ".join(b.screens[sid]["text"]).split())
        for pat in LEFTOVER:
            if re.search(pat, text, re.I):
                fix.append(f"leftovers: screen {sid} contains placeholder text matching '{pat}'")
        m = re.search(r"\[[^\]\d][^\]]{1,40}\]", text)
        if m:
            fix.append(f"leftovers: screen {sid} has a bracket left in the copy: {m.group(0)}")
    if re.search(r"<title>[^<]*FEATURE NAME", src):
        fix.append("leftovers: the page title still says FEATURE NAME")

    # coverage vs cards
    cards = set(b.cards)
    for cls, text in b.cells:
        m = re.search(r"\b(D?\d{1,2}|S)\b", text)
        if not m:
            continue
        n = m.group(1)
        if ("designed" in cls or "incomplete" in cls) and n not in cards and "see" not in text.lower() and " en la " not in text.lower():
            warn.append(f"coverage: '{text}' is marked designed but no card has the number {n}")

    # contrast
    root = re.search(r":root\s*\{(.*?)\}", src, re.S)
    if root:
        var = dict(re.findall(r"--([\w-]+)\s*:\s*(#[0-9a-fA-F]{3,6})\b", root.group(1)))
        pairs = list(PAIRS)
        for name in var:   # any extra --x / --x-bg pair the board added
            if name.endswith("-bg") and name[:-3] in var and (name[:-3], name) not in pairs:
                pairs.append((name[:-3], name))
        for fg, bg in pairs:
            if fg in var and bg in var:
                r = ratio(var[fg], var[bg])
                if r < 4.5:
                    fix.append(f"contrast: --{fg} on --{bg} is {r:.1f}:1 (needs 4.5:1)")

    # tests
    if a.tests:
        try:
            tests = json.loads(Path(a.tests).read_text(encoding="utf-8"))
            items = tests["tests"] if isinstance(tests, dict) else tests
            tested = set()
            for i, t in enumerate(items, 1):
                for key in ("id", "state", "input", "expect"):
                    if key not in t:
                        fix.append(f"tests: test {i} has no '{key}'")
                st = str(t.get("state", "")).split()[0] if t.get("state") else ""
                tested.add(st)
                if st and st not in cards:
                    warn.append(f"tests: test {t.get('id', i)} is for state {st}, which has no card on the board")
            for n in sorted(cards - tested):
                warn.append(f"tests: state {n} has a card but no test")
        except Exception as e:
            fix.append(f"tests: could not read {a.tests}: {e}")

    print(f"{len(b.order)} screens, {len(cards)} cards, {len(b.cells)} coverage cells")
    if fix:
        print("\nFix:")
        for f in fix:
            print("  - " + f)
    if warn:
        print("\nCheck:")
        for w in warn:
            print("  - " + w)
    if not fix and not warn:
        print("Nothing to fix.")
    return 1 if fix else 0


if __name__ == "__main__":
    sys.exit(main())
