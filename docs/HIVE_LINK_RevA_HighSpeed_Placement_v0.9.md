# HIVE LINK Rev.A — High-Speed Placement Review v0.9

## Status

This review covers **placement-level signal integrity preparation** for the Rev.A board. It is not a claim of routed impedance compliance.

## Official targets

### Raspberry Pi CM4 Ethernet
- 100 ohm differential pairs.
- P/N within each pair should ideally be matched to better than 0.15 mm.
- Pair-to-pair matching should be better than 50 mm; deliberate pair-to-pair tuning is usually unnecessary.

### Raspberry Pi CM4 USB 2.0
- 90 ohm differential pair.
- P/N should ideally be matched to better than 0.15 mm.

### CAN-FD
- TCAN1042HGV supports CAN FD up to 5 Mbps.
- Connector-side ESD/protection placement is required.
- Debug pads on CAN_H/L must be inline or effectively zero-stub; no long T-branches.

## v0.9 placement corrections

Compared with v0.8:
- U9 CAN1 ESD moved between J3 and U7.
- U10 CAN2 ESD moved between J4 and U8.
- U11 TELEM ESD moved directly behind J2.
- TP110 / TP111 moved next to the CAN1 bus path.
- TP112 / TP113 moved next to the CAN2 bus path.
- CAN decoupling and standby components were compacted around U7 / U8.
- TELEM series resistors were moved behind the connector-side ESD stage.

## Routing rules

1. Route Ethernet before ordinary low-speed nets.
2. Keep a continuous L2 GND reference under Ethernet and USB.
3. Put ESD physically between the external connector and the protected electronics.
4. Do not add USB D+/D- test stubs.
5. Route CAN_H/L through or directly past local debug pads instead of creating long T-stubs.
6. Leave CAN termination jumpers open unless the HIVE LINK node is physically at the bus end.
7. Use the PCB fabricator's impedance calculator for the final stack-up; do not freeze trace width/gap from the preview board.

## Hard gate before fabrication

- Native KiCad ERC
- Update PCB from Schematic
- Official-footprint courtyard verification
- Controlled-impedance routing
- DRC
- Gerber/drill inspection
