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
                
def find_min(root):
    my_list = []
    postorder(my_list, root)
    
    for num in my_list:
        if num.left != None or num.right != None:
            if num.left == None:
                right = num.right.val
                left = 0
            elif num.right == None:
                left = num.left.val
                right = 0
            else:
                left = num.left.val
                right = num.right.val
                
            num.val = min(left, right)
            
            if num.left != None:
                num.left.val = num.left.val - num.val
            if num.right != None:
                num.right.val = num.right.val - num.val
            
    return  sum(node.val for node in my_list)
    
def postorder(my_list, root):
    if root:
        postorder(my_list, root.left)
        postorder(my_list, root.right)
        my_list.append(root)
                
def printing(root: TreeNode, dep = 0) -> None:
    if(not root): return
    printing(root.right, dep+1)
    if root.val != "null":
        print(f"{' '*6*dep}{root.val}")
    printing(root.left, dep+1)
                
B = BST()

inp = [i for i in input("Enter Input : ").strip().split("/")]

num = [int(i) for i in inp[1].strip().split()]

for i in range(int(inp[0])//2):
    B.insert(0)
for i in num:
    B.insert(i)
    
if (int(inp[0])//2 + 1 != len(num)) or int(inp[0]) < 3 or int(inp[0]) % 2 == 0:
    print("Incorrect Input")
else:
    print(find_min(B.root))

