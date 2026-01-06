import random, os

class Room:
    def __init__(self, _id, size, x, y):
        self.id = _id
        self.size = size
        self.x = x
        self.y= y

class Entity:
    def __init__(self, x, y, symbol, items, health, attack, magic):
        self.x = x
        self.y = y
        self.symbol = symbol
        self.items = items
        self.health = health
        self.attack = attack
        self.magic = magic
    def attack(self):
        pass
    
class Player(Entity):
    def __init__(self, x, y, symbol, items, health, attack, magic):
        super().__init__(x, y, symbol, items, health, attack, magic)

ROOM_MIN_SIZE = 2
ROOM_MAX_SIZE = 3

def generate_level(size, rooms, enemies):
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
                        #if k == 0 and j == 0:
                        #    l[room_y+k][room_x+j]  = room_objects[i].id
                        #elif l[room_y+k][room_x+j] == " ":
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
                                if sroom.y+sroom.size+j < len(l) and l[proom.y+proom.size+j][proom.x+i] == " ":
                                    l[proom.y+proom.size+j][proom.x+i] = "#"  
                        else:
                            for j in range(distance): 
                                if sroom.y+sroom.size+j < len(l)  and l[sroom.y+sroom.size+j][sroom.x+i] == " ":
                                    l[sroom.y+sroom.size+j][sroom.x+i] = "#"
                        break
                for i in range(proom.size):
                    if proom.y + i >= sroom.y and proom.y + i <= sroom.y + sroom.size:
                        distance = 0
                        higher = "primary"
                        if proom.x < sroom.x:
                            distance = abs(proom.x - sroom.x + sroom.size)+1
                        else:
                            distance = abs(sroom.x - proom.x + proom.size)+1
                            higher = "secondary"
                        #print("[", proom.id, proom.x, "][", sroom.id, sroom.x,"] distance: ", distance)
                        if proom.x > sroom.x:
                            for j in range(distance):
                                if sroom.x+sroom.size+j < len(l[0]) and l[sroom.y+i][sroom.x+sroom.size+j] == " ":
                                    l[sroom.y+i][sroom.x+sroom.size+j] = "#"  
                        else:
                            for j in range(distance): 
                                if proom.x+proom.size+j < len(l[0]) and l[proom.y+i][proom.x+proom.size+j] == " ":
                                    l[proom.y+i][proom.x+proom.size+j] = "#" 
                        break 
    start_pos = (0,0)
    while True:                
        y = random.randint(0, len(l)-1)
        x = random.randint(0, len(l[0])-1)
        if l[y][x] == "#":
            start_pos = (x,y)
            break
    for i in range(enemies):
        while True:                
            y = random.randint(0, len(l)-1)
            x = random.randint(0, len(l[0])-1)
            if l[y][x] == "#":
                l[y][x] = "&"
                enemies.append(Entity(x, y, "&", [], random.randint(1,10), random.randint(1,10), random.randint(1,10)))
    return l, start_pos, enemies

def print_map():
    for i in range(len(level)-1):
        for j in range(len(level[i])-1):
            print(level[i][j], end='')
        print("")

level, start_pos = generate_level(18, 10, 2)
player = Player(start_pos[0], start_pos[1], "@", [], random.randint(1,10), random.randint(1,10), random.randint(1,10))
level[player.y][player.x] = player.symbol



while True:
    os.system("clear")
    print_map()
    #try:
    #    print(level[player.y-1][player.x-1], end="")
    #    print(level[player.y-1][player.x], end="")
    #    print(level[player.y-1][player.x+1])
#
 #       print(level[player.y][player.x-1], end="")
  #      print(level[player.y][player.x], end="")
    #    print(level[player.y][player.x+1])

    #    print(level[player.y+1][player.x-1], end="")
     #   print(level[player.y+1][player.x], end="")
      #  print(level[player.y+1][player.x+1])
    #except:
    #    pass

    user_input = input("> ")
    if user_input == "w" and player.y != 0 and level[player.y-1][player.x] != " ":
        level[player.y][player.x] = "#"
        player.y -= 1
        level[player.y][player.x] = "@"
    elif user_input == "s" and player.y != len(level)-1 and level[player.y+1][player.x] != " ":
        level[player.y][player.x] = "#"
        player.y += 1
        level[player.y][player.x] = "@"
    elif user_input == "a" and player.x != 0 and level[player.y][player.x-1] != " ":   
        level[player.y][player.x] = "#"
        player.x -= 1
        level[player.y][player.x] = "@"
    elif user_input == "d" and player.x != len(level[0])-1 and level[player.y][player.x+1] != " ": 
        level[player.y][player.x] = "#"
        player.x += 1
        level[player.y][player.x] = "@"
    elif user_input == "q":
        break





















