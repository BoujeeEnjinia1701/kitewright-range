---
doc_id: KWR-PRC-001
title: Kitewright Range design precis
project: Kitewright Range
doc_type: Precis
version: "0.5"
status: Draft
date: '2026-10-03'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-09-30'
  author: Amish Chadha
  change: Initial scaffold
- version: "0.2"
  date: '2026-10-03'
  author: Amish Chadha
  change: TRL 2 precis with first-order numbers, components, design choices and safety (KWR-DDR-001)
- version: "0.3"
  date: '2026-10-03'
  author: Amish Chadha
  change: TRL 3 numbers from KWR-CAL-001 v0.2 on the constructable design (KWR-DDR-002)
- version: "0.4"
  date: '2026-10-03'
  author: Amish Chadha
  change: "Round 2 requirement decisions applied (KWR-DDR-003): 22 in propellers on 5215-class motors, 5.0 Ah cells; figures from KWR-CAL-001 v0.3"
- version: "0.5"
  date: '2026-10-03'
  author: Amish Chadha
  change: "Figures from KWR-CAL-001 v0.4, with the Core power leads in the harness (Kitewright Core decision 17 B)"
---

# Kitewright Range design precis

An all-electric quadplane frame for the Kitewright family that takes off vertically and cruises on a fixed wing for long surveys.

## Summary

Kitewright Range is a 2.5 m span quadplane of 11.1 kg that lifts off on four fixed 22 in rotors, flies its survey on the wing and lands vertically again. On paper it hovers at 5,000 m with a 51.7 % thrust margin and flies 32.9 min and 44.4 km on the wing with a 1 kg payload and a 20 % reserve. It is built from hot-wire cut foam and glass, lite-ply, carbon tubes and printed parts with hobby tools, and costs an estimated USD 4,285 against a USD 5,000 value-engineering target. Amish decided the four round 2 requirement decisions on 2026-10-03 (KWR-DDR-003). Endurance (R2) and take-off mass (R7) still miss their targets; the remaining endurance shortfall is an open decision for Amish (`docs/06-design-decisions.md`).

## How it works

A two-piece wing on a carbon joiner sits at the shoulder of a lite-ply fuselage. Under each wing a printed pylon holds a carbon boom with one lift motor 531 mm ahead of the centre of gravity and one 531 mm behind it, so the four rotors lift through the balance point; their discs run 78 mm below the wing-top plane. A tractor motor with a folding propeller at the nose drives the aircraft in cruise, and a conventional tail on a carbon boom steers it. The aircraft rises on the rotors, accelerates on the cruise motor to about 22 m/s, stops the rotors with their blades parked fore and aft, and flies a planned survey; then it slows, hovers and lands on four faired legs. Two ColdCell packs sit either side of the wing joiner on the Kitewright Core power bus, the Core avionics sit in the front bay and the payload hangs on the Core mount under the centre of gravity. The flight code is stock PX4 quadplane firmware with published parameters (KWR-DDR-001, D1).

## Main components

Table 1. Components (numbers are BOM lines)

| # | Component | Made from, or bought | Role |
| --- | --- | --- | --- |
| 1, 2 | Fuselage box and hatch | Lite-ply and birch ply, glass outside | Carries the wing, packs, avionics, payload mount and tail |
| 3 | Nose cone and cruise motor mount | Printed ASA | Fairs the nose and holds the cruise motor on the thrust line |
| 4, 14, 15 | Tail boom socket, tail boom, tail mount | Printed ASA, carbon tube | Carries the tail 1 m behind the wing |
| 5, 6, 7, 8 | Wing panels with ailerons, spars, joiner, wing bolts | XPS foam and glass, carbon tubes, nylon bolts | Lift in cruise; panels come off for transport |
| 9, 10, 11, 12 | Boom pylons, pylon bolts, clamp caps, lift booms | Printed ASA, steel bolts, carbon tube | Hold the lift motors below the wing |
| 13 | Landing legs | Carbon rod, printed clamp and fairing, rubber foot | Stand the aircraft on rough ground |
| 16, 17 | Stabiliser with elevator, fin with rudder | XPS foam and glass | Pitch and yaw stability and control |
| 18 to 21 | Motor mounts, ESCs, 5215-class lift motors, 22 in propellers | Bought | Vertical take-off, hover and landing |
| 22, 23 | Cruise motor and ESC, 14 in folding propeller | Bought | Wing-borne flight |
| 24, 25 | Servos, heated pitot and airspeed sensor | Bought | Control surfaces; airspeed in cold and icing |
| 26, 27 | Kitewright Core avionics and payload mount | From the Kitewright Core | Autopilot, GNSS, radios, payload interface |
| 28 | ColdCell packs, two | From the ColdCell design | 648 Wh of heated Li-ion energy (5.0 Ah cells) |

## Numbers from the TRL 3 calculations

Table 2. Key figures (KWR-CAL-001 v0.4)

