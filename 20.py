# its basically cheating to use python to solve old problems :/

def fact(n):
	r = 1
	for i in range(1, n + 1):
		r *= i
	return r
print(sum(int(c) for c in str(fact(100))))
