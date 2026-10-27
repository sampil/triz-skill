# Modeling the problem

Most failed TRIZ attempts fail here: the contradiction is formulated vaguely or about the wrong
thing. Spend effort on this step.

## 1. From situation to problem

A user usually describes a *situation* (many issues at once). Pick one problem to solve:
- Which undesired effect matters most?
- Is it a cause or a symptom? Build a short cause-effect chain from the visible symptom back
  to root causes ("why does this happen?" 3–5 times). Choose the link where intervention is
  cheapest or where a contradiction first appears.
- Consider the inverse problem: instead of removing harm, could the system tolerate or use it?

## 2. Function model (for Standard and Deep modes)

List the main components of the system and of its immediate environment (including people,
data and the product being processed). For each pair that interacts, label the action:
- **useful and sufficient**;
- **useful but insufficient** (too weak, too slow, unreliable);
- **useful but excessive**;
- **harmful**.

Problems live on the insufficient, excessive and harmful links. A component that only performs
auxiliary functions is a candidate for **trimming**: can its function be done by another
component or made unnecessary, so the component can be removed?

## 3. Operating zone and operating time

- **Operating zone**: the exact place where the conflict happens (a surface, an interface, a
  step in a flow, one screen).
- **Operating time**: when it happens (before, during, after; peak vs off-peak).
Narrowing the zone and time often reveals that the opposite demands do not actually overlap,
which opens separation in space or time.

## 4. Mini-problem

"Keep the system as it is (or simplify it) and eliminate the undesired effect." This forbids the
easy escape of adding a new subsystem and forces the use of resources. Relax it only if no
solution appears.

## 5. Ideal Final Result (IFR)

Template: "**X itself**, without complicating the system and without harmful effects,
eliminates [undesired effect] during [operating time] within [operating zone], while keeping
[useful function]."

- X is an existing element or resource (a component, the product, the environment, the user,
  existing data). Try several Xs.
- Stronger variants: "the function is performed with no system at all" or "the need for the
  function disappears."
- The IFR is a direction finder. A solution that is 80% of the way to the IFR with no added
  parts beats a full solution that adds a new subsystem.

**Ideality** = useful functions ÷ (cost + harm + complexity). Every idea should raise it.

## 6. Contradiction formulations

**Administrative contradiction**: "we need X but don't know how" (just the starting point).

**Technical contradiction (TC)**: "If [action/feature], then [A improves], but [B worsens]."
- Always write TC-1 and the inverse TC-2 (the opposite action improves B, worsens A).
- Choose the TC that better serves the main function for further work.

**Physical contradiction (PC)**: "[Element] must be [P] to satisfy [requirement 1] and must
be [not-P] to satisfy [requirement 2]."
- P is a single property of a single element (size, presence, speed, state, visibility,
  ownership, strictness).
- The macro level (the element) and micro level (its parts, particles, fields) can each carry a PC.

## Example of a well-formed chain

Situation: mobile app feels slow because product photos are large.
- TC-1: if we use high-resolution images, quality improves (33 ease of use / 18 visibility)
  but load time worsens (25 loss of time).
- TC-2: if we use low-resolution images, load is fast but users cannot judge products.
- Operating zone: the product card; operating time: first seconds of viewing.
- PC: the image must be large (for detail) and small (for speed).
- Separation in time: tiny placeholder first, full image when the user dwells or zooms.
  Separation by condition: full resolution only on Wi-Fi or on zoom.
