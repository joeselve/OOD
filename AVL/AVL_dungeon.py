class AVLNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.height = 0
        self.setHeight() # คํานวณครั้งแรกจากลูก
    def getHeight(self, node):
    # หัวใจของทุกอย่าง : NULL มี height = -1
        return -1 if node is None else node.height
    def setHeight(self):
    # คํานวณ height ของตัวเองใหม่จากลูกทั)งสอง -- O(1)
        self.height = 1 + max(self.getHeight(self.left),
        self.getHeight(self.right))
        return self.height
    def balanceValue(self):
    # BF = h(ซ้าย) - h(ขวา) -> + หนักซ้าย / - หนักขวา
        return self.getHeight(self.left) - self.getHeight(self.right)
    
class AVL:
    def __init__(self):
        self.root = None
        self.my_list = []
        self.node = 0
        
    def search(root, key):
        while root is not None: # วนลูป ไม่กิน stack
            if key == root.data: return root
            root = root.left if key < root.data \
            else root.right
        return None
    
    def rotateWithLeftChild(self, x):
        # ยกลูกซ้ายขึ*นแทน x -- ใช้กับ Case 1 (LL)
        y = x.left
        x.left = y.right # T2 ย้ายมาเป็นลูกซ้ายของ x
        y.right = x # x ลงมาเป็นลูกขวาของ y
        x.setHeight() # x ก่อนเสมอ !
        y.setHeight()
        return y # y = root ใหม่ของ subtre
    
    def rotateWithRightChild(self, x):
        # ยกลูกขวาขึ*นแทน x -- ใช้กับ Case 3 (RR)
        y = x.right
        x.right = y.left
        y.left = x
        x.setHeight()
        y.setHeight()
        return y
    
    def doubleWithLeftChild(self, x): # Case 2 (LR)
        x.left = self.rotateWithRightChild(x.left)
        return self.rotateWithLeftChild(x)

    def doubleWithRightChild(self, x): # Case 4 (RL)
        x.right = self.rotateWithLeftChild(x.right)
        return self.rotateWithRightChild(x)

    def rebalance(self, x):
        if x is None:
            return x
        x.setHeight() # อัปเดต height ก่อนอ่าน BF
        bf = x.balanceValue() # bf = h(ซ้าย) - h(ขวา)
        if bf == 2: # หนักซ้าย
            if x.left.balanceValue() < 0: # หักศอก (LR)
                x = self.doubleWithLeftChild(x) # Case 2
            else: # เส้นตรง (LL)
                x = self.rotateWithLeftChild(x) # Case 1
        elif bf == -2: # หนักขวา
            if x.right.balanceValue() > 0: # หักศอก (RL)
                x = self.doubleWithRightChild(x) # Case 4
            else: # เส้นตรง (RR)
                x = self.rotateWithRightChild(x) # Case 3
        x.setHeight()
        return x
    
    def add(self, data):
        self.root = self._add(self.root, data) # อย่าลืมรับค่ากลับ!
    def _add(self, root, data):
        # --- ขาลง : หาทีDว่าง ---
        if root is None:
            return AVLNode(data) # เจอทีDว่าง -> สร้าง leaf ใหม่
        if data < root.data:
            root.left = self._add(root.left, data)
        else: # data >= root.data -> ไปขวา
            root.right = self._add(root.right, data)
        # --- ขากลับ : ซ่อมทุก node ทีDผ่านมา ---
        return self.rebalance(root)
    
    def inorder(self, m_list, root):
        if root:
            self.inorder(m_list, root.left)
            m_list.append(root)
            self.inorder(m_list, root.right)
    
    def print_tree(self, node, level = 0):
        if not node:
            return
        self.print_tree(node.right, level + 1)
        print("    " * level + str(node.data))
        self.print_tree(node.left, level + 1)
        
    def check_leaf(self, node):
        if (node.left is None) and (node.right is None):
            return True
        return False
        
    def enter_dungeon(self, node, health):
        if node:
            health -= node.data
            if health >= 0:
                self.node += 1
            self.my_list.append(node.data)
            if self.check_leaf(node):
                return health
            if node.left != None:
                return self.enter_dungeon(node.left, health)
            elif node.right != None:
                return self.enter_dungeon(node.right, health)
        else:
            return False
            
A = AVL()

inp = [i for i in input("Enter Input : ").strip().split("/")]
route = [int(i) for i in inp[0].split()]
hp = int(inp[1])

if len(route) <= 0:
    print("EMPTY DUNGEON!")
    exit()

for i in route:
    A.add(i)
    
survive = A.enter_dungeon(A.root, hp)

if survive < 0:
    print("GAME OVER!")
    print(f"Died Node : {A.node}")
    print(f"HP at death : {survive}")
    print(f"Path : {' -> '.join(map(str, A.my_list))}")
else:
    print("SUCCESS!")
    print(f"Remaining HP : {survive}")
    print(f"Path : {' -> '.join(map(str, A.my_list))}")
