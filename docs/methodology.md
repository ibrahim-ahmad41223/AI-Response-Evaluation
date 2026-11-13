# Methodology

This document describes how the AI Response Evaluation Benchmark is designed and carried out. The project is ongoing, so this document describes the intended procedure and will be refined as the work progresses.

## 1. Project Overview

The purpose of this project is to compare how four AI models respond to the same set of prompts. Each response is assessed on four dimensions: accuracy, instruction-following, completeness, and clarity.

Using identical prompts and a single shared rubric allows the responses to be compared on consistent terms. The goal is to document observable strengths and weaknesses of each model across different kinds of tasks, not to declare a single overall "best" model.

## 2. Models Evaluated

Four AI models are included in the benchmark:

| Provider | Model Version | Access Method | Settings |
|---|---|---|---|
| Google Gemini | 4 Hydrogen | Website | Everyday Help |
| OpenAI ChatGPT | Default model (exact version not disclosed) | Website | Default settings |
| xAI Grok | Default model (exact version not disclosed) | Website | Fast |
| Anthropic Claude | Claude Sonnet 5.5 | Website | Low effort |

## 3. Evaluation Prompts

The benchmark is designed around 30 prompts, covering a range of task types and difficulty levels. Each prompt is stored as its own file in the `prompts/` directory and is identified by a zero-padded ID (`P01` through `P30`).

The 30 prompts have been designed and finalised, but their individual files are still being populated. The benchmark is a work in progress, so not every prompt file contains its text yet.

## 4. Response Collection Procedure

1. The same prompt is submitted, word for word, to each of the four models.
2. Whenever a prompt requires context or attachments, identical context and attachments must be provided to all models.
3. Each model's response is saved exactly as it was returned, without editing, trimming, or reformatting.
4. Responses are stored in a folder named after the prompt, with one file per model:

   ```
   responses/
   └── P01/
       ├── gemini.txt
       ├── chatgpt.txt
       ├── grok.txt
       └── claude.txt
   ```

Preserving responses unedited ensures that scoring reflects what each model actually produced.

## 5. Evaluation Rubric

Every response is scored on four dimensions:

- **Accuracy** — whether the content is factually correct.
- **Instruction-Following** — whether the explicit instructions in the prompt were obeyed.
- **Completeness** — whether everything the prompt requires is covered.
- **Clarity** — whether the response is easy to understand for its intended audience.

Each dimension is scored independently on a scale from 1 to 5. The full score definitions and scoring principles are in [`scores/rubric.md`](../scores/rubric.md).

## 6. Scoring Procedure

Each response is evaluated individually against the same rubric. The evaluator reads the prompt and a single response, then assigns a 1–5 score for each of the four dimensions according to the definitions in `scores/rubric.md`.

Scores are recorded in `scores/scores.csv`. Notes and conclusions drawn from the scores belong in `analysis/final-analysis.md`.

## 7. Limitations

- **Model updates.** Providers update their models and products over time, so the same prompt may produce a different response at a later date. Results reflect the models only at the time each response was collected.
- **Differences in model settings.** Models may be accessed through different interfaces and may use different default settings, system instructions, or features (such as web search). These differences may affect responses and may not be fully controllable or visible.
- **Subjective judgment.** Although a defined rubric is used, assigning scores involves human judgment, particularly for clarity and completeness. Different evaluators could reasonably assign different scores.
- **Single Evaluator.** All responses are scored by one evaluator, which may introduce individual bias. The scores have not been independently verified by additional evaluators.
- **Limited sample size.** A benchmark of 30 prompts cannot represent every task or domain, so findings should not be generalised beyond the prompts tested.
- **Response variability.** A model may return different answers to the same prompt on different attempts. Each prompt is evaluated on the response collected, which may not be representative of every possible output.
