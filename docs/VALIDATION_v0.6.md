# HIVE LINK Rev.A — v0.6 Validation

## Result
- Root schematic components: **183**
- Root wire stubs: **592**
- Root global labels: **592**
- Unresolved footprints: **0**
- Critical nets with <2 endpoints: **0**
- All schematic/library S-expressions balanced: **True**

## Critical pin assertions
- XT30: pad 1=GND, pad 2=VIN_RAW — PASS
- CSD19537Q3: S=1/2/3, G=4, D=5 — PASS
- JS202011CQN: common terminals 2 and 5 — PASS
- USB-A: 1=VBUS,2=D-,3=D+,4=GND,SH=Shield — PASS
- USB-C USB4105: A/B duplicated D+/D-/VBUS/GND pads mapped — PASS

## Project-local footprint pad counts
- `Wurth_7447797360_WE-PDF_1045`: pads=2, expected=2, unique labels=2
- `TI_DRT0003_1.0x1.0`: pads=3, expected=3, unique labels=3
- `TI_DQA0010A_2.5x1.0_P0.5`: pads=10, expected=10, unique labels=10
- `TI_RSE0010A_2.0x1.5`: pads=10, expected=10, unique labels=10
- `CK_JS202011CQN_DPDT_THT`: pads=6, expected=6, unique labels=6
- `TRJG0926HENL_CM4IO`: pads=20, expected=20, unique labels=20
- `Raspberry-Pi-4-Compute-Module`: pads=200, expected=200, unique labels=200

## Native KiCad status
- Native ERC: **NOT RUN** — kicad-cli is unavailable in this runtime.
- Update PCB from Schematic: **NOT RUN**.
- Native PCB DRC: **NOT RUN**.
- Therefore v0.6 is **placement-ready, not fabrication-ready**.
