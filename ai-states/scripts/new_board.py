#!/usr/bin/env python3
"""Start a new state board from the template, ready to fill.

    python new_board.py board.html --title "HR assistant" [--lang es] [--review]

Copies assets/template.html, removes the instruction comment and the example cards
(everything between EXAMPLES START and EXAMPLES END), sets the title and the language,
and - unless --review - removes the findings block and the map's Today column.
The CSS, the components and the flow player stay. Then add your cards where the
examples were (look for the line ADD YOUR CARDS HERE).
"""
import argparse
import re
import sys
from pathlib import Path

ES = [
    ('open: "Try the flow", title: "Flow", back: "Back", restart: "Restart", close: "Close"',
     'open: "Probar el flujo", title: "Flujo", back: "Atrás", restart: "Empezar de nuevo", close: "Cerrar"'),
    ('path: "Path", ok: "Every screen has a way out and can be reached."',
     'path: "Recorrido", ok: "Todas las pantallas tienen salida y se puede llegar a ellas."'),
    ('dead: "No way out", orphan: "Nothing leads here", missing: "Button leads to a screen that does not exist"',
     'dead: "Sin salida", orphan: "Nada lleva acá", missing: "El botón lleva a una pantalla que no existe"'),
    ('unwired: "This button is not wired to a screen"', 'unwired: "Este botón no lleva a ninguna pantalla"'),
    ("<h2>Coverage</h2>", "<h2>Cobertura</h2>"),
    ("<h2>Findings, by harm</h2>", "<h2>Hallazgos, por daño</h2>"),
    ("<h2>Across all states</h2>", "<h2>En todos los estados</h2>"),
    ("<h2>State map</h2>", "<h2>Mapa de estados</h2>"),
    ("<h2>Signals the system must expose</h2>", "<h2>Señales que el sistema tiene que exponer</h2>"),
    ("<th>State</th>", "<th>Estado</th>"), ("<th>Applies</th>", "<th>Aplica</th>"), ("<th>Today</th>", "<th>Hoy</th>"),
    ("<th>Why / where / signal</th>", "<th>Por qué / dónde / señal</th>"),
    ("<th>Signal</th><th>Used by</th><th>Status</th>", "<th>Señal</th><th>La usa</th><th>Estado</th>"),
    ("<li><b>Surface:</b>", "<li><b>Superficie:</b>"), ("<li><b>Stakes:</b>", "<li><b>Riesgo:</b>"),
    ("<li><b>Autonomy:</b>", "<li><b>Autonomía:</b>"), ("<li><b>Register:</b>", "<li><b>Trato:</b>"),
    ("<li><b>Version:</b>", "<li><b>Versión:</b>"), ("<h3>Interruption</h3>", "<h3>Interrupción</h3>"),
    ("<h3>Memory</h3>", "<h3>Memoria</h3>"), ("<h3>Proactivity</h3>", "<h3>Proactividad</h3>"), ("<h3>Cost</h3>", "<h3>Costo</h3>"),
]

TEMPLATE = Path(__file__).resolve().parent.parent / "assets" / "template.html"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("--title", required=True)
    ap.add_argument("--lang", default="en")
    ap.add_argument("--review", action="store_true", help="keep the findings block and the Today column")
    a = ap.parse_args()

    s = TEMPLATE.read_text(encoding="utf-8")
    s = re.sub(r"<!--\s*\n\s*STATE BOARD TEMPLATE.*?-->\n", "", s, count=1, flags=re.S)
    s = re.sub(r"<!-- =+ EXAMPLES START.*?EXAMPLES END =+ -->",
               "<!-- ADD YOUR CARDS HERE: one <section class=\"moment m-...\"> per moment, one <article class=\"state\"> per state. -->",
               s, count=1, flags=re.S)
    s = re.sub(r"<html lang=\"[^\"]*\">", f'<html lang="{a.lang}">', s, count=1)
    s = s.replace("<title>State board - FEATURE NAME</title>", f"<title>State board - {a.title}</title>")
    s = s.replace("<h1>FEATURE NAME: state board</h1>", f"<h1>{a.title}: state board</h1>")
    if not a.review:
        s = re.sub(r"<!-- FINDINGS:.*?</section>\n", "", s, count=1, flags=re.S)
        s = s.replace("<th>Applies</th><th>Today</th>", "<th>Applies</th>")
        s = re.sub(r'(<tr><td>[^<]*</td><td>[^<]*</td><td class="[^"]*">[^<]*</td>)<td[^>]*>[^<]*</td>', r"\1", s)
    if a.lang.startswith("es"):
        for en, es in ES:
            s = s.replace(en, es)
    Path(a.out).write_text(s, encoding="utf-8", newline="\n")
    print(f"Wrote {Path(a.out).name}. Replace the example rows in the coverage strip, map and signals table, "
          f"add your cards, then run check_board.py.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
