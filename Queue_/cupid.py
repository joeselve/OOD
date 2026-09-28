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
    
act = {0:"Eat", 1:"Game", 2:"Learn", 3:"Movie"}
place = {0:"Res.", 1:"ClassR.", 2:"SuperM.", 3:"Home"}
    
My = Queue()
Her = Queue()

inp = input("Enter Input : ").strip().split(",")

score = 0
mq = Queue()
hq = Queue()
ma = Queue()
ha = Queue()

for i in inp:
    j = i.split()
    my = j[0]
    her = j[1]
    k = my.split(":")
    m_ac = int(k[0])
    m_lo = int(k[1])
    l = her.split(":")
    h_ac = int(l[0])
    h_lo = int(l[1])

    My.enqueue(my)
    mq.enqueue(my)
    ma.enqueue(f"{act[m_ac]}:{place[m_lo]}")
    Her.enqueue(her)
    hq.enqueue(her)
    ha.enqueue(f"{act[h_ac]}:{place[h_lo]}")

    if m_ac == h_ac and m_lo == h_lo:
        score += 4
    elif m_ac == h_ac:
        score += 1
    elif m_lo == h_lo:
        score += 2
    else:
        score -= 5

show_mq = ""
show_ma = ""
show_hq = ""
show_ha = ""

while not mq.is_empty():
    if mq.size() == 1:
        show_mq += f"{mq.dequeue()}"
        show_ma += f"{ma.dequeue()}"
        show_hq += f"{hq.dequeue()}"
        show_ha += f"{ha.dequeue()}"
    else:
        show_mq += f"{mq.dequeue()}, "
        show_ma += f"{ma.dequeue()}, "
        show_hq += f"{hq.dequeue()}, "
        show_ha += f"{ha.dequeue()}, "

print(f"My   Queue = {show_mq}")
print(f"Your Queue = {show_hq}")

print(f"My   Activity:Location = {show_ma}")
print(f"Your Activity:Location = {show_ha}")

if score >= 7:
    print(f"Yes! You're my love! : Score is {score}.")
elif score > 0:
    print(f"Umm.. It's complicated relationship! : Score is {score}.")
else:
    print(f"No! We're just friends. : Score is {score}.")