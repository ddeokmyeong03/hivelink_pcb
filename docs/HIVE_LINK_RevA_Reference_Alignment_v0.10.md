# HIVE LINK Rev.A — Reference Alignment v0.10

## Ethernet ESD alignment

Rev.A U19/U20 Ethernet ESD devices are aligned to `TPD4EUSB30`, matching the Raspberry Pi CM4 official Ethernet reference design.

Why:
- Raspberry Pi's CM4 Ethernet reference directly uses TPD4EUSB30.
- TPD4EUSB30 and the previous TPD4E05U06 option share the same DQA 10-pin signal/GND/NC pin arrangement used by this design.
- The project-local DQA footprint can therefore be retained.
- TPD4EUSB30 provides flow-through routing and a 5 A 8/20 us surge rating.

The Pixhawk TELEM interface ESD device U11 remains `TPD4E05U06`; the CM4 Ethernet reference does not apply to that interface.

## Routing baseline

- Ethernet: 100 ohm differential, P/N ideally matched to <=0.15 mm.
- USB 2.0: 90 ohm differential, P/N ideally matched to <=0.15 mm.
- CAN-FD: connector-side protection; CAN debug pads must be local/inline, not remote T-stubs.
- L2 remains a continuous GND reference plane.

## Fabrication gate

This change does not make the board fabrication-ready. Required next steps remain:

1. Native KiCad ERC
2. Update PCB from Schematic
3. Official-footprint courtyard verification
4. Controlled-impedance routing
5. DRC
6. Independent Gerber/drill inspection
