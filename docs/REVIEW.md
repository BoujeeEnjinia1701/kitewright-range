# Review note: Kitewright Range

## Session 2026-09-30: scaffolded

### What was done

- Repository created from kit 1.6.0 at TRL 1, target TRL 2.
- `docs/01-problem.md` (KWR-PRB-001 v0.1): problem with cited evidence, users, environment, constraints, prior work, open questions.
- `docs/02-concept.md` (KWR-PRC-001 v0.1): how it works, components, patent design-arounds, shared blocks, safety.
- `docs/03-requirements.md` (KWR-REQ-001 v0.1): 10 proposed requirements.
- `README.md` with concept rationale, burning platform, where it could be used, and what sparked the idea.

### Next

- Run `/populate` to bring the repo to a strong TRL 2 with concept media.

## Session 2026-10-03: TRL 2 (populate, under Amish's pre-approval)

Run as the first half of `/to-trl3` on kit 1.7.0, under Amish's 2026-10-03 instructions: "start with the first 14 repos from the list of 29 projects. I pre-approve the batch runs along with any recommendations you come up with. I also accept any cost overruns or variations from the assumed scope cost." and, for Batch 2, "Proceed with the remaining 15 scaffolds".

### What was done

- Kit 1.7.0 installed (`.kit/`, `.claude/commands/`); root `CLAUDE.md` replaced from `.kit/CLAUDE.md`.
- `docs/01-problem.md` (KWR-PRB-001 v0.2): open questions answered, value-engineering wording, co-design candidate, safety note.
- `docs/03-requirements.md` (KWR-REQ-001 v0.2): concept status for each requirement (targets unchanged).
- `docs/02-concept.md` (KWR-PRC-001 v0.2): how it works, components, first-order numbers, design choices, safety.
- `docs/decisions/0001-trl2-review-decisions.md` (KWR-DDR-001): D1 to D10.
- Massing model, concept media and BOM, then carried straight into TRL 3 (below), so the TRL 2 media were superseded by the TRL 3 set in the same session.

### Results at TRL 2

- The TRL 2 concept was carried straight into the TRL 3 calculations in the same session; all figures are the TRL 3 figures below.

### Decisions made under the pre-approval (KWR-DDR-001)

- D1 PX4 quadplane firmware; D2 2.5 m two-piece wing; D3 one 20 in propeller set; D4 the LakeWatch winch belongs on Kitewright Lift; D5 nose tractor and tail boom; D6 two ColdCell 6S3P Li-ion packs; D7 foam, glass, lite-ply and printed build; D8 Sikkim State Disaster Management Authority as the first co-design candidate to approach (not agreed), a university glaciology group second; D9 staged powered tests with tie-downs, keep-out zone, arming plug and lockable switch (conservative; relax the tie-down only after 10 logged tied hovers with no fault); D10 return to launch and land vertically on loss of link or low battery, land in place at the reserve, geofence.

### Safety concerns

- Large propellers, lithium-ion packs and a crash in remote terrain; covered in the precis safety section and D9, D10.

## Session 2026-10-03: TRL 3 (advance, design for construction, build plan)

### What was done

- `docs/04-calcs/01-sizing.md` (KWR-CAL-001 v0.2) with `docs/04-calcs/sizing.py` and `results.csv`: mass and balance from the model, drag build-up, hover at 5,000 m, energy, structure, geometry rules, cost, options for every shortfall, and a results table against every requirement.
- `cad/src/model.py`: parametric build123d model of the constructable design with constructability checks (72 solids in 48 parts: no overlaps, nothing floating, rotor discs at least 70 mm below the wing-top plane, lift and cruise discs apart, every part shorter than a 1.3 m case). STEP in `cad/step/` (assembly, fuselage, right wing panel, right boom pylon, landing leg parts, tail) and STL of the printed parts in `cad/stl/`.
- `cad/src/sheets.py`: general arrangement KWR-DWG-001 at Rev P2 (P1 preliminary GA, P2 design for construction).
- `bom/bom.csv`: 32 lines, every one priced, with a supplier type.
- `cad/src/concept_media.py`: hero, cutaway, exploded view with BOM numbers, blueprint KWR-DWG-010 Rev P2, glTF viewer (`media/model.glb`, about 1 MB, coarse tessellation) and energy flow per flight.
- `docs/decisions/0002-design-for-construction.md` (KWR-DDR-002): changes C1 to C13.
- `cad/src/build_plan_media.py`: overview, 13 making sketches (KWR-DWG-101 to 113), 8 joint close-ups, 16 assembly steps.
- `docs/05-build-plan.md` (KWR-BLD-001), `docs/06-design-decisions.md` (KWR-DEC-001).
- `cad/src/product_model.py` (appearance model, hero, exploded and detail views) and render scenes exported to `/home/claude/renders/kitewright-range/` for the photoreal renders on Amish's Mac.
- `docs/02-concept.md` v0.3 and `docs/03-requirements.md` v0.3 brought to the TRL 3 figures; `project.yaml` at TRL 3, target 3, `design_state: constructable`; README leads with `media/render-hero.png` (made on the Mac) and has the build plan link and "Building the prototype".

