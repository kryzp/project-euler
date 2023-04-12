import numpy as np

c = [9 * (i + 1) * 10 ** i for i in range(20)]

def digit(n):
	i = 0
	while n > c[i]:
		n -= c[i]
		i += 1
	l = (n - 1) / (i + 1)
	d = (n - 1) % (i + 1)
	return int(str(10 ** i + l)[d])

product = 1
for i in range(7):
	product *= digit(10 ** i)
print(product)
