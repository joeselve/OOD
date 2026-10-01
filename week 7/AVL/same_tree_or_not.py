class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 0
        self.setHeight()
        
    def getHeight(self, node):
        return -1 if node is None else node.height
    
    def setHeight(self):
        self.height = 1 + max(self.getHeight(self.left), self.getHeight(self.right))
        return self.height
    
    def balanceValue(self):
        return self.getHeight(self.left) - self.getHeight(self.right)
    
    def __str__(self):
        return str(self.data)
        
class AVL:
    def __init__(self):
        self.root = None
        
    def rotateWithLeftChild(self, node):
        temp = node.left
        node.left = temp.right
        temp.right = node
        
        node.setHeight()
        temp.setHeight()
        
        return temp
    
    def rotateWithRightChild(self, node):
        temp = node.right
        node.right = temp.left
        temp.left = node
        
        node.setHeight()
        temp.setHeight()
                
        return temp
    
    def doubleRotateWithLeftChild(self, node):
        node.left = self.rotateWithRightChild(node.left)
        return self.rotateWithLeftChild(node)
    
    def doubleRotateWithRightChild(self, node):
        node.right = self.rotateWithLeftChild(node.right)
        return self.rotateWithRightChild(node)
    
    def rebalance(self, node):
        if node is None:
            return node
        node.setHeight()
        bf = node.balanceValue()
        
        if bf == 2:
            if node.left.balanceValue() < 0:
                node = self.doubleRotateWithLeftChild(node)
            else:
                node = self.rotateWithLeftChild(node)
        elif bf == -2:
            if node.right.balanceValue() > 0:
                node = self.doubleRotateWithRightChild(node)
            else:
                node = self.rotateWithRightChild(node)
                
        node.setHeight()
        
        return node
    
    def insert(self, node, data):
        if node is None:
            return Node(data)
            
        if data < node.data:
            node.left = self.insert(node.left, data)
        else:
            node.right = self.insert(node.right, data)
            
        return self.rebalance(node)
    
    def inorder(self, node, result = None):
        if result is None:
            result = []
        if node is not None:
            result.append(node.data)
            self.inorder(node.left, result)
            self.inorder(node.right, result)
            
            return result
            
    def printTree(self, node, level = 0):
        if node is not None:
            self.printTree(node.right, level + 1)
            print(" " * 6 * level, node)
            self.printTree(node.left, level + 1)
            
def checkSameTree(Tree1, Tree2):
    Tree1_list = Tree1.inorder(Tree1.root)
    Tree2_list = Tree2.inorder(Tree2.root)
    
    if Tree1_list is not None and Tree2_list is not None:
        if len(Tree1_list) != len(Tree2_list):
            return False
        else:
            for i in range(len(Tree1_list)):
                if Tree1_list[i] != Tree2_list[i]:
                    return False
            return True
    return True
            
Tree1 = AVL()
Tree2 = AVL()

Tree1_inp, Tree2_inp = input("Enter Tree1/Tree2 : ").split("/")

Tree1_inp = Tree1_inp.split()
Tree2_inp = Tree2_inp.split()

for i in Tree1_inp:
    Tree1.root = Tree1.insert(Tree1.root, int(i))
for i in Tree2_inp:
    Tree2.root = Tree2.insert(Tree2.root, int(i))

print("Tree 1")  
Tree1.printTree(Tree1.root)
print()
print("Tree 2")
Tree2.printTree(Tree2.root)

print()

if checkSameTree(Tree1, Tree2):
    print("Same Tree")
else:
    print("Different Tree")


