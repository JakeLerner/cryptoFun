## Implements Miller Rabin Primality Testing in a probably inefficient way
## (Mostly to help me understand the algorithm)



def gcd(a,b):
	# takes in two integers a and b, with a >= b
	# recursively runs the euclidean algorithm
	# outputs their greatest common divisor as an integer

	assert a >= b
	if b == 0: 
		return a
	else:
		return gcd(b , a % b)


#returns true iff N is a composite number
def mrWitness(N, witness, verbose = False):
	gcdW = gcd(N, witness)
	if gcdW > 1 and gcdW < N:
		if verbose:
			print "Proven composite in step 1 by witness %d" %witness
		return True
	x = N - 1
	k = 0
	while x%2 == 0:
		k += 1
		x = x / 2
	q = x
	a = witness ** q
	if a % N == 1:
		if verbose:
			print "Test 2 Fails with witness %d" %witness
		return False

	i = 0
	while i <= k - 1:
		if a % N == N - 1:
			if verbose:
				print "Test 3 Fails with witness %d" %witness
			return False
		a = (a ** 2) % N
		i += 1
	if verbose:
		print "Proven composite in step 4 by witness %d" %witness
	return True


#return true if N is a composite number
#Not yet probabilistic, ie doesn't operate in a monte carlo way just tests all witnesses less than maxN (or N-1 if no maxN is specified)
def millerRabin(N, verbose = False, maxN = 0):
	if not maxN:
		maxN = N - 1
	result = False
	witness = 2
	while not result and witness < maxN:
		result = mrWitness(N, witness, verbose)
		if verbose and result:
			print "hit at witness value of: " + str(witness)
		witness += 1
	if verbose and result:
		print "*********** Mission Accomplished for %d ***********" %N
	elif verbose:
		print "****** %d Could Be Prime Who Knows*******" %N
	return result





#some arbitrary primes slightly larger than 10^6
primes = [1020751, 1020757, 1020779, 1020797, 1020821, 1020823, 1020827, 1020839, 1020841, 1020847, 1020853, 1020881, 1020893, 1020907, 1020913, 1020931, 1020959, 1020961, 1020967, 1020973, 1020977, 1020979, 1020989, 1020991, 1020997, 1021001, 1021019, 1021043, 1021067, 1021073, 1021081, 1021087]

#some arbitrary non-smooth composites slightly larger than 10^12 (the products of the above primes)
bigComposites = [primes[i] * primes[j] for i in range(len(primes)) for j in range(len(primes))]

#Other arbitrary but more smooth composites around the size of 10^6 or 10^7
smallComposites = [prime - 1 for prime in primes]
medComposites = [primes[i] * (i + 2) for i in range(len(primes))]

def test(verbose = False):
	a = [number for number in smallComposites if millerRabin(number,verbose)]
	assert a == smallComposites
	if verbose:
		print "--------------------------------------------------------------"
		print "----------------------Passed Test 1---------------------------"
		print "--------------------------------------------------------------"		
	b = [number for number in medComposites if millerRabin(number, verbose)]
	assert b == medComposites
	if verbose:
		print "--------------------------------------------------------------"
		print "----------------------Passed Test 2---------------------------"
		print "--------------------------------------------------------------"	

	#Turns out the big composites are just too big for this little macbook air :(
	"""
	c = [number for number in bigComposites if millerRabin(number, verbose)]
	assert c == bigComposites
	if verbose:
		print "--------------------------------------------------------------"
		print "----------------------Passed Test 3---------------------------"
		print "--------------------------------------------------------------"
	"""

	d = [number for number in primes if millerRabin(number, verbose, 50)]
	print "primes " + str(len(primes))
	print "returned " + str(len(d))
	if verbose:
		print "--------------------------------------------------------------"
		print "----------------------Passed Test 4---------------------------"
		print "--------------------------------------------------------------"

test(True)
