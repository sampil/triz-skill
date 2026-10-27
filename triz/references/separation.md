# Resolving physical contradictions: separation

A physical contradiction says one element must be P and not-P. Separate the two demands so each
holds where or when it is needed. Check whether the demands really overlap: often they do not.

Ask in order:
1. Do both demands hold **at the same time**? If not → separation in time.
2. Do both hold **in the same place**? If not → separation in space.
3. Do both hold **under the same conditions** (for every user, load, input)? If not → separation by condition.
4. Must the **whole system and its parts** have the same property? If not → separation between system levels.
If the answer is "yes" to all four, look for a substance or effect whose state changes on its
own (phase transitions, a material or mechanism that responds to conditions) or reformulate the PC.

## Separation in time
The element is P at one moment and not-P at another.
- Typical principles: 9, 10, 11, 15, 16, 19, 21, 26, 27, 29, 34, 37.
- T: folding bicycle (large while riding, small when stored); airbag (absent until a crash).
- S: lazy loading; schedule heavy jobs at night; credentials valid only during a session.
- B: introductory pricing; seasonal staffing; a feature visible only during onboarding.

## Separation in space
The element is P in one place and not-P in another.
- Typical principles: 1, 2, 3, 4, 7, 13, 14, 17, 24, 26, 30.
- T: bifocal lenses; a tool with a hard edge and a soft grip.
- S: strict validation at the API boundary, permissive inside; data hot in one region, cold elsewhere.
- B: premium shop-in-shop inside a discount store; different rules for different departments.

## Separation by condition
The element is P under one condition and not-P under another (load, user type, input, temperature, direction).
- Typical principles: 1, 5, 6, 7, 8, 13, 14, 22, 23, 25, 27, 33, 35.
- T: a sieve (passes small particles, blocks big ones); a one-way valve; non-Newtonian fluids.
- S: rate limits that apply only to anonymous users; feature flags; adaptive quality by connection.
- B: free tier vs paid tier; strict approval only above a spending threshold.

## Separation between system levels (whole vs parts)
The system as a whole has property P; its parts have not-P (or the supersystem does).
- Typical principles: 1, 5, 6, 12, 22, 25, 27, 33, 40.
- Transition to subsystem: a bicycle chain is flexible as a whole, but each link is rigid.
- Transition to supersystem: one sensor is unreliable, a network of sensors is reliable.
- Transition to the anti-system: combine a system with its opposite (antivirus that uses viruses, red team).
- S: each microservice is simple, the whole is capable; individual nodes fail, the cluster does not.
- B: each team is autonomous, the company is aligned through shared goals.

## After separating
Check that the separation boundary itself is cheap to create and manage. If the boundary
(the switch, the detector, the coordinator) becomes a new complex subsystem, look for a
resource that can serve as the boundary (`resources.md`).
