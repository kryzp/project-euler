
i = 0
num = 0
N = 10_001

def is_prime(n):
	for i in range(2, n // 2):
		if n % i == 0:
			return False
	return True

while i <= (N + 1):
	print(str(i / (N + 1) * 100) + '%')
	num += 1
	if is_prime(num):
		i += 1

print(num)
