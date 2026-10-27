# Worked example: signup qualification vs conversion

This shows the reasoning trail the skill follows. In a normal answer most of it stays hidden;
the user sees the ideas, why they work, the risks and the next step.

## Situation
A B2B SaaS company. Sales wants company size, role and use case at signup to route leads.
Growth reports that each extra field costs conversion. Today the form has two fields.

## Gate
A trade-off where neither side accepts a compromise → TRIZ applies. Standard mode.

## Model
- System: signup flow; main function: turn visitors into users who can be routed correctly.
- Undesired effect: either poor routing (few fields) or lost signups (many fields).
- Operating zone: the signup form. Operating time: the first minute of the visit.
- IFR: "the user's normal use of the product itself, without extra steps, tells us their
  company size, role and use case."

## Technical contradiction
- TC-1: if we add fields, lead qualification improves, but signup takes longer and is harder.
- Parameters: improving 28 (measurement accuracy); worsening 33 (ease of operation) and 25 (loss of time).

```
$ python scripts/matrix.py --improve 28 --worsen 33 25
Improve 28 Measurement accuracy  vs  worsen 33 Ease of operation
  1 Segmentation, 13 The other way round, 17 Another dimension, 34 Discarding and recovering
Improve 28 Measurement accuracy  vs  worsen 25 Loss of time
  24 Intermediary, 34 Discarding and recovering, 28 Mechanics substitution, 32 Color changes
```

## Principles → ideas
- **1 Segmentation**: ask one question per session, at moments when it is natural
  (progressive profiling).
- **13 The other way round**: instead of the user telling us, we tell the user: show "Looks
  like you're at a 50-person company, right?" from enrichment, and they only confirm.
- **17 Another dimension**: collect the data in another channel or moment: the invite step
  ("invite your team") reveals team size by itself.
- **34 Discarding and recovering**: questions disappear once answered or inferred; no one is
  asked twice.
- **24 Intermediary**: an enrichment service fills company data from the email domain.
- **28 Mechanics substitution**: replace typing with signals: sign-in with a work account
  brings company and role; behavior in the first session reveals the use case.

## Physical contradiction
The form must be long (to qualify) and short (to convert).
- Separation in time: short at signup, questions later in context.
- Separation by condition: long only for visitors with high-intent signals (pricing page,
  "talk to sales"), short for everyone else.

## Resources
Email domain, work-account sign-in, the invite step, the template the user chooses first,
pages visited before signup, the sales call that will happen anyway for big accounts.

## Answer the user would see (condensed)
1. **Infer, then confirm** (strongest): enrich from the work email and show the guess for
   one-tap confirmation. Removes most typing; risk: wrong guesses for personal emails, so fall
   back to one question.
2. **Let the product ask**: use the first template choice as the use case and the invite step as
   team size. Zero added fields; risk: delayed data for routing in the first hour.
3. **Long form only for high intent**: show extra fields only after "talk to sales".
**Next step:** A/B test idea 1 against the current form for two weeks; measure signup rate
and the share of correctly routed leads.
