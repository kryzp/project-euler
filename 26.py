
def cycle(d):
    digit_indexes = {}
    digits = []
    n = 1
    i = 0
    while True:
        digit_indexes[n] = i
        n *= 10
        digit = n // d
        n -= digit * d
        digits.append(digit)
        if n in digit_indexes:
            return len(digits[digit_indexes[n]:])
        i += 1

number = -1
maxima = -1
for i in range(1, 1000):
	c = cycle(i)
	if c > maxima:
		maxima = c
		number = i
print(number)
