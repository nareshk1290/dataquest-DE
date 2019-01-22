################ Performance Boosts of Using a B-Tree ################

## Mission 1

def brute_search():
    with open('amounts.csv') as f:
        reader = csv.reader(f)
        rows = []
        for row in reader:
            if reader.line_num in [4, 41231, 284400]:
                rows.append(row)
        return rows

def cache_search():
    return list(csv.reader(linecache.getline('amounts.csv', i) for i in [4, 41231, 284400]))

print(timeit.timeit('brute_search()', 'from __main__ import brute_search', number=50))
print(timeit.timeit('cache_search()', 'from __main__ import cache_search', number=50))

brute = brute_search()
cache = cache_search()

## Mission 2

class Node:
    def __init__(self, keys=None, children=None):
        self.keys = keys or []
        self.children = children or []
        
    def is_leaf(self):
        return len(self.children) == 0

    def __repr__(self):
        return "<BNode: {}>".format(self.keys)    

class BTree:
    def __init__(self, t):
        self.t = t
        self.root = None
        
b_node = Node(keys=[1, 4, 8])
node_is_leaf = b_node.is_leaf()
btree = BTree(3)
btree.root = b_node
keys = btree.root.keys

## Mission 3

class Node:
    def __init__(self, keys=None, children=None):
        self.keys = keys or []
        self.children = children or []
    
    def is_leaf(self):
        return len(self.children) == 0

    def __repr__(self):
        return "<Node: {}>".format(self.keys)    

class BTree:
    def __init__(self, t):
        self.t = t
        self.root = None

    def insert(self, key):
        self.insert_non_full(self.root, key)
    
    def insert_non_full(self, node, key):
        if node.is_leaf():
            if len(node.keys) >= 2*self.t - 1:
                return
            
            index = 0
            for k in node.keys:
                if key > k: index += 1
                else: break
            node.keys.insert(index, key)
            return
        
        index = 0
        for k in node.keys:
            if key > k: index += 1
            else: break
        self.insert_non_full(node.children[index], key)
            
btree = BTree(4)
b_node = Node(keys=[8, 16])
b_node.children.append(Node(keys=[2, 3, 5, 7]))
b_node.children.append(Node(keys=[9, 10, 11, 12]))
b_node.children.append(Node(keys=[17, 20, 44]))
btree.root = b_node
btree.insert(1)
btree.insert(4)
btree.insert(6)
btree.insert(-1)
btree.insert(13)
btree.insert(22)
child_keys = btree.root.children[1].keys

## Mission 4

class BTree(BaseBTree):
    def insert_non_full(self, node, key):
        if node.is_leaf():
            index = 0
            for k in node.keys:
                if key > k: index += 1
                else: break
            node.keys.insert(index, key)
            return
        
        index = 0
        for k in node.keys:
            if key > k: index += 1
            else: break
                
        if len(node.children[index].keys) == 2*self.t - 1:
            left_node, right_node, new_key = self.split(node.children[index])
            node.keys.insert(index, new_key)
            node.children[index] = left_node
            node.children.insert(index+1, right_node)
            if key > new_key:
                index += 1
            
        self.insert_non_full(node.children[index], key)
    
    def split(self, node):
        left_node = Node(
            keys=node.keys[:len(node.keys)//2],
            children=node.children[:len(node.children)//2+1]
        )
        right_node = Node(
            keys=node.keys[len(node.keys)//2:],
            children=node.children[len(node.children)//2:]
        )
        key = right_node.keys.pop(0)
        return left_node, right_node, key
            

btree = BTree(4)
b_node = Node(keys=[8, 18])
b_node.children.append(Node(keys=[-3, -2, -1, 2, 3, 5, 7]))
b_node.children.append(Node(keys=[9, 10, 11, 12, 14, 18, ]))
b_node.children.append(Node(keys=[17, 20, 44]))
btree.root = b_node
btree.insert(1)
btree.insert(4)
btree.insert(6)
btree.insert(13)
btree.insert(17)
btree.insert(22)
child_keys = btree.root.children[1].keys

## Mission 5

class BTree(BaseBTree):
    def insert_multiple(self, keys):
        for key in keys:
            self.insert(key)
        
    def insert(self, key):
        if not self.root:
            self.root = Node(keys=[key])
            return
        
        if len(self.root.keys) == 2*self.t - 1:
            old_root = self.root
            self.root = Node()
            left, right, new_key = self.split(old_root)
            self.root.keys.append(new_key)
            self.root.children.append(left)
            self.root.children.append(right)
            
        self.insert_non_full(self.root, key)
            

btree = BTree(5)
btree.insert_multiple(btree_keys)
child_keys = btree.root.children[-1].children[0].keys

## Mission 7

class BTree(BaseBTree):
    def search(self, node, term):
        if not self.root:
            return False
        index = 0
        for key in node.keys:
            if key == term:
                return True
            if term > key:
                index += 1
        if node.is_leaf():
            return False
        
        return self.search(node.children[index], term)

btree = BTree(5)
btree.insert_multiple(btree_keys)
search_6 = btree.search(btree.root, 6)
search_73 = btree.search(btree.root, 73)
search_101 = btree.search(btree.root, 101)
