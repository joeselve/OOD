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
    
    def insert(self, root, data):
        if root is None:
            node = Node(data)
            if self.root is None:
                self.root = node
            return node
        if data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)
        return root
    
    def findDepth(self, root, key):
        if root is None:
            return -1
        
        if root.data == key:
            return 0
        elif key < root.data:
            subtree = self.findDepth(root.left, key)
        else:
            subtree = self.findDepth(root.right, key)
        return subtree + 1 if subtree != -1 else -1
            
    def printTree(self, root, level = 0):
        if root != None:
            self.printTree(root.right, level + 1)
            print('     ' * level, root)
            self.printTree(root.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
values = inp[:-1]
key = inp[-1]

for i in values:
    root = T.insert(T.root, i)
T.printTree(root)
print('-' * 50)
print(f"Depth of {key} : {T.findDepth(root, key)}")