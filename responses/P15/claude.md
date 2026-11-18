I'll start by checking which models are currently generally available.

Now I'll confirm Gemini's newest generally available model.

I can't run either model here, so I have no accuracy or speed measurements. I have no API access to Gemini or Grok in this conversation and no way to time requests under controlled conditions. Anything I reported as a result would be invented. What I can give you is the verified model identification as of today and a procedure you can run yourself.

## Models to test (as of November 13, 2026)

| | Gemini | Grok |
|---|---|---|
| Model | Gemini 4 Argon | Grok 4.7 |
| API ID | `gemini-4-argon` | `grok-4.7` |
| GA status | Generally available in the Gemini API on October 13, 2026, on the paid tier only | xAI's docs list Grok 4.7 as the flagship; its knowledge cutoff is May 2026 |
| Context | Not verified | 500k tokens |

**Sources:**
- Gemini's release notes list Argon under the October 13 date. Google's changelog also lists the deprecation of Gemini 3.7 Flash in favor of 3.8 Flash.
- xAI's model page, last updated September 21, 2026, lists grok-4.7 as the flagship.
- Third-party trackers corroborate these. One tracker checked on 2026-11-05 found no Grok 5 and named Grok 4.7 as the newest released model.

**Caveats on the selection:**
- Argon and Grok 4.7 are flagships, not like-for-like tiers. For a speed-focused comparison, `gemini-3.8-flash` is arguably the fairer Gemini counterpart. It was generally available as of September 2, 2026.
- Grok 4.8 is rumored, but as of November 10, 2026 there was no xAI announcement, model page, or release note for it. I excluded it because it isn't generally available.
- Recheck both vendors' model pages on your test day, since both ship new versions every few weeks.

## Five questions and reference answers

I chose these because they have stable, checkable answers. They are likely too easy for flagship models, so treat this as a harness check and add harder questions for a real comparison.

1. Which element has the symbol W, and what is its atomic number? **Tungsten, 74.**
2. Who was the first woman to win a Nobel Prize, and in which field(s)? **Marie Curie: Physics (1903) and Chemistry (1911).**
3. In what year was the Peace of Westphalia signed? **1648.**
4. Who wrote *One Hundred Years of Solitude*, and when was it first published? **Gabriel García Márquez, 1967.**
5. What is the exact speed of light in a vacuum in m/s? **299,792,458.**

Verify these references against an independent source before grading.

## Measuring speed

Use streaming requests and record three metrics per request:
- **TTFT (time to first token):** the time from sending the request to the first content chunk, using a monotonic clock (`time.perf_counter()`).
- **Total latency:** the time from sending the request to the final chunk.
- **Output tokens:** use each API's reported usage count. Tokenizers differ, so also record characters.

Run each question at least 20 times per model, interleaving the two models randomly. Report the median and p95, not the mean. Run from one machine and region within the same time window. Match the reasoning settings for both models and record them, since thinking time dominates latency on these models. Cap max output tokens identically and use no tools or search.

## Reproducible script

```python
import time, json, random, statistics, datetime, os
from google import genai
from openai import OpenAI

QUESTIONS = [
 "Which element has the symbol W, and what is its atomic number?",
 "Who was the first woman to win a Nobel Prize, and in which field(s)?",
 "In what year was the Peace of Westphalia signed?",
 "Who wrote One Hundred Years of Solitude, and when was it first published?",
 "What is the exact speed of light in a vacuum in m/s?",
]
RUNS = 20
gem = genai.Client()  # GEMINI_API_KEY
grok = OpenAI(base_url="https://api.x.ai/v1", api_key=os.environ["XAI_API_KEY"])

def run_gemini(q):
    t0 = time.perf_counter(); ttft = None; text = ""
    for chunk in gem.models.generate_content_stream(model="gemini-4-argon", contents=q):
        if chunk.text and ttft is None: ttft = time.perf_counter() - t0
        text += chunk.text or ""
    return ttft, time.perf_counter() - t0, text

def run_grok(q):
    t0 = time.perf_counter(); ttft = None; text = ""
    for chunk in grok.chat.completions.create(
            model="grok-4.7", messages=[{"role": "user", "content": q}], stream=True):
        d = chunk.choices[0].delta.content if chunk.choices else None
        if d and ttft is None: ttft = time.perf_counter() - t0
        text += d or ""
    return ttft, time.perf_counter() - t0, text

jobs = [(m, q, i) for m in ("gemini", "grok") for q in QUESTIONS for i in range(RUNS)]
random.shuffle(jobs)  # interleave to spread network/time-of-day effects
rows = []
for m, q, i in jobs:
    ttft, total, text = (run_gemini if m == "gemini" else run_grok)(q)
    rows.append(dict(model=m, q=q, run=i, ttft=ttft, total=total, text=text,
                     ts=datetime.datetime.utcnow().isoformat()))
json.dump(rows, open("results.json", "w"), indent=1)
```

Before running, check each vendor's current docs for reasoning/thinking parameters and set them to comparable levels. I did not verify Argon's parameter names. I left sampling parameters unset because Google deprecated `temperature`, `top_p`, and `top_k` on recent Flash models, and I haven't confirmed Argon's behavior.

**Grading:** have two people grade the saved `text` blind to model identity as correct, partially correct, or incorrect against the references. Report agreement between graders and the per-model counts across all runs. Record the UTC test date, the exact model IDs, SDK versions, region, and reasoning settings.

## Limitations

- **No direct measurement here.** I had no API access to either model, so this answer contains no results.
- **Sample size.** Five questions can't separate two strong models. Most flagship models will score 5/5, so accuracy differences would be noise.
- **Mismatched tiers and settings.** Flagship versus flagship isn't the same as equal cost or equal reasoning effort. Reasoning settings, pricing, and tokenization differ.
- **Speed is environment-dependent.** It varies with your network, region, time of day, provider load, and rate limits. Argon is paid-tier only, so your tier affects throughput.
- **Fast-moving targets.** Model aliases and versions can change under you. Pin exact IDs and log them.
- **Source quality.** Vendor docs are the most reliable sources. I relied on third-party trackers for some release dates and for the absence of Grok 5 and 4.8, so check xAI's release notes yourself.

If you'd like, I can write a harder question set (including false-premise and recent-events questions) or a script to compute the medians and p95 from `results.json`.