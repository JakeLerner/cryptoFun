# Algorithms implemented by Jake Lerner, to help him understand his Math 116 (cryptography) homework.

def euclid_gcd_recursive(a,b):
	# takes in two integers a and b, with a >= b
	# recursively runs the euclidean algorithm
	# outputs their greatest common divisor as an integer

	assert a >= b
	if b == 0: 
		return a
	else:
		return euclid_gcd_recursive(b , a % b)

def euclid_gcd_iterative(a,b):
	# takes in two integers a and b, with a >= b
	# iteratively runs the euclidean algorithm
	# outputs their greatest common divisor as an integer

	assert a >= b
	r = [a, b]
	i = 1
	while True:
		r.append(r[i-1]%r[i])
		if r[i + 1] == 0:
			return r[i]
		else:
			i = i + 1

def gcd_tester(fn):
	# Test Function to assert algorithm implementation is correct
	assert fn(4,2) == 2
	assert fn(17 * 49, 17 * 35) == 17 * 7
	assert fn(41, 3) == 1 
	assert fn(129458, 129458) == 129458
	print "~~ GCD Test Passed ~~"


# test both implementations
gcd_tester(euclid_gcd_recursive)
gcd_tester(euclid_gcd_iterative)


def extended_euclid(a, b):
	# Generally, the Extended Euclidean Algorithm states that:
	# "For positive integers a and b, there exist integers u and v such that au + bv = gcd(a,b)."
	#  This function takes in two integers a and b, and returns a tuple of three integers u, v, and g such that
	#  au + bv = gcd(a,b) = g.

	u = 1
	g = a
	x = 0
	y = b
	while y: 
		q = g / y
		t = g % y
		s = u - (q * x)
		u = x
		g = y
		x = s
		y = t
	v = (g - a * u )/ b
	return (u, v, g)

def find_inverse(a, m):
	#Finds the multiplicative inverse of a (mod m), or returns 0 if a has no inverse in Z/mZ,
	#using the extended euclidean algorithm
	u,v,g = extended_euclid(a,m)
	if g != 1:
		return 0
	else:
		return u



def inverse_tester(fn):
	assert fn(3,5) == 2
	assert fn (12,27) == 0
	assert fn (15,29) == 2
	assert fn (4,27) == 7
	print "~~ Inversion Tests Passed ~~"

#test extended euclid and find_inverse

inverse_tester(find_inverse)



	


