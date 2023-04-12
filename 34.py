
def fact(n):
	x = 1
	for i in range(2, n+1):
		x *= i
	return x

result = 0

for n in range(10, 1000000): # literally just picked a big number lol
	if sum(fact(int(c)) for c in str(n)) == n:
		result += n

print(result)
