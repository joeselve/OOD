class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class BST:
    def __init__(self):
        self.root = None
        self.complete = False

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

    def check_BST(self, node, min_val = float("-inf"), max_val = float("inf")):
        if node is None or node.val == "null":
            return True
        if int(node.val) >= max_val or int(node.val) <= min_val:
            return False
        return (self.check_BST(node.left, min_val, int(node.val))) and (self.check_BST(node.right, int(node.val), max_val))

    def go_all_node(self):
        if self.check_BST(self.root):
            return True
        return False
    
    def check_leaf(self, node):
        if (node.left is None) and (node.right is None):
            return True
        return False
    
    def merge(self, node, target):
        if not node or node.val == "null":
            return None
        
        node.left = self.merge(node.left, target)
        node.right = self.merge(node.right, target)
        
        if self.check_leaf(node) and node.val == target.val:
            self.complete = True
            return target
        
        return node
        
class Solution:
    @staticmethod
    def print_tree(node, level=0):
        if not node:
            return
        Solution.print_tree(node.right, level + 1)
        print("    " * level + str(node.val))
        Solution.print_tree(node.left, level + 1)
        
F = BST()
S = BST()

inp = input("Enter trees: ").split("/")
print()
first_l = inp[0].strip().strip("[]").split(",")
second_l = inp[1].strip().strip("[]").split(",")

for i in first_l:
    F.insert(i)

for j in second_l:
    S.insert(j)

F.root = F.merge(F.root, S.root)

if not F.complete:
    print("Cannot merge these trees.")
    exit()

if F.go_all_node():
    print("Merged successfully:")
    Solution.print_tree(F.root)
else:
    print("Cannot merge these trees.")




