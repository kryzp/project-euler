
result = 0

for n1 in range(6 * (9 ** 5)): # max upper bound is around 6 digits
	n1str = str(n1)
	if len(n1str) <= 1:
		continue
	n2 = 0
	for d in [int(c) for c in n1str]:
		n2 += d ** 5
	if n1 == n2:
		result += n1

print(result)
