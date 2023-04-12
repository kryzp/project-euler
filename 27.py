
def is_prime(n):
	if n == 0:
		return False
	for i in range(2, int(n ** 0.5) + 1):
		if n % i == 0:
			return False
	return True

maxima = [-1, -1, -1]

for a in range(-1000 + 1, 1000):
	for b in range(-1000, 1000 + 1):
		n = 0
		while True:
			f = (n * n) + (a * n) + b
			if not is_prime(abs(f)):
				break
			n += 1
		if n > maxima[0]:
			maxima[0] = n
			maxima[1] = a
			maxima[2] = b

print(maxima)
print(maxima[1] * maxima[2])
