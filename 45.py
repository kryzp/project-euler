
def T  ( n): return n * (1*n + 1) / 2
def P  ( n): return n * (3*n - 1) / 2
def H  ( n): return n * (2*n - 1)
def isT(Tn): return (-1 + ((1 +  8*Tn) ** 0.5)) % 1 == 0
def isP(Pn): return ( 1 + ((1 + 24*Pn) ** 0.5)) % 3 == 0

n = 143 + 1

while True:
	h = H(n)
	if isT(h) and isP(h):
		print(h)
		break
	n += 1
