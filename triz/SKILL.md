---
name: triz
description: Solve stuck design, engineering, software, product or business problems with TRIZ (Theory of Inventive Problem Solving, ТРИЗ). Use when improving one thing makes another worse (a trade-off nobody wants to compromise on), when something must be both X and not-X, when obvious fixes have failed, or when the user asks for TRIZ, the contradiction matrix, the 40 inventive principles, the ideal final result (ИКР), ARIZ (АРИЗ), separation principles or su-field analysis. Also use to forecast how a product or technology will evolve. Do not use for ordinary bugs, known-pattern tasks or pure preference questions.
---

# TRIZ

TRIZ resolves contradictions instead of trading them off. The aim is a solution where both
conflicting requirements are met, usually by using resources the system already has.

The method is your thinking scaffold, not the deliverable. The user wants concrete, specific
ideas that would actually work in their situation. Terminology without concrete mechanisms is
"framework theater" and makes the answer worse.

## 0. Gate: is TRIZ the right tool?

Use TRIZ when at least one holds:
- improving A degrades B, and a compromise between them is not good enough;
- one element must have opposite properties (fast and slow, present and absent);
- the obvious solutions have been tried, or the problem keeps coming back;
- the user explicitly asks for TRIZ or one of its tools.

Do NOT use TRIZ when the task is a defect with a findable cause (debug it), a known pattern
answers it, it needs measurement or data before anything else, or it is a matter of taste.
In those cases just help directly and do not mention TRIZ.

## 1. Choose the depth

- **Quick** (default): one clear contradiction. Steps 2–4, then 7.
- **Standard**: the conflict is fuzzy or the matrix gives weak hints. Steps 2–7.
- **Deep**: a hard, long-standing or high-stakes problem, or the user asks for ARIZ.
  Follow `references/ariz.md`, which reuses the steps below.

## 2. Model the problem

Before any solution, state:
- **System and its main function** (what it is for, from the user's point of view).
- **Undesired effect**: what goes wrong, where, when. Be concrete.
- **Constraints**: what must not change; cost, time, regulation.
- **Mini-problem**: "achieve the result with minimal change to the system."

If key facts are missing and guessing would change the answer, ask one or two short
questions. Otherwise state assumptions and continue.

Then formulate the **Ideal Final Result (IFR)**: "X ITSELF, without complicating the system,
without cost or harm, eliminates the undesired effect while keeping the useful function."
Name the element X. The IFR points at where to look, not at what is achievable.
Details: `references/problem-modeling.md`.

## 3. Technical contradiction → matrix → principles

1. Write it as a pair: "If we [action], then [A improves] but [B worsens]." Also write the
   reverse pair (the opposite action improves B and worsens A). Both are useful.
2. Map A and B to the 39 parameters. Use `references/parameters.md` for meaning and for
   non-technical equivalents (software, product, business, process). Pick 1–2 candidates for
   each side when the mapping is uncertain.
3. Look up the matrix with the script. Never recall matrix cells from memory; they are
   easy to get wrong.

   ```bash
   python scripts/matrix.py 9 14                       # improving 9, worsening 14
   python scripts/matrix.py --improve 9 39 --worsen 14 36   # several pairs, ranked
   python scripts/matrix.py --find "latency"            # find parameters by keyword
   ```
   If scripts cannot run, open `scripts/matrix.json` and read the key `"improving,worsening"`.
   An empty cell means the classic matrix has no recommendation: go to step 4.
4. Read the suggested principles in `references/principles.md`. For each one, produce at
   least one idea specific to this system (name the actual component, data, step or actor).
   Discard a principle only after trying it seriously.

## 4. Physical contradiction → separation

Sharpen the technical contradiction down to one element with opposite demands:
"[element] must be [P] in order to [benefit 1] and must be [not-P] in order to [benefit 2]."

Resolve it by separating the opposite demands: in time, in space, by condition, or between
the whole and its parts (system levels). See `references/separation.md`, which also maps each
separation to the principles that typically implement it.

Physical contradictions usually give stronger ideas than the matrix. In Standard and Deep
modes always do this step.

## 5. Resources

List what is already in or around the system and costs nothing: substances and materials,
fields and energy, time windows, empty space, information and data that already exist,
people and their existing behavior, by-products and waste. Then ask which resource could play
element X from the IFR. See `references/resources.md`.

## 6. Additional tools (when relevant)

- **Su-field analysis and standard solutions** when the problem is about an interaction that
  is missing, insufficient, harmful, or hard to measure/detect: `references/su-field.md`.
- **Trends of evolution** when the question is "what comes next" for a product or technology,
  or to check whether an idea goes with or against the direction of evolution:
  `references/evolution.md`.

## 7. Evaluate and answer

For each idea check: does it remove the contradiction or only move it? How close is it to the
IFR? What new problem does it create (a secondary contradiction)? Rough cost and effort to try.

Answer format, adapted to the request:

1. **The core conflict** in one or two plain sentences.
2. **Strongest ideas** (2–5): the concrete mechanism, why it resolves the conflict, and the
   main risk. Lead with the best one.
3. **Other ideas worth a look**, briefly.
4. **Next step**: the cheapest experiment that would confirm or kill the best idea.

Show the TRIZ trail (parameters, matrix cell, principle numbers, IFR wording) only when the
user asked for a TRIZ analysis or explicitly wants the reasoning. Otherwise keep the method
out of sight and mention at most the principle behind an idea in a few words.

Respond in the user's language. Russian TRIZ terms: противоречие, ИКР, вепольный анализ,
приёмы, принципы разрешения противоречий, ресурсы, АРИЗ.

## Pitfalls

- Jumping to solutions before the contradiction is clear.
- Mapping to parameters too loosely, then forcing principles that do not fit.
- Listing principles with generic advice ("make it dynamic") instead of concrete mechanisms.
- Accepting a compromise and calling it a solution.
- Adding complexity (a new subsystem) when a resource already present could do the job.
- Using engineering parameters literally for business problems: translate them.
