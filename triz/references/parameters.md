# The 39 parameters and how to translate them

The classical matrix speaks engineering. To use it for software, product or business problems,
translate the real conflict into the parameter whose *role* is closest, not whose name sounds
similar. When two parameters fit, try both and compare the principles you get.

"Moving" objects are ones that change position or state during operation (or, by analogy,
things that are transmitted, travel or are processed). "Stationary" objects stay in place
(infrastructure, data at rest, fixed assets).

| # | Parameter | Meaning | Software / data | Product / business / process |
|---|---|---|---|---|
| 1 | Weight of moving object | Mass of something that moves | Payload size, bundle size, message size | Burden carried by a customer or employee through a flow |
| 2 | Weight of stationary object | Mass of something fixed | Storage footprint, dataset size | Fixed assets, overhead, headcount |
| 3 | Length of moving object | Linear size of a moving thing | Length of a code path or call chain | Length of a customer journey |
| 4 | Length of stationary object | Linear size of a fixed thing | Depth of a hierarchy, number of layers | Length of an org chain, approval chain |
| 5 | Area of moving object | Surface of a moving thing | Surface of an API that is transmitted | Contact surface with the customer |
| 6 | Area of stationary object | Surface of a fixed thing | Screen real estate, attack surface | Retail footprint, market coverage |
| 7 | Volume of moving object | Space taken by a moving thing | Memory use at runtime | Inventory in transit, work in progress |
| 8 | Volume of stationary object | Space taken by a fixed thing | Disk and database size | Warehouse stock, office space |
| 9 | Speed | Rate of motion or process | Latency, throughput per request | Time to market, speed of response |
| 10 | Force | Interaction that changes state | Load applied, pressure on a service | Sales push, marketing pressure, leverage |
| 11 | Stress or pressure | Force per unit area | Load per instance, rate per user | Workload per employee, pressure on a team |
| 12 | Shape | External contours, structure | Data schema, API shape, UI layout | Product form factor, org structure |
| 13 | Stability of the object's composition | Integrity, resistance to decay | Data integrity, consistency, schema stability | Brand consistency, team stability, process discipline |
| 14 | Strength | Resistance to breaking under force | Robustness under load, security strength | Resilience of a business model, contract strength |
| 15 | Duration of action of moving object | How long a moving thing works | Session length, battery life, job runtime | Customer lifetime, campaign duration |
| 16 | Duration of action of stationary object | How long a fixed thing works | Uptime of infrastructure, data retention | Longevity of assets, contract term |
| 17 | Temperature | Thermal state | Hot vs cold data, system load "heat" | Urgency, emotional intensity, market "heat" |
| 18 | Illumination intensity | Brightness, light | Visibility, observability | Brand visibility, awareness |
| 19 | Use of energy by moving object | Energy consumed by a moving thing | CPU/energy per request, client battery | Effort per transaction, customer effort |
| 20 | Use of energy by stationary object | Energy consumed by a fixed thing | Idle infrastructure cost | Fixed operating cost |
| 21 | Power | Work per unit of time | Compute capacity | Team capacity, production capacity |
| 22 | Loss of energy | Energy wasted | Wasted compute, inefficient queries | Wasted effort, rework, meetings |
| 23 | Loss of substance | Material lost | Data loss, dropped messages | Lost inventory, churned customers, lost leads |
| 24 | Loss of information | Data or knowledge lost | Lost logs, missing context | Lost knowledge when people leave, poor handoffs |
| 25 | Loss of time | Time wasted | Waiting time, blocked threads | Delays, queues, waiting for approval |
| 26 | Quantity of substance | Amount of material | Number of records, cache entries | Inventory quantity, number of SKUs, users |
| 27 | Reliability | Ability to perform without failure | Availability, error rate | Delivery predictability, service quality |
| 28 | Measurement accuracy | Closeness of measured value to real | Accuracy of metrics, model accuracy | Forecast accuracy, attribution accuracy |
| 29 | Manufacturing precision | Accuracy of producing to spec | Correctness of implementation, build reproducibility | Execution quality, conformance to standards |
| 30 | External harm affects the object | Damage from outside | Attacks, bad input, dependency failures | Competition, regulation, market shocks |
| 31 | Object-generated harmful factors | Harm the object produces itself | Side effects, noisy neighbors, tech debt | Negative externalities, employee burnout, spam |
| 32 | Ease of manufacture | Simplicity of production | Ease of building and deploying | Ease of producing, sourcing, fulfilling |
| 33 | Ease of operation | Simplicity of use | Usability, developer experience | Customer ease of use, onboarding effort |
| 34 | Ease of repair | Simplicity of fixing | Debuggability, mean time to recovery | Ease of support, returns, corrections |
| 35 | Adaptability or versatility | Ability to work in varied conditions | Configurability, extensibility, portability | Flexibility of offer, fit for many segments |
| 36 | Device complexity | Number and diversity of elements | Codebase complexity, number of services | Org complexity, product line complexity |
| 37 | Difficulty of detecting and measuring | How hard it is to observe | Observability gaps, hard-to-test behavior | Hard-to-measure outcomes, opaque processes |
| 38 | Extent of automation | Share of work done without humans | Automation, CI/CD coverage | Self-serve share, process automation |
| 39 | Productivity | Useful output per unit of time or cost | Throughput, developer productivity | Revenue per employee, output per period |

## Tips

- Name the parameter that *improves* first, from the user's goal. The *worsening* parameter is
  the price they are unwilling to pay.
- "Cost" has no parameter of its own. Map it to what drives it: 22 or 20 (energy/running cost),
  23 (material), 25 (time), 32 (production effort), 36 (complexity).
- "User experience" usually maps to 33. "Quality" splits into 27 (does it fail?), 29 (made to
  spec?) or 13 (does it stay consistent?).
- "Security" usually maps to 30 (attacks from outside) and 14 (resistance), sometimes 31.
- Run `python scripts/matrix.py --find <keyword>` to search parameter names.
