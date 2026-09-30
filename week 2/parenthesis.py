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
        n = len(self.__stack) - 1
        f = self.__stack[n]
        self.__stack.pop()
        return f

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
    
def parenthesis_check():
    s = Stack()

    i = input("Enter Input : ")

    pair = {')':'(', ']':'[', '}':'{'}
    for cha in i:
        if cha in "({[":
            s.push(cha)
        elif cha in "]})":
            if s.is_empty():
                return False
                break
            top = s.pop()
            if pair[cha] != top:
                return False
        else:
            continue
    if s.is_empty():
        return True
    else:
        return False
    
if parenthesis_check():
    print("Parentheses : Matched ! ! !")
else:
    print("Parentheses : Unmatched ! ! !")