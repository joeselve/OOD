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
    
    def doubleRotateWithLeft(self, node):
        node.left = self.rotateWithRightChild(node.left)
        return self.rotateWithLeftChild(node)
    
    def doubleRotateWithRight(self, node):
        node.right = self.rotateWithLeftChild(node.right)
        return self.rotateWithRightChild(node)
    
    def rebalance(self, node):
        if node is None:
            return node
        node.setHeight()
        bf = node.balanceValue()
        if bf == 2:
            if node.left.balanceValue() < 0:
                node = self.doubleRotateWithLeft(node)
            else:
                node = self.rotateWithLeftChild(node)
        elif bf == -2:
            if node.right.balanceValue() > 0:
                node = self.doubleRotateWithRight(node)
            else:
                node = self.rotateWithRightChild(node)
                
        node.setHeight()
        return node                
    
    def insert(self, node, data):
        if node is None:
            new_node = Node(data)
            if self.root is None:
                self.root = new_node
            return new_node
        
        if data < node.data:
            node.left = self.insert(node.left, data)
        else:
            node.right = self.insert(node.right, data)
            
        return self.rebalance(node)
    
    def inorder_generator(self, node):
        if node is not None:
            yield from self.inorder_generator(node.left)
            yield node.data
            yield from self.inorder_generator(node.right)
            
    def find_k_smallest(self, node, k):
        gen = self.inorder_generator(node)
        
        for i in range(k - 1):
            next(gen, None)
            
        return next(gen, None)
    
    def printTree(self, node, level = 0):
        if node is not None:
            self.printTree(node.right, level + 1)
            print(" " * 6 * level, node)
            self.printTree(node.left, level + 1)
    
T = AVL()    
    
inp = [i for i in input("input  N node, Data, K small : ").split(",")]
n = int(inp[0])
my_list = list(inp[1].split())
find = int(inp[2])

for i in my_list:
    T.root = T.insert(T.root, int(i))
    
T.printTree(T.root)

print(T.find_k_smallest(T.root, find))