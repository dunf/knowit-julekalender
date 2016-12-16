#!/usr/bin/python

for var in range(100000, 500000):
    if sum((int(x) for x in str(var))) == 43:
        print(var) if int(round(var**(1/2)))**2 == var or int(round(var**(1/3)))**3 == var else None
