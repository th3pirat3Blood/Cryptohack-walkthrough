#!/usr/bin/python3

from operator import xor

data = "label"

# converting to corresponding integer list
data_int = [ord(c) for c in data]

# xor for each integer value in list
xor_data = [xor(v,13) for v in data_int]

# converting back xored integer to string value
print("".join([chr(i) for i in xor_data]))