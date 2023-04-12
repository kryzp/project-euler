
def is_prime(n):
	if n == 1 or n == 2:
		return True
	for i in range(2, 1 + int(n ** 0.5)):
		if n % i == 0:
			return False
	return True

def turn(string, amount):
	return string[amount:] + string[:amount]

circular_primes = set()

for i in range(2, 1_000_000):
	if all(is_prime(int(turn(str(i), j))) for j in range(len(str(i)))):
		circular_primes.add(i)

print(len(circular_primes))
