N = 2_000_000
primes = set(range(3, N+1, 2))

for n in range(3, N//2 + 1):
	if n not in primes:
		continue
	i = n
	while i < N:
		i += n
		if i in primes:
			primes.remove(i)

print(sum(primes))
