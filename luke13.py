#!/usr/bin/python

import numpy as np
from timeit import default_timer

lights, answer = np.zeros(shape=(10000, 10000)), 0

start_time = default_timer()
with open('luke13file') as file:
    for line in file:
        line = line.rsplit(' ', 3)
        fromX, fromY = int(line[1].split(',')[0]), int(line[1].split(',')[1])
        toX, toY = int(line[3].split(',')[0]), int(line[3].split(',')[1])

        for a in range(fromX, toX+1):
            for b in range(fromY, toY+1):
                if 'toggle' in line[0]:
                    lights[a][b] = 1 if lights[a][b] == 0 else 0
                else:
                    lights[a][b] = 1 if 'turn on' in line[0] else 0

for a in range(10000):
    answer += np.sum(lights[a])
elapsed = default_timer() - start_time
print(elapsed.__round__(2))
print(int(answer))