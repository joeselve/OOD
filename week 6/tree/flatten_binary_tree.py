class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)
        
class Tree:
    def __init__(self):
        self.root = None
        
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return self.root
        
        node = Node(data)
        q = [self.root]
        while(q):
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
                
    def flatten(self, root, result = None):
        if result == None:
            result = []
        
        if root is None or root.data == "null":
            return result
        
        result.append(root)
        self.flatten(root.left, result)
        self.flatten(root.right,result)
        
        return result
    
    def rearrange(self, root, result):
        if not result:
            return
        if len(result) >= 2:
            if result[0].data == self.root.data:
                now = result.pop(0)
        next = result.pop(0)
        root.left = None
        root.right = next
            
        self.rearrange(next, result)
            
        return self.root
            
        
    
    def printTree(self, node, level = 0):
        if node is not None:
            self.printTree(node.right, level + 1)
            if node.data != "null":
                print(" " * 6 * level, node)
            self.printTree(node.left, level + 1)
        
        
T = Tree()

inp = [i for i in input("Enter Binary Tree : ").split()]

for i in inp:
    if i != "null":
        try:
            int(i)
        except ValueError:
            print("error")
            exit()
    T.insert(i)
    
print(f"Before:")
print((T.printTree(T.root)))

T.rearrange(T.root, T.flatten(T.root))

print(f"After:")
print((T.printTree(T.root)))