### Results (KWR-CAL-001 v0.2)

| Quantity | Value |
| --- | --- |
| Take-off mass with 1 kg payload | 10.58 kg (packs 2.80 kg) |
| Centre of gravity | 28.4 % of the mean chord, unchanged by the payload |
| Hover at 5,000 m | 1,815 W; thrust margin 31.8 % |
| Cruise | 21.9 m/s, L/D 7.5, 585 W |
| Endurance and range on the wing | 31.0 min, 40.9 km with a 20 % reserve |
| Lowest structural safety factor | 2.9, wing spar at 2.5 g |
| Cost | Value-engineering target: USD 5,000. Estimated cost of the constructable design: USD 3,945 (USD 1,055 under the target) |

### Requirements not met or at risk

- R1 hover thrust margin: at risk (31.8 %, on maker-class thrust not yet measured).
- R2 endurance: not met (31.0 min).
- R3 survey range: at risk (40.9 km).
- R7 take-off mass: not met (10.58 kg).
- All others met on paper or by design; R5 depends on cold ratings to confirm when parts are bought.

### Decisions for Amish

Each item is **Proposed, awaiting Amish**, and is listed in `docs/06-design-decisions.md` under Open decisions. Figures are from KWR-CAL-001 v0.2, Table 5; the design stays as it is until Amish decides.

**O1. R1 hover thrust margin.** State: 31.8 % at 10.58 kg and 0.736 kg/m3, against the requirement's margin; cause: it rests on a maker-class 5.8 kgf sea-level thrust scaled by density, with no measured data, so a few percent of thrust shortfall or mass growth erases it.
- A: keep 20 in propellers on 5212-class motors. Margin 31.8 %; no cost or mass change.
- B: 22 in propellers on 5215-class motors. Margin 53.3 %; +USD 160; +0.40 kg; endurance -1.7 min, range -1.7 km; booms 50 mm longer and 20 mm further out to keep the disc clearances.
- C: keep A now and switch to B only if AltiRig measures less than the requirement. No change now; the risk moves to the test.
- **Recommendation: B.** Hover authority at 5,000 m is the aircraft's safety margin in gusts, so the conservative choice applies; the cost is small and combined with O2-A the endurance still improves on today's design.

**O2. R2 endurance.** State: 31.0 min against the requirement; cause: 583 Wh in 2.80 kg of packs drives a 10.6 kg aircraft with a zero-lift drag coefficient of 0.077 (stopped lift motors and an external payload), needing 585 W in cruise.
- A: two 6S3P packs of 5.0 Ah high-rate 21700 cells. 35.6 min; +USD 120; no mass change; hover margin unchanged.
- B: two 6S4P packs. 38.9 min; +USD 190; +0.88 kg; hover margin falls to 21.7 % (R1 then fails).
- C: moulded carbon wing, tail and fuselage with two 6S4P packs. 43.3 min; +USD 1,390; +0.19 kg; margin 29.4 %; USD 5,335 in all.
- **Recommendation: A** for the first prototype; C is the path for a second prototype once the first one's drag and mass are measured.

**O3. R3 survey range.** State: 40.9 km against the requirement, a 2 % margin; cause: range follows endurance at 21.9 m/s.
- A: 5.0 Ah cells as O2-A. 46.8 km; +USD 120; no mass change.
- B: A together with O1-B. 45.0 km; +USD 280; +0.40 kg.
- C: keep as is. 40.9 km; no change.
- **Recommendation: A**, decided together with O2 (B if O1-B is chosen).

