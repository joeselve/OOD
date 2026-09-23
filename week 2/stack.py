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
    
def f(L = []): #function with default argument
    print(L)
    L.append(1)

def parenthesis_check():
    s = Stack()

    i = input("Enter your parenthesis: ")

    pair = {')':'(', ']':'[', '}':'{'}
    for cha in i:
        if cha in "({[":
            s.push(cha)
        elif cha in "]})":
            if s.is_empty():
                return "False"
                break
            top = s.pop()
            if pair[cha] != top:
                return "False"
        else:
            continue
    if s.is_empty():
        return "True"
    else:
        return "False"
    
def postfix():
    n = Stack()
    i = input("Enter: ")

    for cha in i:
        if cha.isdigit():
            n.push(int(cha))
        elif cha in "+-*/":
            b = n.pop()
            a = n.pop()
            if cha == '+':
                n.push(a + b)
            elif cha == '-':
                n.push(a - b)
            elif cha == '*':
                n.push(a * b)
            elif cha == '/':
                n.push(a / b)
            else:
                return "Unknown operator"
    return n.pop()
        
def in_post():
    precedence = {
        '*':2,
        '/':2,
        '+':1,
        '-':1,
        '(':0
    }

    n = Stack()
    i = input("Enter :")
    post = ""

    for cha in i:
        if cha.isdigit():
            post += cha
        elif cha == "(":
            n.push(cha)
        elif cha == ")":
            while not n.is_empty() and n.peek() != "(":
                post += n.pop()
            n.pop()
        elif cha in "+-*/":
            while(not n.is_empty() and precedence[n.peek()] >= precedence[cha]):
                post += n.pop()
            n.push(cha)
        
    while not n.is_empty():
        post += n.pop()
    
    return post

print(in_post())