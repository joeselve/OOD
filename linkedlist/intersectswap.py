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
    
    def find(self, index):
        current = self.head
        i = 0

        while current is not None:
            if i == index:
                return current
            current = current.next
            i += 1

        return None

L = LinkedList()

inp = input("Enter edges: ").strip().split(",")

next_node = {}
nodes = set()

for item in inp:
    a, b = map(int, item.split(">"))
    next_node[a] = b
    nodes.add(a)
    nodes.add(b)

pointed = set(next_node.values())

head = sorted(nodes - pointed)

old_head = head.copy()

count = {}
for x in next_node.values():
    count[x] = count.get(x, 0) + 1

duplicate = []

for node, c in count.items():
    if c > 1:
        duplicate.append(node)

duplicate.sort()

if len(duplicate) == 0:
    print("No intersection")
else:
    for start in duplicate:
        current = start
        visited = set()
        size = 0

        while current not in visited and current is not None:
            visited.add(current)
            size += 1
            current = next_node.get(current)
        print(f"Node({start}, size={size})")

    print("Delete intersection then swap merge:")

    children = {}

    for d in duplicate:
        if d in next_node:
            children[d] = next_node[d]
            

    for k in list(next_node):
        if next_node[k] in duplicate:
            del next_node[k]

    for node in duplicate:
        if node in next_node:
            del next_node[node]

    pointed = set(next_node.values())

    # เอา head เดิมก่อนลบ
    head = []

    # ใช้ head เดิม
    for h in old_head:
        if h not in duplicate and h not in head:
            head.append(h)

    # เพิ่มลูกของ intersection
    for child in children.values():
        if child not in duplicate and child not in head:
            head.append(child)

    head.sort()

    lists = []

    for h in head:
        ll = LinkedList()
        current = h

        while current is not None:
            ll.append(current)
            current = next_node.get(current)
        
        lists.append(ll)

    i = 0
    while True:
        found = False

        for ll in lists:
            node = ll.find(i)

            if node is not None:
                L.append(node.data)
                found = True

        if not found:
            break
        i += 1

    print(L.__str__())