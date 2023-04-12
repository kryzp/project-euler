
def factors(n):
	i = 2
	ret = set()
	while i * i <= n:
		if n % i == 0:
			n //= i
			ret.add(i)
		else:
			i += 1
	if n > 1:
		ret.add(n)
	return ret

n = 1
while True:
	valid = True
	for i in range(4):
		ff = factors(n + i)
		if len(ff) != 4:
			valid = False
			break
	if valid:
		break
	n += 1

print(n)
