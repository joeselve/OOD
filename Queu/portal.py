class Queue(): #Queue Class
    def __init__(self, dequ = None):
        if dequ == None:
            self.__queue = []
        else:
            self.__queue = [dequ]

    def enqueue(self, item):
        self.__queue.append(item)
        return item

    def dequeue(self):
        f = self.__queue[0]
        self.__queue.pop(0)
        return f

    def peek(self):
        n = len(self.__queue) - 1
        return self.__queue[n]

    def is_empty(self):
        if len(self.__queue) >= 1:
            return False
        else:
            return True
    
    def size(self):
        return len(self.__queue)
    
    def items(self):
        return self.__queue.copy()
    
Q = Queue()
y = 0
start = None
end = None
found = False
    
inp = input("Enter width, height, and room: ").strip().split()

width = int(inp[0])
height = int(inp[1])
map_g = inp[2].split(",")

f_count = 0

for row in map_g:
    f_count += row.count("F")

if f_count != 1:
    print("Invalid map input.")
    exit()

if len(map_g) != height:
    print("Invalid map input.")
    exit()

for row in map_g:
    if len(row) != width:
        print("Invalid map input.")
        exit()

matrix = [[0 for _ in range(width)] for _ in range(height)]

for level in map_g:
    x = 0
    for cha in level:
        if cha == "F":
            start = (x, y)
            matrix[y][x] = "F"
            Q.enqueue((x, y))
        elif cha == "O":
            end = (x, y)
            matrix[y][x] = "O"
        elif cha == "_":
            matrix[y][x] = "_"
        else:
            matrix[y][x] = "X"
        x += 1
    y += 1

while not Q.is_empty():
    print(f"Queue: {Q.items()}")
    i = Q.dequeue()
    x, y = i[0], i[1]
    if -1 < x < width and -1 < y < height:
        if y-1 >= 0 and matrix[y - 1][x]  in ["_", "O"]:
            if matrix[y - 1][x] == "O":
                print("Found the exit portal.")
                found = True
                break
            matrix[y - 1][x] = "."
            Q.enqueue((x, y - 1))
        if x+1 < width and matrix[y][x + 1]  in ["_", "O"]:
            if matrix[y][x + 1] == "O":
                print("Found the exit portal.")
                found = True
                break
            matrix[y][x + 1] = "."
            Q.enqueue((x + 1, y))
        if y+1 < height and matrix[y + 1][x]  in ["_", "O"]:
            if matrix[y + 1][x] == "O":
                print("Found the exit portal.")
                found = True
                break
            matrix[y + 1][x] = "."
            Q.enqueue((x, y + 1))
        if x-1 >= 0 and matrix[y][x - 1]  in ["_", "O"]:
            if matrix[y][x - 1] == "O":
                print("Found the exit portal.")
                found = True
                break
            matrix[y][x - 1] = "."
            Q.enqueue((x - 1, y))

if not found:
    print("Cannot reach the exit portal.")


    
            
