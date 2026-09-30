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
        
    def unload(self, lis):
        if not lis:
            return
        mid_c, mid_i, new_list = self.findMiddle(lis)
        print(mid_c, mid_i, new_list)
        
        self.insert(self.root, mid_c)
        
        left = new_list[:mid_i]
        right = new_list[mid_i:]
        
        self.unload(left)
        self.unload(right)
        
        
    def findMiddle(self, lis):
        if len(lis) % 2 == 0:
            index = len(lis) // 2 - 1
        else:
            index =  len(lis) // 2
            
        if len(lis) != 0:
            mid_c = lis.pop(index)
            return mid_c, index, lis
        else:
            return
        
    def insert(self, node, data):
        if node is None:
            n = Node(data)
            if self.root is None:
                self.root = n
            return n
        
        if data <= node.data:
            node.left = self.insert(node.left, data)
        else:
            node.right = self.insert(node.right, data)
        
        return node
    
    def printTree(self, node, level = 0):
        if node is not None:
            self.printTree(node.right, level + 1)
            print(" " * 6 * level, node)
            self.printTree(node.left, level + 1)
        
T = BST()       

inp = [int(i) for i in input("Enter data stream : ").split()]

T.unload(inp)
T.printTree(T.root)