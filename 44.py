
def P(n):
	return n * (3*n - 1) / 2

def isP(Pn):
	return (1 + ((1 + 24*Pn) ** 0.5)) % 3 == 0

minima = 999999999
for k in range(1, 10000):
	for j in range(k + 1, 10000):
		diff = P(j) - P(k)
		summ = P(j) + P(k)
		if isP(diff) and isP(summ):
			minima = int(min(minima, abs(diff)))
print(minima)
