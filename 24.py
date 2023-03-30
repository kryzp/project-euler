import itertools as it
perms = sorted(list(it.permutations(range(10))))
print("".join([str(n) for n in perms[999_999]]))
