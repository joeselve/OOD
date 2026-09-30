class LinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
        
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.size = 0
    
    def add_head(self, data):
        new_node = self.Node(data)
        new_node.next = self.head
        self.head = new_node
        if self.tail == None:
            self.tail = new_node
        self.size += 1
        
    def append(self, data):
        new_node = self.Node(data)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1

    def __str__(self):
        ans = []
        node = self.head
        while node:
            ans.append(str(node.data))
            node = node.next
        return ' -> '.join(ans)
    
    def find_index(self, index):
        current = self.head
        i = 0

        while current is not None:
            if i == index:
                return current
            current = current.next
            i += 1

        return None
    
    def find_data(self, data):
        current = self.head
        i = 0
        while current is not None:
            if current.data == data:
                return current, i
            current = current.next
            i += 1
        return None
    
    def reverse(self):
        old_head = self.head
        prev = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
        self.tail = old_head
    
BL = LinkedList()
AL = LinkedList()

inp = input("Enter Input : ").strip().split()

for num in inp:
    BL.append(num) 

max_val = max(abs(int(x)) for x in inp)
longest = len(str(max_val)) if max_val > 0 else 0
count = 0
for i in range(longest - 1, -1 ,-1):
    bucket = {j: [] for j in range(10)}
    for num in inp:
        abs_num = str(abs(int(num))).zfill(longest)
        digit = int(abs_num[i])
        bucket[digit].append(num)

    print("-" * 60)
    print(f"Round : {longest - i}")

    for d in range(10):
        print(f"{d} :", end=" ")

        # 🌟 จุดที่แก้ไข: ปริ้นท์ตัวเลขบวกใน Bucket ก่อน เพื่อความถูกต้องของ Descending Sort
        for num in bucket[d]:
            if int(num) >= 0:
                print(num, end=" ")
        
        # 🌟 ตามด้วยปริ้นท์ตัวเลขติดลบในลำดับถัดมา
        for num in bucket[d]:
            if int(num) < 0:
                print(num, end=" ")
        print()

    new_inp = []
    # 1. ดึงตัวเลขบวกจาก 9 ลงมา 0
    for d in range(9, -1, -1):
        for num in bucket[d]:
            if int(num) >= 0:
                new_inp.append(num)
                
    # 2. ดึงตัวเลขลบจาก 0 ไป 9
    for d in range(10):
        for num in bucket[d]:
            if int(num) < 0:
                new_inp.append(num)

    inp = new_inp
    count += 1

for num in inp:
    AL.append(num)

print("------------------------------------------------------------")
print(f"{count} Time(s)")
print(f"Before Radix Sort : {BL.__str__()}")
print(f"After  Radix Sort : {AL.__str__()}")