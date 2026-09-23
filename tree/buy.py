class BST:
    class TreeNode:
        def __init__(self, val):
            self.data = val
            self.left = self.right = None

    def __init__(self):
        self.root = None
        
    def find_middle(self, datas):
        if (len(datas) % 2) != 0:
            middle = (len(datas)//2)
        else:
            middle = (len(datas)//2) - 1
        
        if len(datas) != 0:
            middle_char = datas.pop(middle)
            return middle, middle_char, datas
        else:
            return

    def load_from_inorder(self, datas: list) -> None:
        if not datas:
            return
        index, start, new_list = self.find_middle(datas)
        
        self.insert(self.root, start)
        
        left_list = new_list[:index]
        right_list = new_list[index:]
        
        self.load_from_inorder(left_list) 
        self.load_from_inorder(right_list)
        
    def insert(self, root, data):
        if root is None:
            node = self.TreeNode(data)
            if self.root is None:
                self.root = node
            return node
        if data <= root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)
        return root

    def display(self) -> None:
        self._display(self.root, 0)
        
    def _display(self, node: TreeNode, dep: int) -> None:
        if(not node): return
        self._display(node.right, dep+1)
        print(f"{' '*6*dep}{node.data}")
        self._display(node.left, dep+1)
        
T = BST()        

inp = [int(i) for i in input('Enter data stream : ').split()]

T.load_from_inorder(inp)

T.display()