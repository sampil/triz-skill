# The 40 inventive principles

Each principle lists its typical moves, then examples from different domains. The examples
are prompts for analogy, not answers: translate the move into the user's system.

Legend: **T** technology/physical, **S** software/data, **B** product, business, process, people.

---

### 1. Segmentation
Divide an object into independent parts; make it easy to take apart; increase the degree of
fragmentation (down to particles, cells, micro-units).
- T: sectional furniture; modular pipelines; powder instead of a solid block.
- S: microservices; sharding; chunked uploads; feature flags per user segment.
- B: tiered pricing; splitting a big launch into small releases; micro-courses instead of a course.

### 2. Taking out (extraction)
Separate the interfering part or property from the object, or extract only the needed part.
- T: noisy compressor placed outside the building; using only the sound of a barking dog as a deterrent.
- S: move heavy computation out of the request path to a worker; extract a config from code.
- B: outsource a non-core function; sell only the valuable component (data, API) separately.

### 3. Local quality
Make the structure non-uniform; let each part work under the conditions that suit it best;
give different parts different functions.
- T: hardened cutting edge on a soft tool body; pencil with an eraser.
- S: hot/cold storage tiers; different caching policies per endpoint; per-region config.
- B: different onboarding for different user types; premium lane at the counter.

### 4. Asymmetry
Replace a symmetric form or arrangement with an asymmetric one; increase asymmetry if it already exists.
- T: asymmetric connector that fits only one way; asymmetric tire tread.
- S: read replicas vs a single writer; asymmetric timeouts for upstream and downstream.
- B: unequal pricing for buyers and sellers in a two-sided market.

### 5. Merging (consolidation)
Join identical or related objects or operations in space or in time; make them work in parallel.
- T: multi-blade razor; combine harvester.
- S: request batching; merging small writes; one pipeline for build, test and deploy.
- B: bundles; combining sales and support calls; shared services across teams.

### 6. Universality
Make one object perform several functions, removing the need for others.
- T: sofa bed; child car seat that converts into a stroller.
- S: one component used in web and mobile; a single command that also installs dependencies.
- B: a role that both sells and onboards; packaging that is also the display stand.

### 7. Nested doll (matryoshka)
Place one object inside another; pass one object through a cavity of another.
- T: telescopic antenna; nested measuring cups.
- S: containers inside VMs; nested transactions; progressive disclosure in a UI.
- B: product inside a product (marketplace inside an app); a pilot nested inside an existing contract.

### 8. Anti-weight
Compensate an object's weight (or any burden) by joining it with something that provides lift,
or by interaction with the environment (aerodynamic, hydrodynamic, buoyancy, magnetic forces).
- T: hydrofoils; helium balloon lifting a banner.
- S: offload load to the client or CDN; let community content carry part of the support load.
- B: offset a costly feature with a partner who pays for it; sponsorship.

### 9. Preliminary anti-action
If an action will have harmful side effects, counteract them in advance; pre-stress the object
against a known future load.
- T: pre-stressed concrete; protective masking before painting.
- S: rate limits and circuit breakers before launch; pre-scaling before a known spike.
- B: setting expectations before a price change; pre-briefing stakeholders before bad news.

### 10. Preliminary action
Perform the required change (fully or partly) in advance; arrange objects beforehand so they
can act from the most convenient place without losing time.
- T: pre-glued wallpaper; perforated sheets that tear easily.
- S: precomputed indexes and materialized views; prefetching; warm pools.
- B: pre-filled forms; meal kits; pre-approved templates for contracts.

### 11. Beforehand cushioning
Compensate for the low reliability of an object with emergency measures prepared in advance.
- T: parachute; fuse; airbag.
- S: backups; feature kill switches; graceful degradation; retries with fallbacks.
- B: insurance; a backup supplier; escrow.

### 12. Equipotentiality
Change working conditions so that the object need not be raised or lowered (remove the need to
fight a potential difference: height, pressure, level of effort).
- T: car service pit so cars need not be lifted; locks on a canal.
- S: same environment in dev and prod; schema-compatible versions so no migration step is needed.
- B: flat handoffs between teams at the same level; self-serve so customers need not escalate.

### 13. The other way round (inversion)
Invert the action; make the movable part fixed and the fixed part movable; turn the object upside down.
- T: treadmill (the road moves, not the runner); cooling the part instead of heating the tool.
- S: push instead of pull; let the server call back instead of polling; inversion of control.
- B: customers come to you instead of sales going to them; reverse auctions; let users set the price.

### 14. Spheroidality (curvature)
Replace straight lines and flat surfaces with curved ones; use rollers, balls, spirals; switch
from linear to rotary motion; use centrifugal forces.
- T: arches and domes; ball bearings; computer mouse ball (historically).
- S: ring buffers; consistent hashing on a ring; carousels instead of long lists.
- B: circular economy loops; rotating roles; cyclic planning.

