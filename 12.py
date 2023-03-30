
def trin(n):
	return int(n * (n + 1) / 2)

val = 0
i = 0
while True:
	val = trin(i)
	div = 0
	for j in range(1, int((val ** 0.5) + 1)):
		if (val / float(j)) % 1 == 0:
			div += 2
	if div > 500:
		break
	i += 1

print(val)
