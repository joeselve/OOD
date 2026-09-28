class Stack(): #Stack Class
    def __init__(self, list = None):
        if list == None:
            self.__stack = []
        else:
            self.__stack = list

    def push(self, item):
        self.__stack.append(item)
        return item

    def pop(self):
        if self.is_empty():
            return None
        return self.__stack.pop()

    def peek(self):
        n = len(self.__stack) - 1
        return self.__stack[n]

    def is_empty(self):
        if len(self.__stack) >= 1:
            return False
        else:
            return True
    
    def size(self):
        return len(self.__stack)
    
    def copy(self):
        return Stack(self.__stack[:])
    

S = Stack()
inp = input("Enter Input : ").split(",")

for arg in inp:
    arg = arg.strip()
    if arg[0] == "A":
        i = int(arg.split()[1])
        if i < 1:
            i = 1
        S.push(i)
        
    elif arg[0] == "B":
        if S.is_empty():
            print("0")
        
        sum = 1
        temp = S.copy()
        if not temp.is_empty():
            i = temp.pop()
            while not temp.is_empty():
                j = temp.pop()
                if i < j:
                    sum += 1
                    i = j
        print(sum)

    elif arg[0] == "S":
        temp = Stack()
        while not S.is_empty():
            temp.push(S.pop())
        while not temp.is_empty():
            i = temp.pop()
            if i % 2 == 0:
                i -= 1
            else:
                i += 2
            if i < 1:
                i = 1
            S.push(i)
    else:
        print("Error")

        