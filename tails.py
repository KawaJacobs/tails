import random



ROOM_MIN_SIZE = 2
ROOM_MAX_SIZE = 3

def generate_level(size, rooms):
    l = []
    for i in range(size):
        l.append([])
        for j in range(size):
            l[i].append(" ")
    for i in range(rooms):
        room_size = random.randint(ROOM_MIN_SIZE, ROOM_MAX_SIZE)
        room_x = random.randint(0, size-room_size)
        room_y = random.randint(0, size-room_size)

        for i in range(room_size):
            if room_y + i < len(l):
                for j in range(room_size):
                    if room_x + j < len(l[0]):
                        l[room_y+i][room_x+j]  = "#"

    return l

level = generate_level(18, 10)
for i in range(len(level)-1):
    for j in range(len(level[i])-1):
        print(level[i][j], end='')
    print("")