**O4. R7 take-off mass.** State: 10.58 kg against the requirement; cause: ColdCell packs 2.80 kg, lift system with mounts 1.32 kg, payload 1.00 kg and Core avionics 0.78 kg leave 4.7 kg for an airframe built with hobby methods.
- A: keep the foam, glass and lite-ply airframe. 10.58 kg; no change.
- B: moulded carbon wing, tail and fuselage. 9.89 kg; +USD 1,200 (USD 5,145 in all, USD 145 over the value-engineering target); endurance +4.1 min.
- C: fly with one pack. 9.18 kg; endurance 15.0 min, which fails R2 and R3 by far.
- **Recommendation: A** for the first prototype, weighed at TRL 4. No option inside the concept reaches the target without giving up endurance; if the target reflects a regulatory class at the first site, that site's rules should set the target before the second prototype.

### Decisions made under the pre-approval

- KWR-DDR-001 D1 to D10 (TRL 2 review) and KWR-DDR-002 C1 to C13 (design for construction), both dated 2026-10-03 and recorded in `docs/06-design-decisions.md` with Amish's words.

### Design changes made for construction (KWR-DDR-002)

- C1 tail on its own carbon tail boom, not on the lift booms.
- C2 lift booms on printed pylons through-bolted under the wing with clamp caps; rotor discs 81 mm below the wing-top plane.
- C3 booms 470 mm out, 38 mm clear of the cruise propeller disc.
- C4 lift motors 506 mm ahead of and behind the centre of gravity.
- C5 tractor cruise motor at the nose on a printed cone, folding propeller.
- C6 two wing panels on a carbon joiner, nylon wing bolts, straight spar at 30 % chord.
- C7 lite-ply fuselage box with packs either side of the joiner and Core avionics in front.
- C8 four faired landing legs.
- C9 wing wiring conduits and root plugs.
- C10 payload mount on the centre of gravity.
- C11 printed tail socket and tail mount.
- C12 hatch with GNSS mast and arming switch.
- C13 heated pitot in the left wing.

### Build plan findings

- The concept's booms could not carry the tail and still fit the 1.3 m case (C1).
- Without a pylon depth rule, the rotor discs would sit near the wing plane the design-around avoids; the model now checks the 70 mm rule on every run.
- The boom spacing first tried (450 mm) put the front lift discs within 18 mm of the cruise propeller disc; 470 mm gives 38 mm.
- Weighing every made part from the model raised the take-off mass from the TRL 2 estimate to 10.58 kg; printed parts are weighed as walls plus infill, and the pylons were shortened to 160 mm to save 0.2 kg.
- The tightest structural margin is the wing spar (2.9 at 2.5 g); the build plan's safety stop 4 requires a proof load before free flight (TRL 4).

### Appearance model (product_model.py)

- Every part comes from `model.py`. The only difference: the lift and cruise propellers are drawn as tapered blades in place of the model's flat blade envelopes of the same diameter. Proposed, awaiting Amish (appearance only).
- The detail view should be rendered with `--focus` on the left front lift motor and pylon.
- Hero framing: the 1.75 m person stands beyond the right wing tip, behind the aircraft as seen from the hero camera, so it never stands between the camera and the product.

### Safety concerns

- Four 20 in lift propellers and a 14 in cruise propeller: fitted only at the propeller safety stop, arming plug and lockable switch, tied first hovers in a 15 m keep-out zone (D9).
- About 580 Wh of Li-ion: charge between 0 and 45 °C pack temperature in a fire-resistant box; crash-damaged packs isolated outdoors.
- Loss of link or power in remote terrain: return on the wing and land vertically, land in place at the reserve, geofence (D10).
- Wing spar margin 2.9 at 2.5 g: proof-load before free flight.
- High-altitude sites may lie in restricted border or protected areas; fly only with the site partner's permissions.

### Cross-repo actions (sibling repos not edited)

Kitewright Core and Kitewright Lift are being done in parallel; these shared-interface assumptions are used here and should be confirmed in those repos:

