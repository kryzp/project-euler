
def d(n):
	result = set()
	for i in range(1, 1 + int(n ** 0.5)):
		if n % i == 0:
			result.add(int(i))
			result.add(int(n / i))
	return sum(result) - n

amicable = 0
N = 10000

for a in range(220, N):
	b = d(a)
	if a == d(b) and a != b:
		amicable += a

print(amicable)
