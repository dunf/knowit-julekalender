#!/usr/bin/python

from collections import defaultdict
import operator

hate = {}
friends = {}
intersection = {}
chameleon = dict()

with open('luke3file') as file:
    for line in file:
        line = line.split(None, 3)
        if 'hates' in line[1]:
            if line[0] not in hate:
                hate[line[0]] = []
            hate[line[0]].append(line[2])
        else:
            if line[1] not in friends:
                friends[line[1]] = []

            if line[2] not in friends:
                friends[line[2]] = []
            friends[line[1]].append(line[2])
            friends[line[2]].append(line[1])

hater = ''
s = 0
for person in hate:
    hates = 0
    for hatee in hate[person]:
        if hatee in friends[person] and person not in hate[hatee]:
            hates += 1
    if hates > s:
        hater = person
        s = hates
print('Solution: ', hater, s)
for var in sorted(hate.items()):
    print(var)





