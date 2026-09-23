class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.val}"
    
class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = TreeNode(data)
            return self.root
            
        node = TreeNode(data)
        
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

def printing(root: TreeNode, dep = 0) -> None:
    if(not root): return
    printing(root.right, dep+1)
    if root.val != "null":
        print(f"{' '*6*dep}{root.val}")
    printing(root.left, dep+1)
    
def get_preorder(node: TreeNode, node_list: list) -> None:
    if not node:
        return
    if node.val != "null":
        node_list.append(node)
    get_preorder(node.left, node_list)
    get_preorder(node.right, node_list)
    
def flatten(root: TreeNode) -> None:
    if not root:
        return
    node_list = []
    get_preorder(root, node_list)
    
    for i in range(len(node_list) - 1):
       
        node_list[i].left = None
        node_list[i].right = node_list[i + 1]
    
        node_list[-1].left = None
        node_list[-1].right = None
    
T = BST()

inp = [i for i in input("Enter Binary Tree : ").split()]

for i in inp:
    if i != "null":
        try:
            int(i)
        except ValueError:
            print("error")
            exit()
    T.insert(i)

print("Before:")
printing(T.root)
print("After:")
flatten(T.root)
printing(T.root)