### 15. Dynamics
Let characteristics of the object or environment change to be optimal at each stage; divide
into parts that can move relative to each other; make a rigid or fixed object movable or adaptive.
- T: adjustable steering column; variable-geometry wing; flexible borescope.
- S: autoscaling; adaptive bitrate; runtime configuration; dynamic pricing.
- B: flexible staffing; plans that adapt to usage; modular offices.

### 16. Partial or excessive action
If 100% of the effect is hard to achieve, do slightly less or slightly more, then correct.
- T: overfill then skim off excess; paint with overspray, then mask.
- S: approximate results first, refine later; over-provision then trim; eventual consistency.
- B: MVP with partial scope; over-recruit for a study knowing some drop out.

### 17. Another dimension
Move into an additional dimension (line → plane → 3D); use multi-story arrangements; tilt or
turn the object; use the other side of a given area.
- T: multi-level parking; spiral staircase; double-sided circuit boards.
- S: add a time dimension (versioning, event sourcing); a second index; layered architecture.
- B: add a new axis of segmentation (time of day, context); use the back of a receipt for a coupon.

### 18. Mechanical vibration
Make the object oscillate; increase frequency (up to ultrasonic); use resonance; replace
mechanical vibrators with piezo; combine ultrasonic and electromagnetic oscillations.
- T: vibrating concrete to remove air bubbles; ultrasonic cleaning.
- S (by analogy): jitter in retries to avoid thundering herds; periodic shake-up of load balancing.
- B (by analogy): short high-frequency feedback loops; rotating small tests instead of one big bet.

### 19. Periodic action
Replace continuous action with periodic or pulsed action; change the frequency; use pauses
between pulses for another action.
- T: pulsed welding; flashing warning lights (more noticeable than steady ones).
- S: batch jobs instead of constant processing; heartbeat intervals; sprints.
- B: seasonal campaigns; office hours instead of always-on availability; periodic billing.

### 20. Continuity of useful action
Carry out the action continuously with all parts working at full load all the time; remove idle
and intermediate motions.
- T: continuous casting; a drill that cuts in both directions of travel.
- S: streaming instead of batch; pipelining; keeping connections warm.
- B: continuous delivery; round-the-clock follow-the-sun support; subscriptions instead of one-off sales.

### 21. Skipping (rushing through)
Conduct a harmful or hazardous process at very high speed so the harm has no time to occur.
- T: flash pasteurization; high-speed cutting of thin plastic tubes so they do not deform.
- S: short-lived credentials; fast-path for small requests; rapid rollback.
- B: rip-the-band-aid reorganizations; short sales windows that limit cannibalization.

### 22. Blessing in disguise (turn harm into benefit)
Use harmful factors (especially from the environment) to obtain a positive effect; remove a
harmful factor by adding it to another harmful factor; amplify it until it stops being harmful.
- T: waste heat used for heating; controlled burn to stop a forest fire.
- S: use error logs as product analytics; chaos engineering (inject failure to gain resilience).
- B: turn complaints into a feature roadmap; sell by-products; publish your failures as content.

### 23. Feedback
Introduce feedback; if it already exists, change its magnitude or influence.
- T: thermostat; automatic gain control.
- S: monitoring with alerts; adaptive rate limiting based on error rates; A/B tests.
- B: NPS loops; usage-based pricing; retrospectives.

### 24. Intermediary
Use an intermediate carrier or process; temporarily join the object with one that is easily removed.
- T: pot holder; a catalyst; a sacrificial layer.
- S: a queue between producer and consumer; an adapter; a proxy; a staging table.
- B: distributors; escrow agents; a translator or broker between two teams.

### 25. Self-service
Make the object serve and repair itself; use waste resources, energy or substances.
- T: self-sharpening teeth of rodents (and blades modeled on them); self-sealing tires.
- S: self-healing systems (auto-restart, auto-remediation); self-documenting APIs.
- B: user communities that answer each other; self-checkout; referral loops where users recruit users.

### 26. Copying
Use a simple, cheap copy instead of an unavailable, expensive or fragile object; replace an
object with its optical image or model; use infrared or ultraviolet copies.
- T: measuring a large object from a photo; flight simulators.
- S: staging environments; mocks and digital twins; read replicas.
- B: demo accounts; prototypes and mockups instead of building; mystery shoppers.

### 27. Cheap short-living objects
Replace an expensive durable object with several cheap ones, sacrificing some properties (e.g. longevity).
- T: disposable syringes; disposable diapers.
- S: ephemeral environments per pull request; throwaway prototypes; spot instances.
- B: short-term contracts; landing-page tests instead of building the product.

