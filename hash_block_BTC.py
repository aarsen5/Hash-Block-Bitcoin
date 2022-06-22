#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 20:20:28 2022

@author: AlanArsen
"""

import hashlib
from binascii import unhexlify, hexlify
from datetime import datetime

#convert into little endian format
def littleEndian(string):
	splited = [str(string)[i:i + 2] for i in range(0, len(str(string)), 2)]
	splited.reverse()
	return "".join(splited)

# Data of Bitcoin block #490624
# Input data in hex and time in %Y-%m-%d %H:%M:%S
ver      = "20000000"
prvHash  = "0000000000000000004239f2a01d8f579bc0dbb214d0f874ece5db587bee3457"
merkHash = "73effaecabddef72c9b6b738efb131c543370766b93d4cc15db995a9afb1a286"
timeStmp = "2017-10-19 16:35:32"
bits     = "1800eb30"
nonce    = "b6647bd6"

# Convert to unix time stamp in hex
timeStmp = hex(int(datetime.strptime(timeStmp, '%Y-%m-%d %H:%M:%S').timestamp()))
timeStmp = timeStmp[2:]

# Convert to little-endian hex
ver      = littleEndian(ver)
prvHash  = littleEndian(prvHash)
merkHash = littleEndian(merkHash)
timeStmp = littleEndian(timeStmp)
bits     = littleEndian(bits)
nonce    = littleEndian(nonce)

print("\nBlock data: \n")
print(f"ver:       {ver}")
print(f"prev hash: {prvHash}")
print(f"merk hash: {merkHash}")
print(f"timestamp: {timeStmp}")
print(f"bits:      {bits}")
print(f"nonce:     {nonce}")

# Contactenate hex
header_hex = ver + prvHash + merkHash + timeStmp + bits + nonce

header_bin = unhexlify(header_hex)
hash = hashlib.sha256(hashlib.sha256(header_bin).digest()).digest()
hexlify(hash).decode("utf-8")
blockHash = hexlify(hash[::-1]).decode("utf-8")
print(f"\nBlock hash: {blockHash}\n")
