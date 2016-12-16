#!/usr/bin/python

candidates = []
for var in range(100000, 500000):
    if sum((int(x) for x in str(var))) == 43:
        candidates.append(var)
[print(cnd) for cnd in candidates if int(round(cnd**(1/2)))**2 == cnd]
