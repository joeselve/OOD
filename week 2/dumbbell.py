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
    
    def items(self):
        return self.__stack.copy()
    
def find(num):
    side = (num - 20) / 2
    return side

def cal_all(bar):
    sum = 0
    for num in bar.items():
        sum += num
    return sum

def calculate(num, bar):
    de_bar = Stack()
    action = []
    plates = [25, 20, 15, 10, 5, 2.5, 1.25]
    num -= cal_all(bar)
    for plate in plates:
        if num >= plate:
            de_bar.push(plate)
            num -= plate

    temp = Stack()

    while not bar.is_empty():
        plate = bar.pop()
        if plate not in de_bar.items():
            action.append(f"PO:{plate}")
        else:
            temp.push(plate)

    current = temp.items()

    while not temp.is_empty():
        bar.push(temp.pop())

    for plate in de_bar.items():
        if plate not in current:
            bar.push(plate)
            action.append(f"PU:{plate}")

    if num > 0:
        return 0
    return bar, action

inp = input("Enter needed weight(s): ").split()
num_list = []
for num in inp:
    num_list.append(float(num))

bar_s = Stack()
for num in num_list:
    result, action = calculate(find(num), bar_s)
    if result == 0:
        result = False

    act = " ".join(action)

    if result == False:
        print(f"It's impossible to archive the weight you want({num})")
    elif result.is_empty():
        print(f"{act}===[]===[]===")
    else:
        print(f"{act} =>----{bar_s.items()}")


