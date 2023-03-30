lst = 0
cur = 1
res = 0

while cur < 4_000_000:
    tmp = cur
    cur += lst
    lst = tmp
    if cur % 2 == 0:
        res += cur

print(res)
