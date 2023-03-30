
def divsum(n):
	ret = 0
	for i in range(2, 1 + int(n ** 0.5)):
		if n % i == 0:
			ret += i
			if i*i != n:
				ret += n / i
	return int(ret + 1)

def abundant(n):
	return divsum(n) > n

L = 28123
ret = 0
abundants = set(p for p in range(1, L+1) if abundant(p))

for n in range(1, L+1):
	for a in abundants:
		b = n - a
		if b in abundants:
			break
	else:
		ret += n

print(ret)
