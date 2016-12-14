#!/usr/bin/python

directions = []
with open('luke7file') as file:
    for line in file:
        line = line.split(' ')
        directions.append((int(line[1]), line[3]))


class Dude(object):
    def __init__(self):
        self.x = 0
        self.y = 0

    def move(self, length, direction):
        if 'east' in direction:
            self.x -= length
        elif 'west' in direction:
            self.x += length
        elif 'north' in direction:
            self.y += length
        else:
            self.y -= length


if __name__ == '__main__':
    julenisse = Dude()
    for length, direction in directions:
        julenisse.move(length, direction)
    print('{}, {}'.format(julenisse.y, julenisse.x))