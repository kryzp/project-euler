
fac = 0
N = 600851475143

while N % 2 == 0:
	fac = 2
	N //= 2

for i in range(1, N // 2):
	if N % i == 0:
		fac = i
		if N == i:
			break
		N //= i

print(fac)
