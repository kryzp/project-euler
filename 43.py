import itertools as it

P = list(it.permutations("1234567890"))

primes = [1, 2, 3, 5, 7, 11, 13, 17]

def has_property(p):
	for i in range(len(p) - 2):
		n = int("".join(p[i:(i+3)]))
		if n % primes[i] != 0:
			return False
	return True

ret = 0
for p in P:
	if has_property(p):
		ret += int("".join(p))
print(ret)
