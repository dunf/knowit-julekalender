#!/usr/bin/python

# Index == roomnumber, value in index == goblins in room
roomsWithGoblins = [x for x in range(1, 101)]
warrior_graveyard, wizard_graveyard = 0, 0
warrior, priest, thief, wizard = True, True, True, True

def heroes():
    return len([x for x in (warrior, thief, wizard, priest) if x == True])

for i in range(100):
    ressurect_used = False
    while roomsWithGoblins[i] > 0 and (thief or priest or wizard or warrior):
        # Punkt 1
        if thief and roomsWithGoblins[i] > 0:
            roomsWithGoblins[i] -= 1

        # Punkt 2
        if wizard and roomsWithGoblins[i] > 0:
            roomsWithGoblins[i] = 0 if roomsWithGoblins[i] <= 10 else roomsWithGoblins[i] - 10

        # Punkt 3
        if warrior and roomsWithGoblins[i] > 0:
            roomsWithGoblins[i] -= 1

        # Punkt 4
        if priest and ressurect_used is False:
            if not warrior and warrior_graveyard == i:
                warrior = True
                ressurect_used = True
            elif not wizard and wizard_graveyard == i:
                wizard = True
                ressurect_used = True

        # Punkt 5
        if thief and not priest and not warrior and not wizard:
            break

        # Punkt 6
        if roomsWithGoblins[i] > 0 and (priest or warrior or thief or wizard):
            if roomsWithGoblins[i] >= 10 * heroes():
                if warrior:
                    warrior = False
                    warrior_graveyard = i
                elif wizard:
                    wizard = False
                    wizard_graveyard = i
                elif priest:
                    priest = False

print(sum(roomsWithGoblins) + heroes() + 17)




