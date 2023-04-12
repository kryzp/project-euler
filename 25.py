
def fibonacci_generator():
	n1 = 0
	n2 = 1
	while True:
		yield n2
		tmp = n1 + n2
		n1 = n2
		n2 = tmp

for i, n in enumerate(fibonacci_generator()):
	if len(str(n)) == 1000:
		print(i + 1)
		break
