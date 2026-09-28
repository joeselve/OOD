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

    
M = Queue()
F = Queue()
S = Queue()

inp = input("Enter people : ").strip()

for cha in inp:
    M.enqueue(cha)

i, n_f, n_s = 0, 0, 0
while not M.is_empty():
    i += 1
    if n_f % 3 == 0 and n_f != 0 and not F.is_empty():
        F.dequeue()
    if n_s % 2 == 0 and n_s != 0 and not S.is_empty():
        S.dequeue()

    if F.size() < 5:
        F.enqueue(M.dequeue())
        
    elif F.size() >= 5 and S.size() < 5:
        S.enqueue(M.dequeue())
    
    if not F.is_empty():
        n_f += 1
    if not S.is_empty():
        n_s += 1

    print(f"{i} {M.items()} {F.items()} {S.items()}")