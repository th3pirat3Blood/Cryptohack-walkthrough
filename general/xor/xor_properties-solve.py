#!/usr/bin/python3

from operator import xor

k1 = 0xa6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
k12 = 0x37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
k23 = 0xc1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
k123f = 0x04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf

k123 = xor(k1, k23)

flag = hex(xor(k123, k123f))

print(f"flag hex: {flag}")
print(bytearray.fromhex(flag[2:]).decode())