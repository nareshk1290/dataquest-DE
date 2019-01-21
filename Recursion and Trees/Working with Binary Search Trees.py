################ Working with Binary Search Trees ################

## Mission 1

class Node:
    def __init__(self, value=None):
        self.left = None
        self.right = None
        self.value = value
    
    def __str__(self):
        return "<Node: {}>".format(self.value)

class BST:
    def __init__(self):
        self.node = None
    
    def insert(self, value=None):
        node = Node(value=value)
        if not self.node:
            self.node = node
            self.node.right = BST()
            self.node.left = BST()
            return
        
        if value > self.node.value:
            if self.node.right:
                self.node.right.insert(value=value)
            else:
                self.node.right.node = node
            return
        
        if self.node.left:
            self.node.left.insert(value=value)
        else:
            self.node.left.node = node
            
    def inorder(self, tree):
        if not tree or not tree.node:
            return []
        return (
                self.inorder(tree.node.left) + [tree.node.value] + self.inorder(tree.node.right)
        )
    
bst = BST()
bst.insert(4)
bst.insert(2)
bst.insert(1)
bst.insert(5)
bst.insert(3)
root = bst.node.value

## Mission 2

class BST(BaseBST):
    def insert_multiple(self, values):
        for value in values:
            self.insert(value)
            
    def inorder(self, tree):
        if not tree or not tree.node:
            return []
        return (self.inorder(tree.node.left) + [tree.node.value] + self.inorder(tree.node.right))
    
bst = BST()
bst.insert_multiple(bst_values)
sorted_inorder = bst.inorder(bst)

## Mission 3

class BST(BaseBST):
    def search(self, value):
        if not self.node:
            return False
        if value == self.node.value:
            return True
        
        result = False
        if self.node.left:
            result = self.node.left.search(value)
        if self.node.right:
            result = self.node.right.search(value)
        return result
    
bst = BST()
bst.insert_multiple(bst_values)

does_exist_1 = bst.search(1)
does_exist_75 = bst.search(75)
does_exist_101 = bst.search(101)

## Mission 4

class BST(BaseBST):
    def depth(self, node):
        if not node:
            return 0
        if not node.left and not node.right:
            return 1
        
        return max(self.depth(node.left.node), self.depth(node.right.node)) + 1
    
    def is_balanced(self):
        if not self.node:
            return True
        
        left_subtree = self.depth(self.node.left.node)
        right_subtree = self.depth(self.node.right.node)
        
        return abs(left_subtree - right_subtree) < 2
    
bst = BST()
bst.insert_multiple(bst_values)
balanced = bst.is_balanced()

## Mission 5

class BST(BaseBST):
    def left_rotate(self):
        old_node = self.node
        new_node = self.node.right.node
        if not new_node:
            return
        
        new_right_sub = new_node.left.node
        self.node = new_node
        old_node.right.node = new_right_sub
        new_node.left.node = old_node
    
    def right_rotate(self):
        old_node = self.node
        new_node = self.node.left.node
        if not new_node:
            return
        
        new_left_sub = new_node.right.node
        self.node = new_node
        old_node.left.node = new_left_sub
        new_node.right.node = old_node


bst = BST()
bst.insert_multiple(bst_values)
bst.left_rotate()
left_balanced = bst.is_balanced()
bst.right_rotate()
right_balanced = bst.is_balanced()

## Mission 7

class BST(BaseBST):
    def insert(self, value=None):
        node = Node(value=value)
        if not self.node:
            self.node = node
            self.node.left = BST()
            self.node.right = BST()
            return
        
        if value > self.node.value:
            if self.node.right:
                self.node.right.insert(value=value)
            else:
                self.node.right.node = node
        else:
            if self.node.left:
                self.node.left.insert(value=value)
            else:
                self.node.left.node = node
        
        difference = self.depth(self.node.left.node) - self.depth(self.node.right.node)
        
        # Left side case.
        if difference > 1:
            # Left-right case.
            if value > self.node.right.node.value:
                self.node.left.left_rotate()
            # Left-left case.
            self.right_rotate()
            
        # Right side case.
        if difference < -1:
            # Right-left case.
            if value <= self.node.left.node.value:
                self.node.left.right_rotate()
            self.left_rotate()
    

bst = BST()
bst.insert_multiple(bst_values)
inorder = bst.inorder(bst)
is_bst_balanced = bst.is_balanced()

## Mission 8

class BST(BaseBST):
    def __init__(self, index=None):
        self.node = None
        self.index = index
    
    def insert(self, value=None):
        key = value
        if self.index:
            key = value[self.index]
        node = Node(key=key, value=value)
        
        if not self.node:
            self.node = node
            self.node.left = BST(index=self.index)
            self.node.right = BST(index=self.index)
            return
        
        if key > self.node.key:
            if self.node.right:
                self.node.right.insert(value=value)
            else:
                self.node.right.node = node
        else:
            if self.node.left:
                self.node.left.insert(value=value)
            else:
                self.node.left.node = node
        
        difference = self.depth(self.node.left.node) - self.depth(self.node.right.node)
        
        # Left side case.
        if difference > 1:
            # Left-right case.
            if key > self.node.right.node.key:
                self.node.left.left_rotate()
            # Left-left case.
            self.right_rotate()
            
        # Right side case.
        if difference < -1:
            # Right-left case.
            if key <= self.node.left.node.key:
                self.node.left.right_rotate()
            self.left_rotate()
    
    def search(self, key):
        if not self.node:
            return False
        if key == self.node.key:
            return True
        
        result = False
        if self.node.left:
            result = self.node.left.search(key)
        if self.node.right:
            result = self.node.right.search(key)
        return result

bst = BST()
bst.insert_multiple(bst_values)
inorder = bst.inorder(bst)

bst_list = BST(index=2)
bst_list.insert_multiple(bst_list_values)
inorder_list = bst.inorder(bst_list)

## Mission 9

class BST(BaseBST):
    def greater_than(self, key):
        if not self.node:
            return []
        
        values = []
        if self.node.left:
            values += self.node.left.greater_than(key)
        if self.node.right:
            values += self.node.right.greater_than(key)
        if self.node.key > key:
            values.append(self.node.value)
        return values

bst = BST()
bst.insert_multiple(bst_values)
greater = bst.greater_than(5)

bst_list = BST(index=2)
bst_list.insert_multiple(bst_list_values)
greater_list = bst_list.greater_than(5)

## Mission 10

bst = BST() 
with open('amounts.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    amount_rows = list((r[0], float(r[1])) for r in reader)
    
bst = BST(index=1)
bst.insert_multiple(amount_rows)
csv_query = bst.greater_than(10)

## Mission 11

