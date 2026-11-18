#!/usr/bin/env python3
"""Local scoring tool for the AI response evaluation.

Run:  python tools/scorer.py
Then it opens http://127.0.0.1:8765 in your browser. Every score you enter is
written straight to scores/scores.csv (no manual export). Re-running the tool
resumes from whatever is already in that file.

Standard library only. Reads prompts/, responses/ and scores/rubric.md.
"""
import csv
import json
import os
import random
import re
import sys
import tempfile
import threading
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PORT = int(os.environ.get("SCORER_PORT", "8765"))
MODELS = ["grok", "chatgpt", "gemini", "claude"]
DIMS = ["accuracy", "instruction_following", "completeness", "clarity"]
FIELDS = ["prompt_id", "model", *DIMS, "note"]
SCORES_CSV = ROOT / "scores" / "scores.csv"
LOCK = threading.Lock()


def read_text(path):
    # newline="" keeps the file's own line endings untouched
    with open(path, encoding="utf-8", newline="") as f:
        return f.read()


def parse_rubric():
    """Read score descriptions and principles from scores/rubric.md (single source of truth)."""
    text = read_text(ROOT / "scores" / "rubric.md")
    dims, principles, section = {}, [], None
    for line in text.splitlines():
        m = re.match(r"## \d+\. (.+)", line)
        if m:
            name = m.group(1).strip().lower().replace("-", "_")
            section = name
            dims[name] = {}
            continue
        if line.startswith("## Scoring Principles"):
            section = "__principles"
            continue
        if section == "__principles":
            if line.startswith("- "):
                principles.append(line[2:])
        elif section:
            m = re.match(r"\|\s*\*\*(\d)\*\*\s*\|\s*(.+?)\s*\|\s*$", line)
            if m:
                dims[section][m.group(1)] = m.group(2)
    return dims, principles


def load_prompts():
    prompts = []
    for p in sorted((ROOT / "prompts").glob("P*.txt")):
        pid = p.stem
        responses = {}
        for model in MODELS:
            f = ROOT / "responses" / pid / f"{model}.md"
            responses[model] = read_text(f) if f.exists() else ""
        order = MODELS[:]
        random.Random(pid).shuffle(order)  # fixed blind order per prompt
        prompts.append({"id": pid, "text": read_text(p), "responses": responses, "order": order})
    return prompts


def load_scores():
    scores = {}
    if SCORES_CSV.exists() and SCORES_CSV.stat().st_size > 0:
        with open(SCORES_CSV, encoding="utf-8", newline="") as f:
            for row in csv.DictReader(f):
                key = f"{row['prompt_id']}|{row['model']}"
                entry = {d: (int(row[d]) if row.get(d) else None) for d in DIMS}
                entry["note"] = row.get("note", "") or ""
                scores[key] = entry
    return scores


def write_scores(scores):
    def sort_key(k):
        pid, model = k.split("|")
        return (pid, MODELS.index(model))

    rows = []
    for key in sorted(scores, key=sort_key):
        e = scores[key]
        if not any(e[d] for d in DIMS) and not e["note"].strip():
            continue
        pid, model = key.split("|")
        rows.append({"prompt_id": pid, "model": model, **{d: e[d] if e[d] else "" for d in DIMS}, "note": e["note"]})
    fd, tmp = tempfile.mkstemp(dir=SCORES_CSV.parent, suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=FIELDS, lineterminator="\n")
            w.writeheader()
            w.writerows(rows)
        os.replace(tmp, SCORES_CSV)
    except Exception:
        if os.path.exists(tmp):
            os.unlink(tmp)
        raise


PROMPTS = load_prompts()
VALID_IDS = {p["id"] for p in PROMPTS}
RUBRIC, PRINCIPLES = parse_rubric()
SCORES = load_scores()


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *args):
        pass

    def _host_ok(self):
        host = (self.headers.get("Host") or "").rsplit(":", 1)[0]
        return host in ("127.0.0.1", "localhost")

    def _send(self, code, body, ctype="application/json"):
        data = body if isinstance(body, bytes) else body.encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", ctype + "; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        if not self._host_ok():
            return self._send(403, "{}")
        if self.path in ("/", "/index.html"):
            return self._send(200, (Path(__file__).parent / "scorer.html").read_bytes(), "text/html")
        if self.path == "/api/data":
            with LOCK:
                payload = {"prompts": PROMPTS, "models": MODELS, "dims": DIMS,
                           "rubric": RUBRIC, "principles": PRINCIPLES, "scores": SCORES}
                return self._send(200, json.dumps(payload))
        self._send(404, "{}")

    def do_POST(self):
        if not self._host_ok() or self.path != "/api/score":
            return self._send(403, "{}")
        if "application/json" not in (self.headers.get("Content-Type") or ""):
            return self._send(415, "{}")
        try:
            body = json.loads(self.rfile.read(int(self.headers.get("Content-Length") or 0)))
            pid, model = body["prompt_id"], body["model"]
            if pid not in VALID_IDS or model not in MODELS:
                raise ValueError("unknown prompt or model")
            entry = {}
            for d in DIMS:
                v = body.get(d)
                if v in (None, ""):
                    entry[d] = None
                elif isinstance(v, int) and 1 <= v <= 5:
                    entry[d] = v
                else:
                    raise ValueError(f"bad value for {d}")
            entry["note"] = str(body.get("note", ""))[:2000]
        except Exception as exc:
            return self._send(400, json.dumps({"error": str(exc)}))
        with LOCK:
            SCORES[f"{pid}|{model}"] = entry
            try:
                write_scores(SCORES)
            except OSError as exc:  # e.g. scores.csv is open in Excel
                return self._send(500, json.dumps({"error": f"Could not write scores.csv: {exc}"}))
        self._send(200, json.dumps({"ok": True}))


if __name__ == "__main__":
    server = ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    url = f"http://127.0.0.1:{PORT}"
    print(f"Scorer running at {url}  (Ctrl+C to stop)")
    print(f"Scores are saved automatically to {SCORES_CSV}")
    if "--no-browser" not in sys.argv:
        webbrowser.open(url)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
