num = 1

while True:
	yes = True
	for i in range(1, 21):
		if num % i != 0:
			yes = False
			break
	if yes:
		break
	num += 1

print(num)
