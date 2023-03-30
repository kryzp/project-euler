
num = -1

for i in range(1, 1000):
	for j in range(1, 1000):
		sr = str(i * j)
		eq = True
		for k in range(len(sr) // 2):
			if sr[k] != sr[-k-1]:
				eq = False
				break
		if eq and i * j > num:
			num = i * j

print(num)