1. **Kitewright Core, firmware:** PX4 (VTOL standard quadplane) as the family reference, with a Range parameter set at sea level, 3,000 m and 5,000 m.
2. **Kitewright Core, avionics envelope:** 180 x 110 x 60 mm, 0.70 kg, plus a GNSS mast of 0.08 kg through the hatch; USD 900 as Range's share in the BOM.
3. **Kitewright Core, payload mount:** a 160 x 80 x 12 mm plate with a rail, locking pin and DS-014 connector, 0.12 kg, fixed by four M4 bolts; payload envelope 150 x 90 x 100 mm and 1 kg with its centre of gravity under the mount centre; connector lead through the fuselage floor.
4. **Kitewright Core, power:** a 6S bus (21.6 V nominal Li-ion) taking two packs in parallel, carrying about 85 A in hover at 5,000 m (about 42 A per pack); an arming plug in the main lead and a lockable arming switch.
5. **ColdCell:** a 6S3P pack of 4.5 Ah 21700 cells, 291.6 Wh, 1.40 kg, 138 x 75 x 82 mm, XT90 lead, film heater and BMS thermostat holding the cells above 15 °C, 95 % usable at -20 °C ambient once warmed; a 5.0 Ah cell variant is proposed in O2.
6. **Kitewright Lift:** shares the 6S bus voltage, the Core mount and the ColdCell pack format; the LakeWatch sampling winch is assigned to Lift (D4).
7. **AltiRig:** first job is the thrust of a 5212-class motor with a 20 x 6.5 in propeller (and the 5215-class with 22 in, for O1) at 0.736 kg/m3.

### Recommended next step

- Amish decides O1 to O4. Then render the hero, exploded and detail views on the Mac from the exported scenes, make the cards, and run the release gate. The design is ready for TRL 4 parts purchase and AltiRig thrust tests once O1 is settled; that is a recommendation only, not started.

## 2026-10-03: photoreal renders

Rendered with Blender Cycles on Amish's Mac from `cad/src/product_model.py`; captioned with `.kit/photo_caption.py`; `media/card.png` and `media/social-preview.png` made with `.kit/cards.py`. Views: hero, exploded, detail. image_qc passes and `render.py --check` has no FAIL.

## 2026-10-03: Amish's requirement decisions carried out

Amish Chadha, 2026-10-03: "i agree with all the 46 recommendations you provided. please proceed." For Kitewright Range that is 36B (O1, R1), 37A (O2 and O3, R2 and R3) and 38A (O4, R7); with Kitewright Core decision 33B, Range now supplies its own power leads from the frame to the Core. Recorded in `docs/decisions/0003-requirement-decisions.md` (KWR-DDR-003) and `docs/06-design-decisions.md` v0.2.

### Changes made

- **36B, R1:** 5215-class lift motors (about 285 g, 62 mm can, at least 7.0 kgf with 22 x 7 in propellers, USD 150 each) and 22 x 7 in carbon propellers (about 55 g, USD 50 each); motor mount top plate at least 64 mm across. Booms moved from 470 to 490 mm out and motors from 506 to 531 mm either side of the centre of gravity; booms 1,142 mm (were 1,092 mm), cut from 1,200 mm tube (USD 52 each). New result: **hover margin 52.0 %** at 5,000 m (target at least 30 %; met on paper, thrust still to measure in AltiRig).
- **37A, R2 and R3:** 5.0 Ah high-rate 21700 cells in the same two 6S3P ColdCell packs, 324 Wh each, same 1.40 kg (USD 350 each). New results: **endurance 32.9 min** (target 45 min; not met, accepted for the first prototype) and **range 44.3 km** (target 40 km; met on paper).
- **38A, R7:** airframe unchanged. New result: **take-off mass 11.07 kg** (target 8 kg; not met, weighed at TRL 4).
- **Core power leads (Core 33B):** new BOM line 33, four 8 AWG leads with AS150 plugs, soldered to the Core's pads at integration (about 124 g, USD 60, the Core's former BOM line 21); build plan step 4 and the bought-parts table say how.
- The recommended figures were quoted one option at a time (53.3 %; 35.6 min and 46.8 km). Taken together, with the leads (0.12 kg) and the larger motors' drag, they are 52.0 %, 32.9 min and 44.3 km. This is the combination v0.2 listed as R3 option B (45.0 km), less the leads.
- `cad/src/model.py`: three new checks (lift disc at least 50 mm from the fuselage side, 141 mm; at least 50 mm from the stabiliser, 110 mm; motor no wider than the mount plate). All 72 solids in 48 parts pass; discs 77 mm below the wing-top plane (rule 70 mm); lift and cruise discs 33 mm apart (rule 20 mm). STEP and STL regenerated.
- `docs/04-calcs/sizing.py` and `01-sizing.md` (KWR-CAL-001 v0.3), `results.csv`; `docs/03-requirements.md` v0.4 (status only; no requirement restated); `docs/05-build-plan.md` v0.2; `docs/02-concept.md` v0.4 and the README figures brought to v0.3 numbers; `bom/bom.csv`.

