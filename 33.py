
numerator_fin = 1
denomenator_fin = 1

def replace_once(string, fromch, toch):
	ret = list(string)
	for i in range(len(ret)):
		if ret[i] == fromch:
			ret[i] = toch
			break
	return "".join(ret)

for denomenator in range(10, 100):
	for numerator in range(10, denomenator):
		if denomenator == numerator:
			continue
		uncanceled_value = numerator / denomenator
		canceled_denom = str(denomenator)
		canceled_numer = str(numerator)
		if canceled_denom.endswith('0') and canceled_numer.endswith('0'):
			continue
		did_cancel = False
		for i in range(len(canceled_denom)):
			c1 = canceled_denom[i]
			for j in range(len(canceled_numer)):
				c2 = canceled_numer[j]
				if c1 == c2:
					canceled_denom = replace_once(canceled_denom, c1, ' ')
					canceled_numer = replace_once(canceled_numer, c1, ' ')
					did_cancel = True
					break
		if canceled_numer.strip() == '' and canceled_denom.strip() == '':
			continue
		if canceled_denom.strip() == '0':
			continue
		canceled_value = float(canceled_numer) / float(canceled_denom)
		if uncanceled_value == canceled_value and did_cancel:
			numerator_fin *= numerator
			denomenator_fin *= denomenator
			print(numerator, denomenator)
			print(canceled_numer, canceled_denom)
			print()

print(numerator_fin, denomenator_fin)
