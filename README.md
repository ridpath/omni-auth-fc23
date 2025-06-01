# OmniPLC FC23 Authenticated Modbus Writer
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




