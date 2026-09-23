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
        if self.root is None:
            self.root = Node(data)
            return self.root
            
        node = Node(data)
        
        q = [self.root]
        while q:
            n = q.pop(0)
            if n.left is None:
                n.left = node
                return self.root
            else:
                q.append(n.left)
            if n.right is None:
                n.right = node
                return self.root
            else:
                q.append(n.right)

    def check_BST(self, node, min_val = float("-inf"), max_val = float("inf")):
        if node is None or node.data == "null":
            return True
        if int(node.data) >= max_val or int(node.data) <= min_val:
            return False
        return (self.check_BST(node.left, min_val, int(node.data))) and (self.check_BST(node.right, int(node.data), max_val))

    def go_all_node(self):
        if self.check_BST(self.root):
            return "This is valid binary search tree."
        return "This isn't valid binary search tree."

def printing(root, dep: int = 0) -> None:
    if(not root): return
    printing(root.right, dep+1)
    if root.data != "null":
        print(f"{' '*6*dep}{root.data}")
    printing(root.left, dep+1)

T = BST()

inp = [i for i in input('Enter data stream : ').split()]

for i in inp:
    if i != "null":
        try:
            int(i)
        except ValueError:
            print("error")
            exit()
    T.insert(i)
    
printing(T.root)
print()
    
print(T.go_all_node())