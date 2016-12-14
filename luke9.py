#!/usr/bin/python


balance = {}
def transactions():                         # Generator function
    with open('luke9file') as file:
        for line in file:
            yield line.split(',')

for line in transactions():
    if line[0] not in balance:
        balance[line[0]] = 0
    if line[1] not in balance:
        balance[line[1]] = 0
    if 'None' in line[0]:                   # Case 1: Money is generated
        balance[line[1]] += int(line[2])
    else:                                   # Case 2: Money is sent from A to B
        balance[line[0]] -= int(line[2])
        balance[line[1]] += int(line[2])

# List comprehension alternative
print('Solution: ', len([x for x in balance.values() if x > 10]))

# Generator expression alternative
#for a, b in enumerate((x for x in balance.values() if x > 10)):
#    pass
#print('Solution: ', a+1)





