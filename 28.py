
def count_diagonals(n):
	d = 2
	i = 0
	c = 1
	s = 1
	for j in range(2 * (n - 1)):
		c += d
		i += d
		s += c
		if i >= 4 * d:
			i = 0
			d += 2
	return s

print(count_diagonals(1001))
