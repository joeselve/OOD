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
        self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def __str__(self):
        ans = []
        node = self.head
        while node:
            ans.append(str(node.data))
            node = node.next
        return '->'.join(ans)
    
    def find(self, index):
        i = 0
        current = self.head
        if index == 0:
            return self.head
        else:
            while current is not None:
                if i == index - 1:
                    found = current
                    nex = found.next
                    break
                current = current.next
                i += 1
    
def check(link_list):
    swapped = True
    while swapped:
        swapped = False
        current = link_list.head
        while current.next is not None:
            if current.data > current.next.data:
                print("")
                print(f"Swapping {current.data} and {current.next.data}")
                current.data, current.next.data = current.next.data, current.data
                swapped = True
                print(f"List: {link_list.__str__()}")
            current = current.next
    print("_______________________________________")
    print(f"Sorted List: {link_list.__str__()}")
        

    


L = LinkedList()

print("*****Bubble Sort Linked List*****")
inp = input("Enter Input: ").strip().split(",")

i = 0
for num in inp:
    number = int(num)
    if i == 0:
        L.add_head(number)
    else:
        L.append(number)
    i += 1

print(f"Input List: {L.__str__()}")
print("_______________________________________")

check(L)


    
