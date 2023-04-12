
def is_prime(n):
	if n == 1:
		return False
	for i in range(2, int(n**0.5)+1):
		if n % i == 0:
			return False
	return True

i = 9
while True:
	if is_prime(i):
		i += 2
		continue
	s = 1
	bb = True
	while 2*s*s < i:
		if is_prime(i - 2*s*s):
			bb = False
			break
		s += 1
	if bb:
		print(i)
		break
	i += 2
