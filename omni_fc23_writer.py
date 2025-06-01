#!/usr/bin/env python3
"""
OmniPLC FC23 Authenticated Modbus Writer
Author: Ridpath

Performs authenticated write operations over Modbus TCP using 
Function Code 23 (Read/Write Multiple Registers). Supports password-
protected write regions like those used in ICS targets such as 
the OmniPLC 3000.

Features:
- Authentication via ASCII password (per-register memory auth)
- Support for writing ASCII, hex, and IEEE 754 float values
- Optional delay after authentication
- CLI-friendly argument parsing

Designed for ethical use in ICS/SCADA simulation environments 


License: MIT
"""

from pymodbus.client import ModbusTcpClient
from pymodbus.pdu import ExceptionResponse
import struct
import argparse
import time

def float_to_registers(f, byteorder='big'):
    b = struct.pack('>f' if byteorder == 'big' else '<f', f)
    return [int.from_bytes(b[0:2], byteorder='big'), int.from_bytes(b[2:4], byteorder='big')]

def send_fc17(client, unit_id, read_addr, read_count, write_addr, write_regs):
    response = client.readwrite_registers(
        read_address=read_addr,
        read_count=read_count,
        write_address=write_addr,
        write_registers=write_regs,
        unit=unit_id
    )
    if isinstance(response, ExceptionResponse) or response.isError():
        print(f"[!] Error: {response}")
        return False, None
    print(f"[+] Success! Response: {response.registers}")
    return True, response.registers

def main():
    parser = argparse.ArgumentParser(description="OmniPLC 3000 FC23 Authenticated Writer (HTB-Compatible)")
    parser.add_argument('--host', required=True, help='Modbus TCP host')
    parser.add_argument('--port', type=int, default=502, help='Modbus TCP port')
    parser.add_argument('--unit-id', type=int, default=1, help='Modbus Unit ID')
    parser.add_argument('--auth', type=str, help='Authentication password')
    parser.add_argument('--auth-addr', type=int, default=3890, help='Authentication register')
    parser.add_argument('--address', type=int, required=True, help='Register to write to')
    parser.add_argument('--data', required=True, help='Data to write (0x64 or ASCII)')
    parser.add_argument('--float', action='store_true', help='Interpret data as float (IEEE 754)')
    parser.add_argument('--delay', type=float, default=0.5, help='Delay after auth (default: 0.5s)')
    args = parser.parse_args()

    client = ModbusTcpClient(args.host, port=args.port)
    if not client.connect():
        print("[!] Failed to connect to Modbus server")
        return

    try:
        if args.auth:
            pw_regs = [ord(c) for c in args.auth]
            print(f"[+] Authenticating with password '{args.auth}' at {args.auth_addr}")
            ok, _ = send_fc17(client, args.unit_id, args.auth_addr, len(pw_regs), args.auth_addr, pw_regs)
            if not ok:
                print("[!] Auth failed.")
                return
            print(f"[+] Waiting {args.delay}s after auth...")
            time.sleep(args.delay)

        if args.float:
            val = float(args.data)
            regs = float_to_registers(val)
            print(f"[+] Writing float {val} as {regs} to {args.address}")
        else:
            if args.data.startswith("0x"):
                regs = [int(x, 16) for x in args.data.split(',')]
            else:
                regs = [ord(c) for c in args.data]
            print(f"[+] Writing {regs} to {args.address}")

        ok, _ = send_fc17(client, args.unit_id, args.address, len(regs), args.address, regs)
        if not ok:
            print("[!] Data write failed.")

    finally:
        client.close()
        print("[*] Modbus session closed.")

if __name__ == "__main__":
    main()
