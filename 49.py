import itertools

def is_prime(n):
	if n == 1:
		return False
	for i in range(2, int(n ** 0.5) + 1):
		if n % i == 0:
			return False
	return True

terms = []

for n in range(10 ** 3, 10 ** 4):
	if n == 1487:
		continue
	if not is_prime(n):
		continue
	perms = [int("".join(x)) for x in itertools.permutations(str(n))]
	terms.clear()
	valid = True
	for i in range(3):
		m = n + (3330 * i)
		terms.append(m)
		if not is_prime(m):
			valid = False
			break
		if m not in perms:
			valid = False
			break
	if valid:
		break

print("".join(str(x) for x in terms))
