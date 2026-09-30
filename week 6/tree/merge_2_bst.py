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
        
    def insert(self, node, data):
        if data == "null":
            return node
        
        if node is None:
            new_node = Node(data)
            if self.root is None:
                self.root = new_node
            return new_node
        
        if data < node.data:
            node.left = self.insert(node.left, data)
        else:
            node.right = self.insert(node.right, data)
        
        return node
    
    def inorder(self, node, target):
        if node is not None and node.data != "null":
            left = self.inorder(node.left, target)
            if left is not None:
                return left
            if node.data == target.data:
                return node
            right = self.inorder(node.right, target)
            if right is not None:
               return right
            
    def merge(self, node, target):
        if not node:
            return False
        if not self.check_leaf(node):
            return False
        node.left = target.left
        node.right = target.right
        if self.check_bst(self.root):
            return True
        return False
        
    def check_leaf(self, node):
        if node.left is None and node.right is None:
            return True
        else:
            return False
    
    def check_bst(self, node, min = float("-inf"), max = float("inf")):
        if node is None or node.data == "null":
            return True
        if int(node.data) <= min or int(node.data) >= max:
            return False
        
        return (self.check_bst(node.left, min, int(node.data)) and self.check_bst(node.right, int(node.data), max))
    
    def printTree(self, node, level = 0):
        if node is not None:
            self.printTree(node.right, level + 1)
            if node.data != "null":
                print(" " * 6 * level, node)
            self.printTree(node.left, level + 1)
    
first = BST()
second = BST()

twolist = [i for i in input("Enter trees: ").split("/")]
f_inp = [i for i in twolist[0].strip(' []').split(',')]
s_inp = [i for i in twolist[1].strip(' []').split(',')]

for i in f_inp:
    if i != "null":
        try:
            first.insert(first.root, int(i))
        except ValueError:
            print("error")
            exit()
    else:
        first.insert(first.root, i)
    
for i in s_inp:
    if i != "null":
        try:
            second.insert(second.root, int(i))
        except ValueError:
            print("error")
            exit()
    else:
        second.insert(second.root, i)

print()
if first.inorder(first.root, second.root) is None:
    print("Cannot merge these trees.")
    exit()

if not first.merge(first.inorder(first.root, second.root), second.root):
    print("Cannot merge these trees.")
    exit()
else:
    print("Merged successfully:")
    first.printTree(first.root)