### Results (KWR-CAL-001 v0.3)

| Requirement | Before | After | Status |
| --- | --- | --- | --- |
| R1 hover margin (at least 30 %) | 31.8 % | 52.0 % | Met on paper |
| R2 endurance (at least 45 min) | 31.0 min | 32.9 min | Not met (accepted) |
| R3 range (at least 40 km) | 40.9 km | 44.3 km | Met on paper |
| R4 balance | 28.4 % MAC | 27.5 % MAC | Met by design |
| R7 take-off mass (8 kg or less) | 10.58 kg | 11.07 kg | Not met (accepted) |
| R9 discs below wing-top plane | 81 mm | 77 mm | Met by design |
| R10 cost | USD 3,945 | USD 4,293 | Met on paper |

Value-engineering target: USD 5,000. Estimated cost of the constructable design: USD 4,293 (USD 707 under the target). Mass 11.07 kg with the 1 kg payload (0.49 kg more). Lowest structural safety factor 2.8 (wing spar at 2.5 g); lift boom 8.4 with the stronger motors.

### Pictures changed

- General arrangement KWR-DWG-001 Rev P3; concept blueprint KWR-DWG-010 Rev P3; hero, cutaway, exploded, flow and the glTF viewer.
- Build plan: overview, making sketches KWR-DWG-105 (hardpoints at 490 mm), KWR-DWG-106 (pylon), KWR-DWG-108 (boom 1,142 mm) and the other sheets regenerated from the same model, the boom joints (joint-02 to joint-04) and assembly steps 8 to 16.

### Appearance model

- `cad/src/product_model.py` takes the 22 in propellers, larger motors and longer booms from `model.py`; the tapered blades are widened in proportion (46 mm root chord, was 42 mm). Appearance only; still recorded as proposed, awaiting Amish, with the earlier blade note. Render scenes re-exported to `/home/claude/renders/kitewright-range/` (hero, exploded, detail); the photoreal renders on the Mac need redoing to show the larger propellers.

### Open decisions

None. No new question needs Amish.

### Safety

- Larger propellers and stronger motors: fitted only at the propeller safety stop, arming plug out, tied first hovers in the 15 m keep-out zone (D9). Boom bending safety factor at full sea-level thrust is 8.4.
- The 8 AWG Core power leads: 100 W iron, pliers on hot wire, polarity checked with a meter and opposite-gender plugs before any pack is connected.
- Packs: unchanged rules; charge between 0 and 45 °C pack temperature in a fire-resistant box.

### Cross-repo actions (sibling repos not edited)

1. **ColdCell:** the Range pack is now 6S3P of high-rate 5.0 Ah 21700 cells, 324 Wh, same 138 x 75 x 82 mm and 1.40 kg, about 14 A per cell in hover at 5,000 m (USD 350 assumed).
2. **Kitewright Core:** Range supplies the four 8 AWG leads with AS150 plugs (PACK 1, PACK 2, FRAME A, FRAME B); the Core's build plan step 9 and BOM line 21 move to the frames. Core should state the pad positions and grommets the leads pass.
3. **Kitewright Core, mass:** Range carries 0.90 kg for the Core avionics, GNSS mast and payload mount (0.70, 0.08 and 0.12 kg); the Core's own estimate after 33B is about 0.99 kg for the same set. If it holds, Range gains about 0.09 kg: hover margin about 50.8 %, endurance about 0.3 min less; nothing changes status. The Core's deck interface (four M4 on 220 x 130 mm, 200 x 112 mm lid opening) also differs from the 180 x 110 x 60 mm envelope assumed here; to settle when the family interface is frozen.
4. **Pack connector:** Range's ColdCell packs have XT90 leads; the Core's inputs are AS150. Recommend AS150 on the ColdCell packs family-wide so the Range harness needs no adapters.
5. **AltiRig:** the first thrust job is now a 5215-class motor with a 22 x 7 in propeller at 0.736 kg/m3.
6. **Kitewright Lift:** also supplies its own Core power leads under Core 33B; the lead set (8 AWG, four AS150 halves, labels) should match Range's BOM line 33.

