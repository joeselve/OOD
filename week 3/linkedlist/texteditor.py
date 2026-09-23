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
        cursor, idx = self.find_data("|")

        new_node.next = cursor.next
        cursor.next = new_node

        if self.tail == cursor:
            self.tail = new_node

        self.size += 1

    def __str__(self):
        ans = []
        node = self.head
        while node:
            ans.append(str(node.data))
            node = node.next
        return ' '.join(ans)
    
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
    
    def right(self):
        current = self.find_data("|")[0]
        if current.next is not None:
            current.data, current.next.data = current.next.data, current.data

    def left(self):
        prev, idx = self.find_data("|")
        if idx == 0: 
            return
        previous = self.find_index(idx - 1)
        previous.data, previous.next.data = previous.next.data, previous.data

    def backspace(self):
        current, idx = self.find_data("|")
        if idx == 0:
            return
        elif idx == 1:
            self.head = current
            self.size -= 1
            return
        prev = self.find_index(idx - 2)
        prev.next = current
        if current.next is None:
            self.tail = current
        self.size -= 1

    def delete(self):
        cursor, idx = self.find_data("|")

        if cursor.next is None:
            return

        if cursor.next == self.tail:
            self.tail = cursor

        cursor.next = cursor.next.next
        self.size -= 1

L = LinkedList()

inp = input("Enter Input : ").strip().split(",")

L.add_head("|")

for act in inp:
    action = act.strip()[0]
    if len(act.strip()) > 1 and action == "I":
        word = act.strip().split()[1]
        L.append(word)
        L.right()
        
    elif action == "R":
        L.right()
        
    elif action == "L":
        L.left()
       
    elif action == "B":
        L.backspace()
       
    elif action == "D":
        L.delete()
       
print(L.__str__())