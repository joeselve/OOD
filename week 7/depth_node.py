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

    def findDepth(self, node, key, depth = 0):
        # Code Here
        # not found return -1
        if node is None:
            return -1
        if node.data == key:
            return depth
        elif key < node.data:
            depth += 1
            return self.findDepth(node.left, key, depth)
        else:
            depth += 1
            return self.findDepth(node.right, key, depth)

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
values = inp[:-1]
key = inp[-1]

for i in values:
    root = T.insert(T.root,i)
T.printTree(root)
print('-' * 50)
print(f"Depth of {key} : {T.findDepth(root, key)}")