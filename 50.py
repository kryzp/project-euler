
def is_prime(n):
	if n == 1:
		return False
	for i in range(2, int(n ** 0.5) + 1):
		if n % i == 0:
			return False
	return True

N = 1_000_000
primes = set(range(3, N + 1, 2))

for n in range(3, (N // 2) + 1):
	if n not in primes:
		continue
	i = n
	while i < N:
		i += n
		if i in primes:
			primes.remove(i)

primes.add(2)
primes = list(primes)

j = 0
longest_run = 0
longest_summation = 0

while True:
	if j >= len(primes):
		break
	summation = 0
	was_prime = 0
	i = 0
	while i + j < len(primes):
		summation += primes[i + j]
		if summation > N:
			break
		if is_prime(summation):
			if i > longest_run:
				longest_run = i
				longest_summation = summation
		i += 1
	j += 1

print(longest_summation)
