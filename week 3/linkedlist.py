class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.__size = 0

    def __str__(self):
        current = self.head
        string = "link list : "
        string_list = ""
        my_list = []
        if self.__size == 0:
            return "List is empty"
        while current is not None:
            i = current.data
            my_list.append(str(i))
            current = current.next

        string_list = "->".join(my_list)
        string += string_list
        return string
            

    def is_empty(self):
        if self.__size == 0:
            return True
        else:
            return False
        
    def add_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        if self.tail == None:
            self.tail = new_node
        self.__size += 1
        
    def append(self, data):
        new_node = Node(data)
        self.tail.next = new_node
        self.tail = new_node

        self.__size += 1

    def insert(self, index, data):
        i = 0
        current = self.head
        if index == 0:
            self.add_head(data)
        else:
            while current is not None:
                if i == index - 1:
                    found = current
                    nex = found.next
                    break
                current = current.next
                i += 1

            new_node = Node(data)
            found.next = new_node
            new_node.next = nex


            if self.tail is found:
                self.tail = new_node
            self.__size += 1

    def check_size(self):
        return self.__size

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

L = LinkedList()

inp = input("Enter Input : ").strip().split(",")

number = inp[0]
if len(number) == 0:
    print("List is empty")
else:
    number_list = number.split()

    L.add_head(number_list[0])
    number_list.pop(0)
    for number in number_list:
        L.append(number)
    print(L.__str__())

for act in inp[1:]:
    action = act.strip().split(":")
    index = int(action[0])
    data = action[1]
    if index < 0 or index > L.check_size():
        print("Data cannot be added")
        print(L.__str__())
        continue
    print(f"index = {index} and data = {data}")
    L.insert(index, data)
    print(L.__str__())
