#!/usr/bin/python

candidates = []
for var in range(100000, 500000):
    sum = 0
    for n in str(var):
        sum += int(n)
    if sum == 43:
        candidates.append(var)
[print(cnd) for cnd in candidates if int(round(cnd**(1/2)))**2 == cnd]

