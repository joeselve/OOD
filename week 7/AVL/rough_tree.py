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
    
    def postorder(self, node, result = None):
        if result is None:
            result = []
        if node is not None:
            self.postorder(node.left, result)
            self.postorder(node.right, result)
            result.append(node)
        return result
    
    def find_min(self, node):
        if node is not None:
            if node.left is None and node.right is None:
                return 0
            elif node.left is not None and node.right is None:
                return node.left.data
            elif node.left is None and node.right is not None:
                return node.right.data
            else:
                return min(node.left.data, node.right.data)
            
    def merge(self, node):
        if node is not None and not self.checkLeaf(node):
            node.data = self.find_min(node)
            if node.left is not None:
                node.left.data -= node.data
            if node.right is not None:
                node.right.data -= node.data
                
        return node.data
    
    def checkLeaf(self, node):
        if node.left is None and node.right is None:
            return True
        else:
            return False
    
    def printTree(self, node, level = 0):
        if node is not None:
            self.printTree(node.right, level + 1)
            print(" " * 6 * level, node)
            self.printTree(node.left, level + 1)
            
Tree = AVL()

n, n_list = input("Enter Input : ").split("/")
n = int(n)
n_list = [int(i) for i in n_list.split()]

if (n // 2 + 1) != len(n_list) or n < 3 or n % 2 == 0:
    print("Incorrect Input")
    exit()

for i in range(n - len(n_list)):
    Tree.root = Tree.insert(0)

for data in n_list:
    Tree.root = Tree.insert(data)

for node in Tree.postorder(Tree.root):
    Tree.merge(node)
    
i = []
for j in Tree.postorder(Tree.root):
    i.append(j.data)

print(sum(i))