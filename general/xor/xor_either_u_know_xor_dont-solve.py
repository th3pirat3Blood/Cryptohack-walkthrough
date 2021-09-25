#!/usr/bin/python3

data = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"

flag_format = "crypto{}"

ff_hex ="".join([hex(ord(c))[2:] for c in flag_format])

ff_byte = bytearray.fromhex(ff_hex)

# Taking first 6 bytes and the last one as "crypto{" will be xored with first 6 bytes
# but the "}"" will be xored with the last byte
data_byte = bytearray.fromhex("0e0b213f26041e04")

xor_key = bytes(a ^ b for (a, b) in zip(ff_byte, data_byte))
print(f"XOR key: {xor_key}")

# Since the key length is small ... it needs to be repeated till we get to the length of data
xor_key = xor_key*10+b'cryp'

data_byte = bytearray.fromhex(data)

flag = bytes(a ^ b for (a, b) in zip(xor_key, data_byte))
print(flag.decode())
