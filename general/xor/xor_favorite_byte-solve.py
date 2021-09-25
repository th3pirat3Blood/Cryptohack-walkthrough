#!/usr/bin/python3

from operator import xor

str_data = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

# Since it is a single byte we have 2^8=256 numbers that either of which could have been selected for key
for n in range(1,256):
	xor_key = ""

	# As xor is being performed bitwise the key needs to be filled with same number 
	for i in range(0, len(str_data), 2):
		xor_key += "0x{:02x}".format(n)[2:]
	
	d = bytearray.fromhex(str_data)
	k = bytearray.fromhex(xor_key)

	potential_flag = bytes(a ^ b for (a, b) in zip(d, k))
	print(f"{n}: ", end="")
	try:
		if "crypto" in potential_flag.decode():
			print(potential_flag.decode())
			break
	except:
		pass
	print("")