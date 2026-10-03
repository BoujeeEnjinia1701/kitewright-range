---
doc_id: KWR-DDR-001
title: Kitewright Range TRL 2 review decisions
project: Kitewright Range
doc_type: Design decision record
version: "0.1"
status: Draft
date: '2026-10-03'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-03'
  author: Amish Chadha
  change: TRL 2 review decisions D1 to D10, decided under Amish's 2026-10-03 pre-approval
---

# 0001: TRL 2 review decisions

- **Date:** 2026-10-03
- **Status:** accepted under Amish's pre-approval. Amish, 2026-10-03: "start with the first 14 repos from the list of 29 projects. I pre-approve the batch runs along with any recommendations you come up with. I also accept any cost overruns or variations from the assumed scope cost." and, for this batch, "Proceed with the remaining 15 scaffolds".

## Context

The scaffold (KWR-PRB-001 v0.1) left five open questions: the reference firmware, the wing span and aspect ratio, one or two propeller sets, whether 1 kg of payload is enough for LakeWatch with its winch, and the first co-design partner. Populating the concept to TRL 2 needed further choices on layout, battery, materials and safety. Each was decided as recommended under the pre-approval above. Requirements that the design does not meet are not decided here; they are open decisions for Amish in `docs/06-design-decisions.md`.

## Options considered and decisions

Table 1. Decisions

| # | Question | Options considered | Decision | Reason |
| --- | --- | --- | --- | --- |
| D1 | Reference firmware | PX4; ArduPilot | PX4 quadplane (VTOL standard) with published parameters; an ArduPilot QuadPlane set may follow | Kitewright Core targets upstream PX4 with no source changes |
| D2 | Wing span and aspect ratio | 2.2 m one piece; 2.5 m in two panels; 3.0 m in three panels | 2.50 m in two 1.18 m panels on a carbon joiner, NACA 2412, root chord 310 mm, tip 250 mm, aspect ratio 8.9 | Largest span whose panels fit a 1.3 m case (R8) with one joint |
| D3 | One or two propeller sets | One set; a low-altitude and a high-altitude set | One set of 20 x 6.5 in propellers for all altitude bands | At sea level they hover at 46 % of maximum thrust, which is efficient enough; one set avoids a wrong-set crash |
| D4 | LakeWatch sampling winch | On Range; on Lift only | 1 kg payload on the Core mount for Range; the sampling winch belongs on Kitewright Lift | A winch needs a hover over one point, which is Lift's job |
| D5 | Layout of the cruise motor and tail | Pusher at the tail with a twin-boom tail; tractor at the nose with a tail boom | Tractor cruise motor with a folding propeller at the nose; conventional tail on a carbon tail boom; lift booms on pylons below the wing | Keeps the lift booms short enough for the cases and the rear rotor wash off the tail |
| D6 | Battery | One or two ColdCell packs; Li-ion or LiPo | Two ColdCell 6S3P Li-ion 21700 packs in parallel, one either side of the wing joiner | Li-ion gives the most energy per kilogram for cruise; two packs share hover current |
| D7 | Materials | Moulded composite; foam, glass, lite-ply and printed parts | Hot-wire cut foam with glass skins, lite-ply fuselage, carbon tubes, printed ASA fittings | Buildable with hobby tools (R10) and repairable in the field |
| D8 | First co-design partner and region | State disaster authority; university glaciology group; mountain NGO | First candidate to approach: the Sikkim State Disaster Management Authority, for lake sites in Sikkim, India; second candidate: a university glaciology group already flying Himalayan lake surveys. Not agreed with either | Sikkim has the high-risk lakes and the 2023 South Lhonak outburst; the authority holds the sites and permissions |
| D9 | Safety approach for powered tests (conservative) | Free hover from the first power-up; staged tests | Staged: motors run with propellers off first; first hovers tied down to ground anchors inside a 15 m keep-out zone; a removable arming plug and a lockable arming switch; no propeller fitted on the bench; packs charged only between 0 and 45 °C pack temperature in a fire-resistant box. Relax the tie-down only after 10 logged tied hovers with no fault, and the keep-out only with the partner's site rules | Large propellers and lithium packs are the main hazards (see safety section) |
| D10 | Failsafes (conservative) | Return and land; land in place | Loss of link or low battery: return to launch on the wing, then land vertically; land in place if the battery reaches the reserve; geofence around the survey area | Remote terrain makes a controlled return safer than an uncontrolled landing |

## Consequences

- The constructable design (KWR-DDR-002) and the calculations (KWR-CAL-001) follow D1 to D10.
- D3 is to be confirmed by AltiRig thrust data at 5,000 m density; D6 depends on the ColdCell format, listed as a cross-repo assumption in `docs/REVIEW.md`.
- D8 records candidates only; no partner has been contacted.
