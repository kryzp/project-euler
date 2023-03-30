
DIGS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def text(n):
	ret = ""
	cnc = ""
	if n >= 1000:
		ret = text(n // 1000) + " thousand"
		n %= 1000
		cnc = " and " if n < 100 else ", "
	elif n >= 100:
		ret = text(n // 100) + " hundred"
		n %= 100
		cnc = " and "
	elif n >= 20:
		ret = TENS[n // 10 - 2]
		n %= 10
		cnc = "-"
	else:
		if n == 0:
			return ""
		return DIGS[n - 1]
	return ret + ("" if n == 0 else cnc) + text(n)

def nchr(n):
	return len(text(n).replace(' ', '').replace('-', ''))

res = 0

for i in range(1, 1001):
    res += nchr(i)

print(res)
