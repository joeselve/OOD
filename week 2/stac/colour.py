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
    
inp = input('Enter Input : ').split()

S = Stack()

combo = 0

stack = []
for char in inp[:]:
    S.push(char)
    stack.append(char)
    if len(stack) >= 3:
        if stack[-1] == stack[-2] == stack[-3]:
            combo += 1
            for i in range(3):
                stack.pop()
                S.pop()
            
print(S.size())

string = ""
while not S.is_empty():
    string += S.pop()

if len(string) != 0:
    print(string)
else:
    print("Empty")

if combo > 1:
    print(f"Combo : {combo} ! ! !")
