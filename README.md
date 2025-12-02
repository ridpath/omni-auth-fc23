<!--
OmniPLC FC23 authenticated modbus writer security tool designed for ICS OT penetration
testing, industrial protocol exploitation, Modbus TCP vulnerability assessment, PLC
register write authentication bypass, insecure by design protocol demonstration,
HackTheBox ICS lab exploitation, ethical security researcher toolkit,
safe Python modbus automation, FC23 read/write multiple registers testing,
operational technology risk validation, red teaming industrial networks,
cyber-physical system security experiment.

Key SEO: modbus hacking tool, PLC security audit, SCADA exploitation research,
ICS protocol pen test script, function code 23 abuse, modbus password register,
OmniPLC 3000 testing, HackTheBox Alchemy tools, industrial control threat simulation
-->

# OmniPLC FC23 Authenticated Modbus Writer
![Status: Alpha](https://img.shields.io/badge/status-alpha-orange)
![Protocol: Modbus](https://img.shields.io/badge/protocol-Modbus%20TCP-blue)
![Function Code: 23](https://img.shields.io/badge/FC23-Read%2FWrite%20Multiple%20Registers-green)
![Tested On: HTB Alchemy](https://img.shields.io/badge/tested-HTB%20Alchemy-purple)
![ICS/OT Security](https://img.shields.io/badge/domain-ICS%20%2F%20SCADA-red)
![MIT License](https://img.shields.io/badge/license-MIT-lightgrey)

**Protocol:** Modbus TCP (Function Code 23 - Read/Write Multiple Registers)  
**Compatibility:** Tested with `pymodbus==3.0.0rc1`

---

## Overview

This Python script performs **authenticated writes** to Modbus holding registers using **function code 23 (FC23)**. It was built to interact with the *OmniPLC 3000* and similar ICS/PLC systems where write operations are **password-protected via in-band Modbus memory registers**.

---

## Features

- FC23 read/write combo support
- Authentication via ASCII password (e.g., `"Hacker1337#4"`)
- Post-auth write delay to simulate server-side unlock window
- Supports:
  - Hex values (e.g. `0x64`)
  - ASCII strings
  - IEEE 754 float-to-register conversions (`--float` mode)


### MITRE ATT&CK for ICS Mapping

| Capability | ATT&CK Technique | ID |
|-----------|-----------------|---|
| Unauthorized Modbus Writes | Manipulation of Control | T0834 |
| Targeting Registers/PLC Memory | Access to Program Organization Units | T0865 |
| Privilege Abuse via Auth Registers | Exploitation for Evasion | T0828 |
| Stateful Timing to Evade Detection | Inhibit Response Function | T0814 |
| Reading Sensitive Register Data | Monitor Process State | T0809 |

---

##  Example Use Case

```bash
python3  omni_fc23_writer.py \
  --host 172.19.8.3 \
  --auth "Hacker1337#4" \
  --auth-addr 3890 \
  --address 1027 \
  --data 0x64
```
##  Command-Line Arguments

| Flag         | Description |
|--------------|-------------|
| `--host`     | Modbus TCP IP address |
| `--port`     | *(Optional)* Default is `502` |
| `--unit-id`  | *(Optional)* Modbus Unit ID, default is `1` |
| `--auth`     | ASCII password for FC23 auth (e.g. `"Hacker1337#4"`) |
| `--auth-addr`| Register address to authenticate against |
| `--address`  | Register address to write data to |
| `--data`     | Data to write (ASCII or hex like `0x64`) |
| `--float`    | *(Optional)* Convert float to 2x registers |
| `--delay`    | Wait time (in seconds) after auth (default: `0.5`) |

---

## Dependencies

```bash
pip install pymodbus==3.0.0rc1
```
## Disclaimer

This tool is provided **strictly for educational and ethical security testing purposes**.  

> Modbus is an unauthenticated protocol designed for trusted environments. Improper use may result in physical system disruption or damage.

By using this software, you agree to the following:

- You will only use it on systems you own or have **explicit written permission** to test.
- You will not use it in production, critical infrastructure, or safety systems.
- The author **assumes no liability** for any damage caused by misuse or unauthorized deployment.

This script is intended to **promote awareness of insecure-by-design ICS protocols** and assist in defensive research, training, and ethical penetration testing.

## License

This project is licensed under the [MIT License](LICENSE).




<!--
SEO Footer — OmniPLC FC23 Authenticated Modbus Writer

Keywords:
modbus unauthorized write detection, PLC register manipulation testing,
ICS security exploitation demo, authenticated modbus payload injection,
read/write multiple registers attack, OT red team support tools,
pymodbus script for ethical SCADA research, hardware-in-the-loop testing,
industrial cyber security awareness, MITRE for ICS mapping, HTB Alchemy ICS kit

Audience:
SCADA penetration testers, ICS defenders, security engineers, and OT red teams

Purpose:
Enable controlled, permission based evaluation of weak Modbus protections
and authentication designs in research environments.
-->
