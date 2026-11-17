#!/usr/bin/env python3
"""Render an HTML state board to a PNG so it can be looked at.

    python screenshot.py board.html board.png [--width 1400]

Tries Playwright first (full page, exact). If it is not installed, falls back to a
headless Chrome, Edge or Chromium found on the machine. Paths are resolved to their
long form first: on Windows, headless browsers fail silently on 8.3 short paths
(C:\\Users\\NAME~1\\...) and without their own profile folder.
"""
import argparse
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


def long_path(p: Path) -> Path:
    p = p.resolve()
    if os.name == "nt":
        try:
            import ctypes

            buf = ctypes.create_unicode_buffer(32768)
            if ctypes.windll.kernel32.GetLongPathNameW(str(p), buf, 32768):
                return Path(buf.value)
        except Exception:
            pass
    return p


def tile_names(out: Path, n: int):
    return [out.with_name(f"{out.stem}-{i + 1:02d}{out.suffix}") for i in range(n)]


def with_playwright(url: str, out: Path, width: int, tile: int = 0) -> bool:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        return False
    try:
        with sync_playwright() as pw:
            browser = pw.chromium.launch()
            page = browser.new_page(viewport={"width": width, "height": 900})
            page.goto(url)
            page.screenshot(path=str(out), full_page=True)
            if tile:
                total = page.evaluate("document.documentElement.scrollHeight")
                n = -(-total // tile)
                for i, name in enumerate(tile_names(out, n)):
                    h = min(tile, total - i * tile)
                    page.screenshot(path=str(name), full_page=True,
                                    clip={"x": 0, "y": i * tile, "width": width, "height": h})
            browser.close()
        return True
    except Exception as e:  # browser binary missing, etc.
        print(f"Playwright could not render ({e}); trying an installed browser.", file=sys.stderr)
        return False


def find_browser():
    names = ["chrome", "google-chrome", "chromium", "chromium-browser", "msedge", "microsoft-edge"]
    for n in names:
        found = shutil.which(n)
        if found:
            return found
    candidates = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
    ]
    for c in candidates:
        if os.path.exists(c):
            return c
    return None


def measure_height(exe: str, src: Path, width: int):
    """Ask the browser how tall the page is: load a copy that writes its height into the DOM."""
    probe = src.with_name(src.stem + ".probe-height.html")
    profile = tempfile.mkdtemp(prefix="board-shot-")
    try:
        html = src.read_text(encoding="utf-8", errors="replace")
        html += ("<script>document.documentElement.setAttribute('data-board-height',"
                 "Math.ceil(document.documentElement.scrollHeight))</script>")
        probe.write_text(html, encoding="utf-8")
        r = subprocess.run(
            [exe, "--headless=new", "--disable-gpu", "--no-first-run", f"--user-data-dir={profile}",
             f"--window-size={width},900", "--dump-dom", probe.as_uri()],
            capture_output=True, timeout=90)
        import re
        m = re.search(rb'data-board-height="(\d+)"', r.stdout)
        return int(m.group(1)) if m else None
    except Exception:
        return None
    finally:
        try:
            probe.unlink()
        except OSError:
            pass
        shutil.rmtree(profile, ignore_errors=True)


def with_browser(url: str, out: Path, width: int, height: int) -> bool:
    exe = find_browser()
    if not exe:
        return False
    profile = tempfile.mkdtemp(prefix="board-shot-")
    try:
        subprocess.run(
            [
                exe,
                "--headless=new",
                "--disable-gpu",
                "--hide-scrollbars",
                "--no-first-run",
                f"--user-data-dir={profile}",
                f"--window-size={width},{height}",
                f"--screenshot={out}",
                url,
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=90,
        )
    except Exception as e:
        print(f"Browser failed: {e}", file=sys.stderr)
    finally:
        shutil.rmtree(profile, ignore_errors=True)
    return out.exists() and out.stat().st_size > 0


def tiles_with_browser(src: Path, out: Path, width: int, total: int, tile: int) -> int:
    """Slices for the fallback: a wrapper page shows the board in an iframe shifted up by the offset."""
    n = -(-total // tile)
    made = 0
    for i, name in enumerate(tile_names(out, n)):
        wrap = src.with_name(f"{src.stem}.probe-tile.html")
        wrap.write_text(
            "<!doctype html><meta charset='utf-8'><style>html,body{margin:0;overflow:hidden}</style>"
            f"<iframe src='{src.name}' style='border:0;width:{width}px;height:{total}px;"
            f"margin-top:-{i * tile}px'></iframe>", encoding="utf-8")
        try:
            if name.exists():
                name.unlink()
            if with_browser(wrap.as_uri(), name, width, min(tile, total - i * tile)):
                made += 1
        finally:
            try:
                wrap.unlink()
            except OSError:
                pass
    return made


def main() -> int:
    ap = argparse.ArgumentParser(description="Render an HTML board to PNG.")
    ap.add_argument("html")
    ap.add_argument("png")
    ap.add_argument("--width", type=int, default=1400)
    ap.add_argument("--height", type=int, default=0,
                    help="page height for the browser fallback (default: measured automatically)")
    ap.add_argument("--tile", type=int, default=0,
                    help="also save slices this many pixels tall (board-01.png, board-02.png...), "
                         "readable when the board is long")
    a = ap.parse_args()

    src = long_path(Path(a.html))
    if not src.exists():
        print(f"Not found: {src}", file=sys.stderr)
        return 2
    out_dir = long_path(Path(a.png).parent if str(Path(a.png).parent) else Path("."))
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / Path(a.png).name
    if out.exists():
        out.unlink()
    url = src.as_uri()

    if with_playwright(url, out, a.width, a.tile):
        print(f"Saved {out.name} (full page, Playwright)")
        return 0
    exe = find_browser()
    height = a.height
    if exe and height == 0:
        height = measure_height(exe, src, a.width) or 6000
    elif height == 0:
        height = 6000
    if with_browser(url, out, a.width, height):
        print(f"Saved {out.name} ({a.width}x{height}, installed browser). "
              f"If the board is cut off, run again with --height.")
        if a.tile:
            n = tiles_with_browser(src, out, a.width, height, a.tile)
            print(f"Saved {n} slices of {a.tile}px: {out.stem}-01{out.suffix} ...")
        return 0
    print("Could not render: install Playwright (pip install playwright && playwright install chromium) "
          "or Chrome/Edge. Without a render, say in your delivery that the board was not reviewed visually.",
          file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
