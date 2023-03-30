
def fact(n):
	res = 1
	for i in range(1, n+1):
		res *= i
	return res

def num_routes(sz):
	return fact(sz * 2) // (fact(sz) ** 2)

print(num_routes(20))
