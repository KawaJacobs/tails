import random

class Room:
    def __init__(self, _id, size, x, y):
        self.id = _id
        self.size = size
        self.x = x
        self.y= y

ROOM_MIN_SIZE = 2
ROOM_MAX_SIZE = 3

def generate_level(size, rooms):
    l = []
    room_objects = []
    for i in range(size):
        l.append([])
        for j in range(size):
            l[i].append(" ")
    for i in range(rooms):
        room_size = random.randint(ROOM_MIN_SIZE, ROOM_MAX_SIZE)
        room_x = random.randint(0, size-room_size)
        room_y = random.randint(0, size-room_size)
        room_objects.append(Room(i, room_size, room_x, room_y))

        for k in range(room_size):
            if room_y + k < len(l):
                for j in range(room_size):
                    if room_x + j < len(l[0]):
                        if k == 0 and j == 0:
                            l[room_y+k][room_x+j]  = room_objects[i].id
                        elif l[room_y+k][room_x+j] == " ":
                            l[room_y+k][room_x+j]  = "#"
    for index, proom in enumerate(room_objects):
        if index < len(room_objects):
            for sroom in room_objects[index+1:]:
                #print(proom.id, sroom.id)
                for i in range(proom.size):
                    if proom.x + i >= sroom.x and proom.x + i <= sroom.x + sroom.size:
                        distance = 0
                        higher = "primary"
                        if proom.y < sroom.y:
                            distance = abs(proom.y - sroom.y + sroom.size)
                        else:
                            distance = abs(sroom.y - proom.y + proom.size)
                            higher = "secondary"

                        if proom.y < sroom.y:
                            for j in range(distance):
                                if sroom.y+sroom.size+j < len(l):
                                    l[proom.y+proom.size+j][proom.x+i] = "@"  
                        else:
                            for j in range(distance): 
                                if sroom.y+sroom.size+j < len(l):
                                    l[sroom.y+sroom.size+j][sroom.x+i] = "@"
                        break
            
                        
    return l

level = generate_level(18, 10)
for i in range(len(level)-1):
    for j in range(len(level[i])-1):
        print(level[i][j], end='')
    print("")

