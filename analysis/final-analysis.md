# Final Analysis

This analysis summarises the 120 scores in [`scores/scores.csv`](../scores/scores.csv): 30 prompts, each answered by four models and scored 1–5 on accuracy, instruction-following, completeness and clarity under [`scores/rubric.md`](../scores/rubric.md). Models, access methods and settings are in [`docs/methodology.md`](../docs/methodology.md). Responses were collected on 2026-11-13.

The differences between models are small and the sample is limited (see [Limitations](#limitations)). This is a description of what the scores show, not a ranking of which model is best.

## 1. Overall results

Mean score per dimension (30 responses per model) and the number of responses scored 5 on all four dimensions:

| Model | Accuracy | Instruction-Following | Completeness | Clarity | Mean of four | All-5 responses |
|---|:-:|:-:|:-:|:-:|:-:|:-:|
| Gemini | 4.90 | 4.93 | 5.00 | 5.00 | 4.96 | 26 / 30 |
| Claude | 4.80 | 4.93 | 5.00 | 4.97 | 4.92 | 24 / 30 |
| Grok | 4.77 | 4.87 | 5.00 | 5.00 | 4.91 | 25 / 30 |
| ChatGPT | 4.80 | 4.80 | 4.93 | 5.00 | 4.88 | 22 / 30 |

Across all 480 individual scores, 454 were 5, 14 were 4, 11 were 3 and 1 was 2. No score was 1. Sixteen of the 30 prompts produced at least one point deduction; the other 14 were scored 5 on every dimension for every model.

The gap between the highest and lowest mean (4.96 vs 4.88) is 0.08 of a point. In raw terms, out of 600 available points per model (30 responses × 4 dimensions × 5), ChatGPT lost 14 and Gemini lost 5, a difference of 9 points. Given the sample size, it should not be read as a meaningful difference in ability.

## 2. Where points were lost

Almost all deductions fall in accuracy and instruction-following. Completeness lost a point once (ChatGPT, P25) and clarity once (Claude, P09). Nobody lost a point in clarity otherwise.

| Model | Deductions | Prompts |
|---|---|---|
| Grok | 4 accuracy, 2 instruction-following | Accuracy: P05 (2), P06 (3), P15 (4), P24 (4). Instruction-following: P05 (3), P30 (3). |
| ChatGPT | 5 accuracy, 4 instruction-following, 1 completeness | Accuracy: P03, P05 (3), P16, P19, P20 (all 4 except P05). Instruction-following: P02 (4), P04 (3), P05 (3), P20 (4). Completeness: P25 (3). |
| Gemini | 3 accuracy, 1 instruction-following | Accuracy: P05, P07, P09 (all 4). Instruction-following: P20 (3). |
| Claude | 4 accuracy, 1 instruction-following, 1 clarity | Accuracy: P10 (4), P15 (3), P18 (3), P30 (4). Instruction-following: P05 (3). Clarity: P09 (4). |

The lowest-scoring prompt was P05 (the real-GDP-growth question with a "fewer than five qualify" rule). It was the only prompt where every model lost points, and it produced the only score of 2 (Grok).

## 3. Patterns by type of error

These patterns come from the notes in the CSV. Each is based on a handful of responses, so treat them as observations rather than findings.

- **Factual slips inside otherwise correct answers.** Many accuracy deductions were an error in a secondary detail while the main answer was right: Grok's two backwards short-circuit examples in P06, Claude's wrong standard deviation in P18, ChatGPT's sample output not matching its own code in P16, Claude listing Italy on the wrong side in P30. The headline answer was correct in each case.
- **Missing "minimal" in key definitions.** ChatGPT (P03, P19) and Grok (P24) defined a candidate key without saying it must be minimal.
- **Constraint and citation instructions.** Instruction-following losses came from specific, checkable constraints: one example only (ChatGPT, P04), only the two requested bullets (ChatGPT, P02), citing sources (Claude P05, Grok P30), and using only the evidence supplied (ChatGPT and Gemini, P20). Word limits, paragraph counts and required words were met by all four models in the prompts where they applied (P10, P21, P28, P30), subject to the title-counting judgement calls in section 5.
- **Current-events accuracy.** Prompts that depend on recent facts (P05, P09, P15, P25) account for a disproportionate share of deductions. In P15, Claude identified an older Gemini model than the one generally available on the test date; in P09 Gemini made a misleading claim about mutual-defense pacts. All four models rejected the false premise in P09 and P17 (no World War 3, no human Mars landing) and in P24 (the primary key definition was reversed).
- **Honesty about limits.** In P15 all four models stated they could not run or time the other model and provided a testing procedure instead of inventing results. In P27 (no information available about the user) none of the four invented an answer, and in P22 (the answer was stated in the prompt) all four answered correctly.
- **Formatting and extras.** ChatGPT often added a closing offer or practice suggestion, and its pasted responses contained interface artifacts (image links, quiz widgets). These were treated as copy artifacts and not penalised, except where a prompt restricted the format (P02).

## 4. Scoring decisions worth knowing

- Ratings were first entered by the evaluator, then reviewed against the rubric, and some were changed with a reason recorded in the `note` column. Every score below 5 has a note.
- Formatting damage from copying responses off the websites (flattened code, image markup, tab-separated tables) was not counted against the model. One ChatGPT response (P15) was restored to its original code block after the evaluator supplied it.
- The same defect was scored consistently across prompts where possible (for example, the missing "minimal" in candidate-key definitions, and absent citations when the prompt required them).

## 5. Limitations

- **Single evaluator.** All scores come from one person, with a rubric-based review pass. They have not been independently verified.
- **Narrow score range.** Most scores are 5, so the benchmark separates models only through a small number of deductions, and a single changed score can alter the ordering. The means above should not be treated as precise.
- **Small sample.** Thirty prompts cannot represent every task type, and each model answered each prompt once, so response variability is not captured.
- **Settings are not identical.** The models were accessed through websites with different defaults (Gemini 4 Hydrogen on Everyday Help, Claude Sonnet 5.5 on Low effort, Grok on Fast, ChatGPT on its default). Features such as web search or account integrations may have differed. For example, Gemini's P27 answer mentions searching the user's Gmail and Drive.
- **Time-sensitive prompts.** Answers to P05, P09, P15, P17 and P25 depend on events up to 2026-11-13 and some claims could only be partly checked against sources. Several deductions rely on what was known on the test date.
- **Judgement calls.** Some checks were ambiguous: whether titles count toward word limits (Claude's P21 and P28 essays pass without the title and exceed the limit by 1–2 words with it), whether naming a source counts as a citation (P15, P25), and whether a required word in lowercase satisfies "include the word" (Gemini, P28). These were scored in the models' favour.
- **Code was checked by reading, not compiling.** Programs in P07, P14, P16 and P26 were traced by hand, as no C++ compiler was available.
