
## Generate Points on an Elliptic Curve y^2 = ax^3 + bx + c in the Field Fp
## Done in a single list comprehension, because that's what's fun :)

def findPoints(a,b,c,p):
	return [(x, y) for x in range(p) for y in range(p) if (a * x ** 3 + b * x + c) % p == (y ** 2) % p] 

points = findPoints(1,2,2,17)
