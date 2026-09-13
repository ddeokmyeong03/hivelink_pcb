# HIVE LINK Core Rev.A — PCB

HIVE LINK is a detachable heterogeneous unmanned-system mission node developed by TRUE:D Labs.

This repository is the GitHub/KiCanvas working repository for **HIVE LINK Core Rev.A**.

## Open in KiCanvas

### Repository
https://kicanvas.org/?github=https://github.com/ddeokmyeong03/hivelink_pcb

### System schematic overview
https://kicanvas.org/?github=https://github.com/ddeokmyeong03/hivelink_pcb/blob/main/HIVE_LINK_RevA.kicad_sch

### PCB placement preview
https://kicanvas.org/?github=https://github.com/ddeokmyeong03/hivelink_pcb/blob/main/HIVE_LINK_RevA_KiCanvas_Placement_Preview.kicad_pcb

### Detailed sheets currently synchronized
- Identity: https://kicanvas.org/?github=https://github.com/ddeokmyeong03/hivelink_pcb/blob/main/09_IDENTITY_RTC.kicad_sch
- Expansion: https://kicanvas.org/?github=https://github.com/ddeokmyeong03/hivelink_pcb/blob/main/10_EXPANSION_IO.kicad_sch

## Current engineering milestone

**Rev.A / v0.9 — full placement/ratsnest preview prepared locally + high-speed placement correction**

The GitHub root remains intentionally optimized for KiCanvas review while the full detailed source is kept under native-KiCad verification.

Current root files:

- `HIVE_LINK_RevA.kicad_pro` — project
- `HIVE_LINK_RevA.kicad_sch` — KiCanvas system-level overview
- `HIVE_LINK_RevA.kicad_pcb` — 100 × 70 mm board floorplan
- `HIVE_LINK_RevA_KiCanvas_Placement_Preview.kicad_pcb` — browser placement preview
- `HIVE_LINK_RevA.kicad_dru` — conservative custom DRC rules

> **Important:** the root schematic shown in KiCanvas is a system-level review schematic, not the fabrication-release detailed schematic.

## v0.9 placement review

The v0.9 engineering pass corrected high-speed/field-interface placement before routing:

- CAN1/2 ESD devices moved connector-side
- TELEM ESD moved connector-side
- remote CAN_H/L debug pads moved local to the transceivers to avoid long PCB stubs
- CAN support components compacted around each transceiver
- TELEM series resistors compacted behind the ESD stage

Review document:
- `docs/HIVE_LINK_RevA_HighSpeed_Placement_v0.9.md`

## Electrical design baseline

Completed in the engineering design baseline:

- 7–24 V protected power input
- TPS26632 eFuse / reverse-polarity protection
- INA226 power telemetry
- AP64501 5 V / 5 A system rail
- independent 3.3 V node-controller rail
- STM32G0B1 node controller
- Raspberry Pi CM4 carrier interface
- partial-power-down-safe STM32 ↔ CM4 isolation
- dual CAN-FD
- Pixhawk / PX4 TELEM interface
- Gigabit Ethernet
- USB Host + eMMC recovery path
- ATECC608C hardware-backed node identity
- universal adapter expansion interface

## Board baseline

- Board: **100 × 70 mm**
- Layers: **4**
- Nominal thickness: **1.6 mm**
- Baseline stack-up: **JLCPCB JLC04161H-7628**
- L2: continuous GND plane
- L3: power distribution
- Ethernet target: 100 Ω differential
- USB 2.0 target: 90 Ω differential

## Placement data already synchronized

- `docs/HIVE_LINK_RevA_Full_Placement_v0.8.csv`
- `docs/HIVE_LINK_RevA_Placement_Audit_v0.8.md`
- `docs/HIVE_LINK_RevA_Placement_Review_v0.8.md`
- `docs/VALIDATION_v0.6.md`

## Fabrication gate

This repository is **not fabrication-ready yet**.

Required before Gerber release:

1. Open the full detailed design in native KiCad
2. Run ERC
3. Update PCB from Schematic
4. Apply/verify physical placement
5. Route Power → Ethernet → USB → CAN → low-speed signals
6. Refill zones and verify return-current paths
7. Run DRC
8. Independent Gerber/drill review
9. Power-only bench bring-up without CM4 installed
10. Install CM4 only after rails and protection are verified

## KiCanvas note

KiCanvas is used for browser-based review and sharing. Native KiCad remains the source of truth for ERC, PCB synchronization, routing and DRC.

## Status

Latest engineering baseline: **v0.9**
