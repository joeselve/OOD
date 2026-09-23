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
count = {}

for char in inp[:]:
    if char not in count:
        count[char] = 0
    for cha in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        if cha == char:
            inp.remove(char)
            S.push(char)
            count[char] += 1

for i in range(S.size()):
    count = 0
        
print(S.size())

string = ""
while not S.is_empty():
    string += S.pop()

print(string)
if combo > 1:
    print(f"Combo : {combo}! ! !")