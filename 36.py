
def is_palindromic(string):
	for i in range(len(string) // 2):
		if string[i] != string[-(i+1)]:
			return False
	return True

result = 0

for n in range(1, 1_000_000):
	decimal = str(n)
	binary  = str(bin(n))[2:]
	if is_palindromic(decimal) and is_palindromic(binary):
		result += n

print(result)
