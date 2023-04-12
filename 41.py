import itertools as it

def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def longest_n_digit(digits):
	p = list(it.permutations("123456789"[:digits]))
	for i in range(len(p) - 1, -1, -1):
		j = p[i]
		n = int("".join(j))
		if is_prime(n):
			return n
	return -1

longest = -1
for i in range(1, 9 + 1):
	longest = max(longest, longest_n_digit(i))
print(longest)
