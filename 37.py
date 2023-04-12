
def is_prime(n):
	if n == 1:
		return False
	for i in range(2, 1 + int(n ** 0.5)):
		if n % i == 0:
			return False
	return True

found = set()

n = 10
while len(found) != 11:
	string = str(n)
	is_valid = True
	for i in range(len(string)):
		if not is_prime(int(string[i:])):
			is_valid = False
			n += 1
			break
	if not is_valid:
		continue
	for i in range(1, len(string)):
		if not is_prime(int(string[:i])):
			is_valid = False
			n += 1
			break
	if is_valid:
		found.add(n)
	n += 1

print(sum(found))