| Quantity | Value |
| --- | --- |
| Span, wing area, aspect ratio | 2.50 m, 0.704 m2, 8.9 |
| Take-off mass with 1 kg payload | 11.09 kg |
| Centre of gravity | 28.4 % of the 281 mm mean chord |
| Hover power and thrust margin at 5,000 m | 1,772 W; 51.7 % |
| Stall and cruise speed at 5,000 m | 18.0 m/s; 22.5 m/s |
| Lift-to-drag ratio in cruise | 7.4 |
| Cruise power from the packs | 634 W |
| Energy for cruise after hover, climb and reserve | 348 Wh |
| Endurance and range on the wing | 32.9 min; 44.4 km |
| Lowest structural safety factor | 2.8 (wing spar at 2.5 g) |
| Longest part for transport | 1,205 mm |
| Estimated cost | USD 4,285; value-engineering target USD 5,000 (USD 715 under) |

Assumptions are stated in KWR-CAL-001, Table 1. The most important are the maker-class thrust of the lift motors (68.7 N each at sea level for a 5215-class motor with a 22 in propeller, scaled by density) and a zero-lift drag coefficient of 0.079.

## Key design choices

All are decided under Amish's 2026-10-03 pre-approval and argued in KWR-DDR-001 and KWR-DDR-002, with the round 2 requirement decisions Amish made on 2026-10-03 in KWR-DDR-003:

- PX4 quadplane firmware, as the Kitewright Core (D1).
- Two-piece 2.5 m wing on a joiner, sized to the 1.3 m transport case (D2, C6).
- One set of lift propellers for every altitude band (D3): 22 in propellers on 5215-class motors (KWR-DDR-003, O1-B).
- Tractor cruise motor at the nose with a folding propeller, conventional tail on a tail boom (D5, C1, C5).
- Lift booms on printed pylons 90 mm below the wing, motors centred on the centre of gravity (C2 to C4).
- Two ColdCell 6S3P Li-ion packs of 5.0 Ah high-rate 21700 cells either side of the joiner (D6, C7; KWR-DDR-003, O2-A).
- The foam, glass and lite-ply airframe kept for the first prototype, weighed at TRL 4 (KWR-DDR-003, O4-A).
- Foam, glass, lite-ply, carbon tube and printed parts: buildable with hobby tools (D7).
- Staged powered tests, tie-downs and conservative failsafes (D9, D10).

## Patent design-arounds

From the preliminary patent, trademark and prior-art screen (not legal advice):

- All-electric, single fixed wing, fixed lift and cruise motors (no tilting thrust), to stay clear of US10343774B2 (tilting thrust, to about 2037).
- Lift booms on pylons below the wing with the rotor discs 78 mm below the wing-top plane, to stay clear of US9120560B1 (rotors even with the wing top surfaces, to 2033). The model checks this on every run.
- Layout kept distinct from US9242738B2 (Wisk, to about 2032); claims still to be read by an attorney before any sale.
- Not a tail-sitter, keeping clear of the Airbound tail-sitter noted in the family screen.

## Relationship to other lab projects

- Kitewright Core: autopilot, radios, GNSS mast, payload mount and power bus, used unchanged. Envelopes and interfaces assumed here are listed in `docs/REVIEW.md`.
- ColdCell: the two heated packs. Kitewright Lift shares the 6S bus.
- AltiRig: measures the lift motor and propeller thrust at 5,000 m density before any flight.
- LakeWatch: the first payload, within 1 kg on the Core mount.

## Safety

> **Safety:** Kitewright Range is published as an open engineering reference, not certified aviation equipment, for civilian use only. Certification under FAA Part 107, EASA rules or India's Drone Rules 2021 is out of scope at this TRL and will be addressed if prototypes progress.
>
> **Propellers.** Four 22 in lift propellers and a 14 in cruise propeller can cause serious injury. The lift propellers are fitted only at the build plan's propeller safety stop, never on the bench; a removable arming plug and a lockable arming switch keep the motors dead while anyone handles the aircraft; first hovers are tied down to ground anchors inside a 15 m keep-out zone (KWR-DDR-001, D9).
>
> **Lithium-ion packs.** Two packs hold about 650 Wh. Charge only between 0 and 45 °C pack temperature, in a fire-resistant box, never unattended; treat any pack from a crash as damaged and isolate it outdoors.
>
> **Loss of link or power in remote terrain.** Return to launch on the wing and land vertically; land in place at the reserve; fly inside a geofence (D10). Fly only where local rules allow, away from people, aircraft and wildlife; high-altitude sites may lie in restricted border or protected areas.
>
> **Structure.** The wing spar has the smallest margin (2.8 at 2.5 g). Proof-load the wing before the first flight (TRL 4).

## Open questions

None in this precis. Requirements still not met are open decisions for Amish in the design decisions register (`docs/06-design-decisions.md`).
