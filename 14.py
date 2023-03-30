
chain = []

def collatz(n):
	global chain
	chain.append(n)
	if n == 1:
		return int(n)
	if n % 2 == 0:
		return collatz(n / 2)
	elif n % 2 == 1:
		return collatz(3*n + 1)

mxlen = (-1, -1)

for i in range(1, 1_000_000):
	print(i)
	chain.clear()
	collatz(i)
	if len(chain) > mxlen[1]:
		mxlen = (i, len(chain))

print(mxlen)
