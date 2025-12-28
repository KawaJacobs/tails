import random

level = []

ROOM_SIZE = 4

def generate_level(size, rooms):
    l = []
    for i in range(size):
        l.append([])
        for j in range(size):
            l[i].append(" ")
    for i in range(rooms):
        l[random.randint(0, size-ROOM_SIZE)][random.randint(0, size-ROOM_SIZE)] = "#"

    return l

print(generate_level(10, 3))

