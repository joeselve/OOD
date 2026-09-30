class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
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
    
    def checkBST(self, node, min = float("-inf"), max = float("inf")):
        if node is None or node.data == "null":
            return True
        if int(node.data) >= max or int(node.data) <= min:
            return False
        
        return (self.checkBST(node.left, min, int(node.data)) and self.checkBST(node.right, int(node.data), max))
    
    def printTree(self, node, level = 0):
        if node is not None:
            self.printTree(node.right, level + 1)
            if node.data != "null":
                print('    ' * level, node.data)
            self.printTree(node.left, level + 1)
            
T = BST()

inp = [i for i in input("Enter data stream : ").split()]

for j in inp:
    if j != "null":
        try:
            int(j)
        except ValueError:
            print("error")
            exit()
    T.insert(j)
    
T.printTree(T.root)
print()
print(T.checkBST(T.root))
