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
    
Q = Queue()
    
inp = input("Enter Input : ").split(",")

act = []
num = []
j = 0

for i in inp:
    ac = i.split()[0]
    act.append(ac)
    if ac == "E":
        num.append(i.split()[1])

j = 0
for action in act:
    if action == "E":
        Q.enqueue(num[j])
        print(f"Add {num[j]} index is {Q.size() - 1}")
        j += 1
    elif action == "D":
        if Q.is_empty():
            print("-1")
        else:
            s = Q.dequeue()
            print(f"Pop {s} size in queue is {Q.size()}")


my_list = []
for i in range(Q.size()):
    my_list.append(Q.dequeue())
if len(my_list) == 0:
    print("Empty")
else:
    print(f"Number in Queue is :  {my_list}")
    
