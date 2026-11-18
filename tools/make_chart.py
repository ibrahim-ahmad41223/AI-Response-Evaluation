#!/usr/bin/env python3
"""Build analysis/points-lost.svg from scores/scores.csv and responses/README.md from prompts/.

Run:  python tools/make_chart.py
Standard library only.
"""
import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MODELS = [("gemini", "Gemini"), ("claude", "Claude"), ("grok", "Grok"), ("chatgpt", "ChatGPT")]
DIMS = [
    ("accuracy", "Accuracy", "#2a6fbb"),
    ("instruction_following", "Instruction-Following", "#d9822b"),
    ("completeness", "Completeness", "#6a8f3a"),
    ("clarity", "Clarity", "#8a5fb0"),
]


def load_scores():
    with open(ROOT / "scores" / "scores.csv", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def points_lost(rows):
    lost = {m: {d: 0 for d, _, _ in DIMS} for m, _ in MODELS}
    for r in rows:
        for d, _, _ in DIMS:
            lost[r["model"]][d] += 5 - int(r[d])
    return lost


def build_svg(lost):
    W, left, top, bar_h, gap = 720, 110, 70, 34, 18
    scale = 34  # px per lost point
    n = len(MODELS)
    H = top + n * (bar_h + gap) + 80
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
        'font-family="-apple-system, Segoe UI, Helvetica, Arial, sans-serif" role="img" '
        'aria-label="Points lost per model, split by scoring dimension">',
        f'<rect width="{W}" height="{H}" fill="#ffffff"/>',
        '<text x="24" y="32" font-size="18" font-weight="600" fill="#1f2328">Points lost per model (out of 600 available)</text>',
        '<text x="24" y="52" font-size="12" fill="#57606a">Each response is scored 1-5 on four dimensions; a point lost is 5 minus the score. Fewer is better.</text>',
    ]
    for i, (key, label) in enumerate(MODELS):
        y = top + i * (bar_h + gap)
        out.append(f'<text x="{left - 12}" y="{y + bar_h / 2 + 5}" font-size="14" text-anchor="end" fill="#1f2328">{label}</text>')
        x = left
        total = 0
        for d, dl, color in DIMS:
            v = lost[key][d]
            total += v
            if v:
                w = v * scale
                out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{bar_h}" fill="{color}"><title>{label}: {v} lost in {dl}</title></rect>')
                if w >= 18:
                    out.append(f'<text x="{x + w / 2}" y="{y + bar_h / 2 + 5}" font-size="13" text-anchor="middle" fill="#ffffff" font-weight="600">{v}</text>')
                x += w
        out.append(f'<text x="{x + 10}" y="{y + bar_h / 2 + 5}" font-size="14" font-weight="600" fill="#1f2328">{total}</text>')
    ly = top + n * (bar_h + gap) + 14
    lx = left
    for d, dl, color in DIMS:
        out.append(f'<rect x="{lx}" y="{ly}" width="14" height="14" rx="2" fill="{color}"/>')
        out.append(f'<text x="{lx + 20}" y="{ly + 12}" font-size="12" fill="#1f2328">{dl}</text>')
        lx += 20 + len(dl) * 7 + 22
    out.append("</svg>")
    return "\n".join(out) + "\n"


def prompt_index():
    lines = [
        "# Responses",
        "",
        "Each model's response to each prompt, saved exactly as returned from the websites (see the notes in the [main README](../README.md)).",
        "Click a model name to read its response. Scores and notes are in [`scores/scores.csv`](../scores/scores.csv).",
        "",
        "| Prompt | Starts with | Grok | ChatGPT | Gemini | Claude |",
        "|---|---|---|---|---|---|",
    ]
    for p in sorted((ROOT / "prompts").glob("P*.txt")):
        pid = p.stem
        text = re.sub(r"\s+", " ", p.read_text(encoding="utf-8")).strip()
        snippet = (text[:70].rstrip() + "...") if len(text) > 70 else text
        snippet = snippet.replace("|", "\\|").replace("`", "")
        links = " | ".join(f"[{name}]({pid}/{m}.md)" for m, name in
                           [("grok", "Grok"), ("chatgpt", "ChatGPT"), ("gemini", "Gemini"), ("claude", "Claude")])
        lines.append(f"| [{pid}](../prompts/{pid}.txt) | {snippet} | {links} |")
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    lost = points_lost(load_scores())
    (ROOT / "analysis" / "points-lost.svg").write_text(build_svg(lost), encoding="utf-8", newline="\n")
    (ROOT / "responses" / "README.md").write_text(prompt_index(), encoding="utf-8", newline="\n")
    for m, name in MODELS:
        print(name, sum(lost[m].values()), lost[m])
