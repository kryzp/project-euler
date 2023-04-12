
def n_solutions(p):
	sol = set()
	for a in range(1, p):
		for b in range(1, p):
			c = (a**2 + b**2) ** 0.5
			if c == int(c) and (b, a, c) not in sol and (a + b + c) == p:
				sol.add((a, b, c))
	return len(sol)

solutions = set()

for p in range(0, 1001):
	solutions.add((n_solutions(p), p))

print(max(solutions)[1])
