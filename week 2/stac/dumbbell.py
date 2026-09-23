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

def calculate(num, bar):
    de_bar = Stack()
    action = []
    plates = [25, 20, 15, 10, 5, 2.5, 1.25]

    if num == 0:
        while not bar.is_empty():
            plate = bar.pop()
            action.append(f"PO:{plate}")
        return bar, action

    # สร้างชุดแผ่นใหม่จากน้ำหนักที่ต้องการ
    remain = num

    for plate in plates:
        while remain >= plate - 1e-9:
            de_bar.push(plate)
            remain -= plate

    if abs(remain) > 1e-9:
        return 0, action

    if de_bar.size() > 5:
        return 0, action
    
    old = bar.items()
    new = de_bar.items()

    keep = 0

    # หาแผ่นที่เหมือนกันจากด้านใน
    while keep < len(old) and keep < len(new):
        if old[keep] == new[keep]:
            keep += 1
        else:
            break


    # ถอดจากด้านนอก
    for plate in reversed(old[keep:]):
        action.append(f"PO:{plate}")

    # ใส่ใหม่ทั้งหมด
    while not bar.is_empty():
        bar.pop()

    for plate in new:
        bar.push(plate)

    # เพิ่ม action เฉพาะแผ่นที่เพิ่ม
    for plate in new[keep:]:
        action.append(f"PU:{plate}")
    
    return bar, action

inp = input("Enter needed weight(s): ").split()
num_list = []
for num in inp:
    num_list.append(num)

bar_s = Stack()
for num in num_list:
    weight = float(num)
    result, action = calculate(find(weight), bar_s)
    if result == 0:
        print(f"It's impossible to achieve the weight you want({num}).")
        break

    act = " ".join(action)
    left = "".join(f"[{x}]" for x in reversed(bar_s.items()))
    right = "".join(f"[{x}]" for x in bar_s.items())
    dash = "-" * (5 - len(bar_s.items()))

    if num == "20":
        if act == "":
            print(f"-----|======|----- => 20 KG.")
        else:
            print(f"{act} => -----|======|----- => 20 KG.")
    elif any(x % 1 != 0 for x in bar_s.items()):
        print(f"{act} => {dash}{left}|======|{right}{dash} => {float(num):.1f} KG.")
    else:
        print(f"{act} => {dash}{left}|======|{right}{dash} => {float(num):.0f} KG.")