### Recommended next step

- Re-render the hero, exploded and detail photoreal views on the Mac from the new scenes, then run the cards and the release gate. The design is ready for TRL 4 parts purchase and AltiRig thrust tests of the 5215-class motor with a 22 in propeller; that is a recommendation only, not started.

## 2026-10-04: Amish's round-3 decisions carried out

Amish Chadha (owner) on 2026-10-04: "For round 3, I agree with all your proposed recommendations". For Kitewright Range that is its share of the Kitewright family reconciliation, item 10A: AS150 plugs everywhere (Range's packs change from XT90), one mounting envelope for the Core shared with Lift with the Core's drawing as the reference, and Range recomputed with the 0.99 kg Core. Core, Lift, ColdCell, AvalancheScout and LakeWatch were brought to the same table in the same session. Recorded in `docs/decisions/0004-family-reconciliation.md` (KWR-DDR-004) and the register (`docs/06-design-decisions.md` v0.3). Nothing was committed or pushed.

### Changes made

- **Model** (`cad/src/model.py`, new `cad/src/core_envelope.py`): the Kitewright Core hung under the floor at the centre of gravity (four M4 on 220 x 130 mm into a new 6 mm birch Core deck doubler, lid up through a 200 x 112 mm floor opening, rail pointing aft); fuselage 156 mm wide (was 140); rear bulkhead at 645 mm (was 585); front pack in the nose bay and rear pack on the doubler behind the lid; payload envelope 140 x 88 x 100 mm on a payload shoe inside the Core's neck. All 75 solids in 49 parts pass the checks (no overlaps, nothing floating, discs 77 mm below the wing-top plane, transport lengths). STEP and STL regenerated.
- **BOM** (`bom/bom.csv`): lines 1, 2, 26, 27, 28 and 29 changed, each with a price basis (wider sheets and doubler USD 6, antenna extension leads USD 15; AS150 at the XT90's price class).
- **Calculations** (`docs/04-calcs/sizing.py`, `01-sizing.md` v0.4, `results.csv`): Core 0.99 kg with its rail and pins, the Core's underside drag, the wider fuselage; every section re-run.
- Documents: `docs/03-requirements.md` v0.5 (status only; no requirement restated), `docs/05-build-plan.md` v0.3, `docs/02-concept.md` v0.5, `README.md`.

### New result per requirement (KWR-CAL-001 v0.4)

| Requirement | Before (v0.3) | Now | Status |
| --- | --- | --- | --- |
| R1 hover margin (at least 30 %) | 52.0 % | 48.3 % | Met on paper |
| R2 endurance (at least 45 min) | 32.9 min | 30.6 min | Not met (accepted) |
| R3 range (at least 40 km) | 44.3 km | 41.5 km | Met on paper, 4 % margin |
| R4 balance | 27.5 % MAC | 28.3 % MAC, payload on the CG | Met by design |
| R7 take-off mass (8 kg or less) | 11.07 kg | 11.35 kg | Not met (accepted) |
| R9 discs below wing-top plane | 77 mm | 77 mm | Met by design |
| R10 cost | USD 4,293 | Value-engineering target: USD 5,000. Estimated cost of the constructable design: USD 4,314 (USD 686 under the target) | Met on paper |

The brief expected about 32.9 min after reconciliation. The 0.99 kg Core's mass alone would cost only about 0.3 to 0.5 min, but carrying the Core to its drawing also costs the doubler, a wider fuselage and the Core's drag under the floor: 30.6 min in all. LakeWatch's R5 is restated on this 30.6 min.

### Kitewright interface table

The same table stands in the review notes of Kitewright Core, Kitewright Lift, Kitewright Range, ColdCell, AvalancheScout and LakeWatch (Amish's decision 10A, 2026-10-04). The Core's drawings are the reference for the mounting envelope.

| Interface | Family figure | Source |
| --- | --- | --- |
| Power connector | AS150 on every pack lead and on each frame's power harness (two pack inputs, two frame outputs, opposite genders); no XT60 or XT90 on the bus | Decision 10A; KWC-DDR-001, D3 |
| Core mounting envelope and hole pattern | Core plate 240 x 150 x 2 mm hung under the frame's lower deck on four 12 mm OD x 8 mm corner spacers; four M4 holes on a 220 x 130 mm pattern; a 200 x 112 mm opening in the deck for the lid; lid 168 x 92 mm, its top 55 mm above the deck's underside (GNSS mast boss 69 mm); where a frame has no 240 mm clear above the lid, the antennas and GNSS receiver go to frame positions on extension cables; rail, pin blocks and pin knobs to 47 mm below the plate top; payload shoe 184 x 128 x 5 mm, payload neck 88 mm wide from the shoe to 30 mm below the rail lips | KWC-DWG-001 Rev P2, KWC-DWG-106 |
| Bus voltage | 18 to 60 V at the Core's pack inputs. Lift: 14S lithium-ion, 42.0 to 58.8 V (50.4 V nominal). Range: 6S lithium-ion, 18.0 to 25.2 V (21.6 V nominal) | KWC-DDR-001, D3 |
| Pack size and mass | Lift: two ColdCell 14S3P lithium-ion packs, 410 x 94 x 94 mm, 4.46 kg and 680 Wh each (CCL-DWG-002). Range: two 6S3P lithium-ion packs of 5.0 Ah cells, 138 x 75 x 82 mm, 1.40 kg and 324 Wh each (Range's figure; ColdCell has not yet drawn this pack) | Decision 8A; CCL-CAL-001 K; KWR-CAL-001 |
| Core mass | 0.99 kg: avionics, radios, GNSS, rail and locking pins; packs, payload shoe and the frame's harness excluded | Core R9; KWC-DDR-003 |

### Pictures changed

General arrangement KWR-DWG-001 Rev P4; making sketches KWR-DWG-101 (fuselage box) and 102 (hatch) Rev P2, the others redrawn unchanged; build plan overview, all eight joints (joint-08 now the battery bays and the Core under the floor) and all sixteen steps (step 4 the doubler, step 5 the Core under the floor); concept media (hero, cutaway, exploded, flow, blueprint, `model.glb`). Looked at: joint-08. `cad/src/product_model.py` takes the Core, its rail and the doubler from `model.py`; render scenes exported to `/home/claude/renders/kitewright-range` (hero, exploded, detail). The photoreal renders, captions and cards in `media/` predate this change and need a re-run on Amish's Mac.

### Open decisions

None. The lower endurance and range keep their status (R2 not met and accepted, R3 met on paper), so nothing new needs Amish.

### Safety

- The Core's pin knobs hang 140 mm and the payload 80 mm above the ground on the landing feet: land only on clear ground, and walk the aircraft round before arming.
- The Core power leads are soldered with every pack disconnected; polarity checked at each AS150 plug with a meter before the first pack goes on.
- Packs: unchanged rules; charge between 0 and 45 °C pack temperature in a fire-resistant box.

### Cross-repo actions

- **ColdCell:** the Range pack (6S3P of 5.0 Ah 21700 cells, 138 x 75 x 82 mm, 1.40 kg, 324 Wh, AS150) is still Range's figure; ColdCell has not drawn it. It is listed so in the interface table.
- **LakeWatch:** plans its surveys on 30.6 min (its R5, restated in its own repository the same day).

### Recommended next step

Re-render the hero, exploded and detail photoreal views on the Mac from the new scenes. The design is ready for TRL 4 parts purchase and AltiRig thrust tests; a recommendation only, not started.

## 2026-10-04: photoreal renders redone after the round-2 and round-3 decisions

Views: hero, exploded, detail; cards regenerated; image_qc passes and `render.py --check` has no FAIL.
