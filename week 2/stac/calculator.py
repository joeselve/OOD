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
    
class StackCalc():
    def __init__(self):
        self.__s = Stack()
        self.__error = 0
    def run(self, instruction):
        my_list = instruction.split()
        for arg in my_list:
            if arg.isnumeric():
                arg = int(arg)
                self.__s.push(arg)
            elif arg == "+":
                i = self.__s.pop()
                j = self.__s.pop()
                k = i + j
                self.__s.push(k)
            elif arg == "-":
                i = self.__s.pop()
                j = self.__s.pop()
                k = i - j
                self.__s.push(k)
            elif arg == "*":
                i = self.__s.pop()
                j = self.__s.pop()
                k = i * j
                self.__s.push(k)
            elif arg == "/":
                i = self.__s.pop()
                j = self.__s.pop()
                k = i / j
                self.__s.push(k)
            elif arg == "DUP":
                i = self.__s.peek()
                self.__s.push(i)
            elif arg == "POP":
                self.__s.pop()
            else:
                print(f"Invalid instruction: {arg}")
                self.__error = 1
                break
    def getValue(self):
        if self.__s.is_empty() and self.__error == 0:
            return 0
        else:
            return int(self.__s.pop())
        
print("* Stack Calculator *")
arg = input("Enter arguments : ")
machine = StackCalc()
machine.run(arg)
print(machine.getValue())