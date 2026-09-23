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

    
inp = input("input : ").strip().split(",")

Q = Queue()

En = 0
De = 0
Er = 0

for arg in inp:
    print(f"Step : {arg}")

    command = arg[0]
    time = arg[1:]

    if arg[1].isnumeric():
        time = int(arg[1:])
    if command == "E":
        for i in range (time):
            Q.enqueue(f"*{En}")
            En += 1
    elif command == "D":
        for i in range (time):
            if not Q.is_empty():
                Q.dequeue()
            else:
                De += 1
    else:
        Er += 1

    if command == "E":
        print(f"Enqueue : {Q.items()}")
    elif command == "D":
        print(f"Dequeue : {Q.items()}")
    else:
        print(Q.items())

    print(f"Error Dequeue : {De}")
    print(f"Error input : {Er}")
    print("--------------------")