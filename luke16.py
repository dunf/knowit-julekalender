#!/usr/bin/python

candidates = []

for var in range(100000, 500000):
    a = str(var)
    sum = 0
    for n in a:
        sum += int(n)
    if sum == 43:
        candidates.append(var)

for cnd in candidates:
    x = cnd**(1/2)
    x = int(round(x))
    if x**2 == cnd:
        print(cnd)

