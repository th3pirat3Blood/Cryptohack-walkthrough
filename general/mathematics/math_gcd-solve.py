#!/usr/bin/python3

def gcd(divident, divisor):
	rem = divident % divisor
	if rem == 0:
		return divisor
	else:
		return gcd(divisor, rem)

a, b = 66528, 52920

print(gcd(a, b))