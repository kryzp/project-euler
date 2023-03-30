
MONTHS = [31 if x not in (3, 5, 8, 10) else 30 for x in range(12)]

def calc_day_count(month, year):
	if month != 1:
		return MONTHS[month]
	if (year % 4 == 0 and year % 100 == 0) or year % 400 == 0:
		return 29
	return 28

wkday = 0
sundays = 0
for year in range(1901, 2000+1):
	for month in range(len(MONTHS)):
		for day in range(calc_day_count(month, year)):
			wkday = (wkday + 1) % 7
			if wkday == 0 and day == 0:
				sundays += 1

print(sundays)
