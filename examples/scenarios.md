# Where the skill helps: scenarios

Each scenario shows the conflict, a prompt you could send, and the kind of directions TRIZ
opens. The directions are illustrations; the skill generates ideas for your actual situation.

---

## 1. Hardware: battery life vs weight
**Conflict:** a bigger battery gives a delivery drone more flight time but adds weight, which
eats the extra flight time.
**Prompt:** "Our drone needs 40% longer flights, but every extra battery cell adds weight that cancels the gain. Ideas?"
**Matrix:** improving 15 (duration of action) vs worsening 1 (weight of moving object).
**Matrix cell:** 19 Periodic action, 5 Merging, 34 Discarding and recovering, 31 Porous materials.
**Directions:** short top-up charges at perches along the route instead of one big battery
(periodic action); make the battery part of the load-bearing frame so it replaces structural
weight (merging); drop an empty auxiliary cell at the delivery point (discarding); a porous,
lighter frame structure (porous materials); and from resources: use the parcel's own
packaging as a lifting surface.

## 2. Software: speed vs reliability of a release pipeline
**Conflict:** the full test suite protects quality but takes 40 minutes; developers need feedback in 5.
**Prompt:** "CI takes 40 minutes. Cutting tests is not an option. How do we get feedback in 5?"
**Directions:** run only tests affected by the change first, the rest after merge (separation
in time and by condition); split the suite across parallel ephemeral runners (segmentation,
cheap short-living objects); keep a precomputed test-impact map (preliminary action).

## 3. Product: lead qualification vs signup conversion
**Conflict:** more signup fields qualify leads better but reduce conversion.
**Prompt:** "Sales wants company size and role at signup. Growth says every field costs 10% conversion."
**Directions:** see `worked-example.md`.

## 4. Security vs convenience
**Conflict:** strong authentication protects accounts but adds friction for every login.
**Prompt:** "We need stronger auth for a banking app, but users hate extra steps. Use TRIZ."
**Directions:** ask for a second factor only when risk signals appear (separation by
condition); verify continuously in the background using signals the device already has
(resources, mechanics substitution); make the trusted device itself the factor (IFR: "the
phone itself proves it's the user").

## 5. Pricing: generous free tier vs paid conversion
**Conflict:** a generous free tier drives adoption but removes the reason to pay.
**Prompt:** "Our free plan is too good, nobody upgrades. If we cut it, signups drop."
**Directions:** keep everything free for individuals, charge where value is collective (whole
vs parts: individual free, team paid); make limits grow with usage success (dynamics,
feedback); let free users pay with something other than money (contribution, referrals).

## 6. Operations: hot food vs crispy food in delivery
**Conflict:** packaging must be closed to keep food hot and open so steam escapes and fries stay crisp.
**Prompt:** "Our fries arrive soggy. If we vent the box, they arrive cold."
**Physical contradiction:** the box must be closed (heat) and open (steam).
**Directions:** vents that let vapor out but keep heat in (separation by condition: porous or
one-way materials); separate compartments (separation in space); finish crisping at
the customer's end (separation in time).

## 7. Machine learning: accuracy vs inference cost
**Conflict:** a larger model is more accurate but too expensive per request.
**Prompt:** "The large model is 8 points more accurate but costs 12x. We can't afford it for all traffic."
**Directions:** route only hard cases to the large model (separation by condition, cascade);
precompute answers for frequent queries (preliminary action); distill the large model into a
small one (copying); let user corrections improve the small model (feedback, self-service).

## 8. Teams: deep focus vs fast alignment
**Conflict:** frequent meetings keep the team aligned but destroy focus time.
**Prompt:** "Our engineers complain about meetings, but when we cut them, teams drift apart."
**Directions:** synchronous time only on fixed days (separation in time, periodic action);
alignment that happens through artifacts people already produce (resources, IFR: "the work
itself keeps people aligned"); a rotating person who absorbs coordination (intermediary).

## 9. Personalization vs privacy
**Conflict:** personalization needs data; users and regulators want less data collected.
**Prompt:** "We want better recommendations without collecting more personal data."
**Directions:** compute on the device and send nothing (taking out, separation in space);
personalize by context of the current session rather than identity (separation by condition);
let users choose and see what is used (feedback, color changes: make it visible).

## 10. Forecasting: what comes next for a product
**Prompt:** "Where are e-bike locks heading over the next 5 years? Use TRIZ evolution trends."
**What the skill does:** places the product on its S-curve, walks the relevant trends
(dynamism, fields, supersystem, less human involvement) to the next stages, and names the
contradiction that blocks each step.

---

## When the skill should stay out
- "This function throws a null pointer when the field is missing." → ordinary debugging.
- "Which is better for our use case, Postgres or MySQL?" → a comparison question, no contradiction.
- "Write a tagline for our café." → taste, not a contradiction.
In these cases the skill's gate tells Claude to help directly without TRIZ.
