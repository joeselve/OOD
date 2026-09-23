class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if data == "null":
            data = " "
        else:
            data = int(data)
        node = Node(data)
        if not self.root:
            self.root = node
            return
        queue = [self.root]
        while queue:
            n = queue.pop(0)
            if n.left is None:
                n.left = node
                return
            else:
                queue.append(n.left)

            if n.right is None:
                n.right = node
                return
            else:
                queue.append(n.right)

    def check_BST(self, root):
        check = True
        if root.left is not None:
            if root.left.data > root.data:
                check = False
                return check
        if root.right is not None:
            if root.right.data < root.data:
                check = False
                return check
        return check

    def go_all_node(self):
        check = True
        q = [self.root]
        while q:
            n = q.pop(0)
            check = self.check_BST(n)
            if check is False:
                return "This isn't valid binary search tree."
            if n.left: q.append(n.left)
            if n.right: q.append(n.right)
        return "This is valid binary search tree."

def printing(root, dep: int = 0) -> None:
    if(not root): return
    printing(root.right, dep+1)
    print(f"{' '*6*dep}{root.data}")
    printing(root.left, dep+1)

T = BST()

inp = [i for i in input('Enter Input : ').split()]

root = T.root
for i in inp:
    T.insert(i)

printing(T.root)

print(T.go_all_node())