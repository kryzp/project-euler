
def is_pand(n):
	if len(n) != 9:
		return False
	if '0' in n:
		return False
	for c in "123456789":
		if n.count(c) > 1:
			return False
	return True

products = set()

for i in range(1, 99):
	for j in range(i, 9999):
		if is_pand(str(i) + str(j) + str(i * j)):
			print(i, '*', j, '=', i * j)
			products.add(i * j)

print(sum(products))