### 28. Mechanics substitution
Replace a mechanical means with an optical, acoustic, thermal or electromagnetic one; use fields
to interact with the object; change from static to moving fields, from unstructured to structured ones.
- T: optical sensors instead of mechanical switches; magnetic locks; induction cooking.
- S (by analogy): replace manual or physical steps with signals and events; replace polling with webhooks.
- B (by analogy): replace physical paperwork with digital signatures; replace site visits with remote inspection.

### 29. Pneumatics and hydraulics
Use gas and liquid parts instead of solid ones: inflatable, liquid-filled, air-cushion, hydrostatic, hydro-reactive.
- T: air-cushion packaging; hydraulic jacks; gel insoles.
- S (by analogy): elastic resources that "flow" to where they are needed (serverless, pooled capacity).
- B (by analogy): flexible budgets that move between teams; liquid staffing pools.

### 30. Flexible shells and thin films
Use flexible shells and thin films instead of three-dimensional structures; isolate the object
from its environment with a film.
- T: greenhouse films; protective coatings; tea bags.
- S: thin wrappers and facades; a sandbox layer; a thin client.
- B: a light brand layer over a partner's product (white label); a thin contract covering many deals.

### 31. Porous materials
Make an object porous or add porous elements; if it is already porous, fill the pores with a useful substance.
- T: sintered bearings filled with oil; porous filters.
- S (by analogy): leave intentional slack (buffers, gaps in ID ranges) to absorb change; sparse structures.
- B (by analogy): slack time in schedules; free capacity that absorbs urgent work.

### 32. Color changes
Change the color or transparency of an object or its environment; use colored additives or
luminescent tracers to observe hard-to-see objects or processes.
- T: color-changing thermal indicators; transparent bandages; dye tracers in pipes.
- S: visual diffs; color-coded statuses; tracing IDs through distributed systems.
- B: making hidden processes visible (dashboards, transparent pricing); traffic-light reports.

### 33. Homogeneity
Make interacting objects of the same material (or of material with identical properties).
- T: welding rods of the same metal as the parts; ice containers for ice.
- S: one language or framework across a stack; same data format end to end.
- B: hire from the customer's community; tools that match how the team already works.

### 34. Discarding and recovering
Make parts that have fulfilled their function go away (dissolve, evaporate, be discarded) or
restore consumed parts directly during operation.
- T: dissolving capsules; self-sharpening blades; rocket stages that are dropped.
- S: temporary caches that expire; garbage collection; scaffolding code removed after migration.
- B: temporary task forces that disband; sunset clauses; one-time onboarding steps that disappear.

### 35. Parameter changes
Change the physical state, concentration, density, flexibility, temperature or other parameters.
- T: liquefied gas for transport; concentrated detergents; tempered glass.
- S: change granularity, precision, consistency level or retention period; compress data.
- B: change price point, frequency, contract length, packaging size or audience concentration.

### 36. Phase transitions
Use effects that occur during phase transitions (volume change, heat absorption or release).
- T: ice packs; heat pipes; wax actuators in thermostats.
- S (by analogy): use state transitions as triggers (on-create, on-expire, on-threshold).
- B (by analogy): use transitions in the customer lifecycle (move, wedding, renewal) as moments to act.

### 37. Thermal expansion
Use thermal expansion or contraction of materials; use several materials with different expansion coefficients.
- T: bimetallic strips; shrink-fitting parts.
- S/B (by analogy): use differences in how parts react to the same change to trigger a useful action automatically.

### 38. Strong oxidants (enriched atmosphere)
Replace ordinary air with enriched air, enriched air with oxygen, oxygen with ionized oxygen or ozone.
- T: oxygen-enriched combustion; ozone water treatment.
- S/B (by analogy): concentrate the active ingredient: a focused team, a high-intent audience, a hotter cache.

### 39. Inert atmosphere
Replace the normal environment with an inert one; add neutral parts or inert additives; carry out the process in a vacuum.
- T: argon in welding; nitrogen in food packaging.
- S: isolated sandboxes; read-only modes during migrations; quiet periods without deploys.
- B: neutral third parties; meeting-free days; no-change freeze before a launch.

### 40. Composite materials
Change from uniform to composite (multiple) materials or structures.
- T: fiberglass; carbon fiber; reinforced concrete.
- S: hybrid architectures (edge + cloud, SQL + search index); ensembles of models.
- B: hybrid teams (in-house + contractors); hybrid sales (self-serve + enterprise).

---

## Most frequent principles

Across the classical matrix the principles that appear most often are 35, 10, 1, 28, 2, 18, 15,
19, 32 and 13 (run `python scripts/matrix.py --top` for the exact ranking). When the matrix cell
is empty, or none of its suggestions fit, try these and the separation principles.
