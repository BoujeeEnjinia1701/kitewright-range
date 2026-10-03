---
doc_id: KWR-DDR-002
title: Kitewright Range design for construction
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
  change: Changes that make the concept buildable, with the reason for each; decided under Amish's 2026-10-03 pre-approval
---

# 0002: Design for construction

- **Date:** 2026-10-03
- **Status:** accepted under Amish's pre-approval. Amish, 2026-10-03: "start with the first 14 repos from the list of 29 projects. I pre-approve the batch runs along with any recommendations you come up with. I also accept any cost overruns or variations from the assumed scope cost." and "Proceed with the remaining 15 scaffolds".

## Context

The scaffold precis (KWR-PRC-001 v0.1) described the quadplane in words: a wing in removable halves, a fuselage pod, two booms under the wing carrying the lift motors and the tail, and a pusher or tractor cruise motor. It did not say how the booms hold on, where the motors sit relative to the centre of gravity and the propeller discs, how the wing comes apart, where the packs go or what the aircraft stands on. Writing the build plan (STANDARDS section 18, Amish 2026-09-30: "fix the design assumptions to match and be physically feasible") settled each of these in `cad/src/model.py`.

The changes keep what the concept does: an all-electric quadplane with one fixed wing, four fixed lift motors with their discs clear of the wing-top plane, one electric cruise motor, the Kitewright Core and its payload mount, and ColdCell packs. Nothing here changes the pitch, the patent design-arounds or the safety case. The model now runs constructability checks with build123d (`python cad/src/model.py`): 72 solids in 48 parts, no two overlapping, none floating, rotor discs at least 70 mm below the wing-top plane, the lift and cruise discs apart, and every part shorter than the 1.3 m case. All pass.

## Decision

Table 1. Changes made to the model, the BOM and the calculations

| # | The concept had | The constructable design has | Why |
| --- | --- | --- | --- |
| C1 | Tail carried on the lift booms | A conventional tail on a 20 mm carbon tail boom from the back of the fuselage | Booms that also reach the tail would be about 1.6 m long and miss the 1.3 m case; the rear rotor wash stays off the tail |
| C2 | Booms "below the wing", no fixing shown | A printed pylon under each wing at 470 mm out, through-bolted with two M5 bolts to plywood hardpoints, the boom held in its saddle by two clamp caps | Gives a bolted, removable boom joint and puts the rotor discs 81 mm below the wing-top plane (design-around R9) |
| C3 | Boom spacing not set | Booms 470 mm either side of the centre line | Keeps the front lift discs 38 mm clear of the cruise propeller disc |
| C4 | Motor positions not set | Lift motors 506 mm ahead of and behind the centre of gravity on each boom | Hover thrust acts through the centre of gravity; the front discs clear the leading edge by 171 mm and the rear discs the trailing edge by 44 mm |
| C5 | Pusher or tractor cruise motor | Tractor at the nose on a printed nose cone, 14 in folding propeller | Nothing behind the fuselage for a pusher to clear; the blades fold back when stopped for landing |
| C6 | Removable wing halves | Two panels on a 20 x 16 mm carbon joiner through the fuselage sides, 6 mm plywood doublers, one nylon M5 wing bolt into each root rib; spar straight at 30 % chord | A straight spar can be a stock tube; the joiner and bolt are the usual field-proven fixing |
| C7 | Fuselage pod, contents not placed | Lite-ply box with a firewall, two bulkheads and a rear wall; Core avionics in the front bay; one ColdCell pack either side of the joiner | Each pack lifts straight out through the hatch with the wing fitted; the packs and payload sit on the centre of gravity |
| C8 | No landing gear | Four landing legs on the booms, 70 mm inboard of the motors: carbon rods in printed fairings with rubber feet | The aircraft stands level on rough ground with 83 mm under the payload; fairings cut leg drag by about four fifths |
| C9 | Wiring not shown | A 10 mm conduit in each wing from the pylon to the root rib, root plugs for each boom, ESCs strapped under the booms | The boom power runs inside the wing and disconnects with it |
| C10 | Payload mount position not set | Core payload mount on four M4 inserts in the floor, centred on the centre of gravity | Fitting or removing the payload does not move the balance (R4) |
| C11 | Tail joint not shown | A printed socket glued inside the rear wall with a split clamp; a printed tail mount that the stabiliser and fin bond to | Tail comes off for transport with one bolt |
| C12 | No hatch | Lite-ply hatch with a front tongue, a rear thumb screw, the GNSS mast and the lockable arming switch | Access to the packs and avionics without tools |
| C13 | Pitot position not set | Heated pitot set into the left wing leading edge, 800 mm out | Clean air outside the propeller wash |

## Consequences

- Take-off mass rose to 10.58 kg once every made part was weighed from the model (KWR-CAL-001 v0.2). R2 and R7 are not met and R1 and R3 are at risk; they are open decisions for Amish, not changed here.
- STEP and STL, the general arrangement (KWR-DWG-001 Rev P2), the concept media and the build plan pictures are regenerated from the changed model.
- The BOM gained the pylons, clamp caps, pylon bolts, landing legs, tail socket, tail mount, wing bolts, transport cases and arming switch.
