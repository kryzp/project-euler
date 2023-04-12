
coins = [1, 2, 5, 10, 20, 50, 100, 200]
paths = [0] * 201
paths[0] = 1

for c in coins:
	for i in range(c, 201):
		paths[i] += paths[i - c]

print(paths[200])
