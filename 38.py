
n = set()

def ispand(x):
	nums = set()
	for c in x:
		if c == '0':
			return False
		nums.add(c)
	return len(nums) == len(x)

for N in range(1, 10000):
	conp = ""
	for i in range(1, 500):
		conp += str(N * i)
		if len(conp) == 9 and ispand(str(conp)):
			n.add(int(conp))

print(max(n))
