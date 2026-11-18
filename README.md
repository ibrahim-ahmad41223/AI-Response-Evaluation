# AI-Response-Evaluation

A benchmark comparing how four AI models respond to the same 30 prompts, scored on accuracy, instruction-following, completeness and clarity.

## Models

| Provider | Model | Access | Settings |
|---|---|---|---|
| Google Gemini | Gemini 4 Hydrogen | Website | Everyday Help |
| OpenAI ChatGPT | Default model (version not disclosed) | Website | Default settings |
| xAI Grok | Default model (version not disclosed) | Website | Fast |
| Anthropic Claude | Claude Sonnet 5.5 | Website | Low effort |

All responses were collected on 2026-11-13.

## Results at a glance

Mean score across the four dimensions (30 responses per model, scale 1–5):

| Model | Mean | Responses scored 5 on every dimension |
|---|:-:|:-:|
| Gemini | 4.96 | 26 / 30 |
| Claude | 4.92 | 24 / 30 |
| Grok | 4.91 | 25 / 30 |
| ChatGPT | 4.88 | 22 / 30 |

The gaps are small and come from a single human evaluator (with AI-assisted rubric review) and a limited sample, so these numbers are not a ranking of which model is best. See [`analysis/final-analysis.md`](analysis/final-analysis.md) for the per-dimension breakdown, error patterns and limitations.

## Repository layout

| Path | Contents |
|---|---|
| `prompts/` | The 30 prompts, `P01.txt` to `P30.txt`. |
| `responses/` | Each model's response, saved exactly as returned: `responses/Pxx/{grok,chatgpt,gemini,claude}.txt`. `responses/collection-log.csv` records the model, access method, settings and date for every response. |
| `scores/rubric.md` | The 1–5 definitions for each dimension and the scoring principles. |
| `scores/scores.csv` | One row per response: four scores and a note explaining every deduction. |
| `analysis/final-analysis.md` | Results, error patterns, scoring decisions and limitations. |
| `docs/methodology.md` | How the benchmark was designed, collected and scored. |
| `tools/` | The local scoring tool. |

## Scoring tool

Run `python tools/scorer.py` and the scoring page opens in your browser. It shows one response at a time (model names hidden until all four scores are set), and every score is written straight to `scores/scores.csv`. Re-running resumes where you left off. Requires Python 3 only.

If you edit `scores/scores.csv` by hand, restart the tool afterwards: it loads the file once on startup and will overwrite outside edits the next time it saves.

## Notes

- Scores were produced by the evaluator together with an AI assistant (Claude); the evaluator reviewed and approved every final score. See `docs/methodology.md`.
- Responses are stored verbatim, including any copy-paste artifacts from the websites (such as image links). These were not counted against the models.
- Results reflect the models only as they behaved on the collection date.
