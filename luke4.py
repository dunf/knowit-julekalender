#!/usr/bin/python

tallrekke = []
k = 0
for var in range(1, 1337+1):
    if var % 7 == 0 or '7' in str(var):
        tallrekke.append(tallrekke[k])
        k += 1
    else:
        tallrekke.append(var)
print('Solution: ', tallrekke[1337-1])
