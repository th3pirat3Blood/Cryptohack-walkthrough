#!/usr/bin/python3

# Extended Euclidean theorem: qu + pv = gcd(p,q)

def extended_gcd_func(d1, d2):
	rem = count = 0
	q_list = [] 
	r_list = []
	u_list = []
	t_list = []	
	u0 = t1 = 1
	u1 = t0 = 0
	u2 = t2 = None

	while True:
		rem = d1 % d2
		q = int(d1 / d2)
		u2 = u0 - q*u1
		t2 = t0 - q*t1
	
		u_list.append(u2)
		t_list.append(t2)
		r_list.append(rem)
		q_list.append(q)
				
		count += 1
		d1 = d2
		d2 = rem
		u0 = u1
		u1 = u2
		t0 = t1
		t1 = t2
		if rem == 0:
			break
	print(f"u: {u_list[-2]} \tt: {t_list[-2]}")


p, q = 26513, 32321
# p , q = 161, 28
print(f"{p}u + {q}t = gcd(p,q)")
extended_gcd_func(p, q)
