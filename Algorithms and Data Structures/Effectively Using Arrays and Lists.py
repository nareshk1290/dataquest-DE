################ Effectively Using Arrays and Lists ################

## Mission 2

numbers = list(range(100))
binary = [(bin(num)[2:])for num in numbers]
new_numbers = [(int(b,2)) for b in binary]

print(binary)

## Mission 4

import time
import matplotlib.pyplot as plt

times = {}
iterations = 1000
numbers = list(range(20))

for i in range(iterations):
    l = []
    start = time.time()
    l.append(i)
    end = time.time()
    if i not in times:
        times[i] = []
    times[i].append(end - start)
    
avg_times = []
for i in numbers:
    avg_times.append(sum(times[i]))

plt.bar(numbers, avg_times)

## Mission 6

sentence = "I desperately want a 1982 Winnebago."
sentence2 = sentence

values = [1,2,3,4,5]

sentence_hex = hex(id(sentence))
sentence2_hex = hex(id(sentence2))

values_elements_hex = [(hex(id(elem))) for elem in values]
values_hex = hex(id(values))

print(sentence_hex)
print(sentence2_hex)
print(values_elements_hex)
print(values_hex)

## Mission 8

import numpy as np

class Array():
    def __init__(self, size):
        self.array = np.zeros(size, dtype=np.float64)
        self.size = size
    
    def __getitem__(self, key):
        return self.array[key]
    
    def __setitem__(self, key, value):
        self.array[key] = value
        
with open("prices.csv", 'r') as f:
    data = f.readlines()
    
all_prices = [(d.split(",")[1]) for d in data][1:]
all_prices = [float(p.strip()) for p in all_prices]

prices = Array(10)

for i in range(10):
    prices[i] = all_prices[i]
	
	
## Mission 9

class Array():
    def __init__(self, size):
        self.array = np.zeros(size, dtype=np.float64)
        self.size = size
    
    def __getitem__(self, key):
        return self.array[key]
    
    def __setitem__(self, key, value):
        self.array[key] = value
        
    def insert(self, position, value):
        new_array = np.zeros(self.size + 1, dtype=np.float64)
        new_pos = 0
        for i, item in enumerate(self.array):
            if i == position:
                new_array[new_pos] = value
                new_pos += 1
            new_array[new_pos] = item
            new_pos += 1
        if position == (self.size):
            new_array[new_pos] = value
        self.size += 1
        self.array = new_array
    
    def __len__(self):
        return self.size
    
    def append(self, value):
        self.insert(self.size, value)
        
prices = Array(0)

for price in all_prices[:100]:
    prices.append(price)
    
prices.insert(50, 646.921081)

## Mission 10

class Array():
    def __init__(self, size):
        self.array = np.zeros(size, dtype=np.float64)
        self.size = size
    
    def __getitem__(self, key):
        return self.array[key]
    
    def __setitem__(self, key, value):
        self.array[key] = value
    
    def insert(self, position, value):
        new_array = np.zeros(self.size + 1, dtype=np.float64)
        new_pos = 0
        for i, item in enumerate(self.array):
            if i == position:
                new_array[new_pos] = value
                new_pos += 1
            new_array[new_pos] = item
            new_pos += 1
        if position == (self.size):
            new_array[new_pos] = value
        self.size += 1
        self.array = new_array
    
    def __len__(self):
        return self.size
    
    def append(self, value):
        self.insert(self.size, value)
        
    def pop(self, position):
        new_array = np.zeros(self.size - 1, dtype=np.float64)
        removed = None
        new_position = 0
        for i, item in enumerate(self.array):
            if i == position:
                removed = self.array[i]
                continue
            new_array[new_position] = self.array[i]
            new_position += 1
        self.array = new_array
        self.size -= 1
        return removed
    
prices = Array(0)

for price in all_prices[:100]:
    prices.append(price)
    
prices.pop(40)

## Mission 12

class Node():
    def __init__(self, value):
        self.value = value
        self.next_node = None
    
    def set_next_node(self, node):
        self.next_node = node
        
    def append(self, value):
        next_node = Node(value)
        self.next_node = next_node
        return next_node
    
price_1 = Node(all_prices[0])
node = price_1
for i in all_prices[1:5]:
    node = node.append(i)
    
current_node = price_1
while current_node.next_node is not None:
    print(current_node.value)
    current_node = current_node.next_node
print(current_node.value)

## Mission 13

class Node():
    def __init__(self, value):
        self.value = value
        self.next_node = None
    
    def set_next_node(self, node):
        self.next_node = node
    
    def append(self, value):
        next_node = Node(value)
        self.next_node = next_node
        return next_node
    
    def __getitem__(self, key):
        node = self
        counter = 0
        while counter < key:
            node = node.next_node
            counter += 1
        return node
    
price_1 = Node(all_prices[0])
node = price_1
for i in all_prices[1:5]:
    node = node.append(i)
    
print(price_1[2].value)

## Mission 14

class Node():
    def __init__(self, value):
        self.value = value
        self.next_node = None
    
    def set_next_node(self, node):
        self.next_node = node
    
    def append(self, value):
        next_node = Node(value)
        self.next_node = next_node
        return next_node
    
    def __getitem__(self, key):
        node = self
        counter = 0
        while counter < key:
            node = node.next_node
            counter += 1
        return node
    
    def insert(self, position, value):
        if position == 0:
            node = Node(value)
            node.next_node = self
            return node
        else:
            node = Node(value)
            split_start = self[position - 1]
            split_end = split_start.next_node
            split_start.next_node = node
            node.next_node = split_end
            return self
        
    
price_1 = Node(all_prices[0])
node = price_1
for i in all_prices[1:5]:
    node = node.append(i)

price_1 = price_1.insert(3, all_prices[5])
price_1 = price_1.insert(0, all_prices[6])
price_1 = price_1.insert(7, all_prices[7])

print(price_1[4].value)

## Mission 15

class Node():
    def __init__(self, value):
        self.value = value
        self.next_node = None
    
    def set_next_node(self, node):
        self.next_node = node
    
    def append(self, value):
        next_node = Node(value)
        self.next_node = next_node
        return next_node
    
    def __getitem__(self, key):
        node = self
        counter = 0
        while counter < key:
            node = node.next_node
            counter += 1
        return node
    
    def insert(self, position, value):
        if position == 0:
            node = Node(value)
            node.next_node = self
            return node
        else:
            node = Node(value)
            split_start = self[position - 1]
            split_end = split_start.next_node
            split_start.next_node = node
            node.next_node = split_end
            return self
        
    def pop(self, position):
        if position == 0:
            return self, self.next_node
        else:
            split_start = self[position - 1]
            to_remove = split_start.next_node
            split_end = to_remove.next_node
            split_start.next_node = split_end
            return to_remove, self
        
    
price_1 = Node(all_prices[0])
node = price_1
for i in all_prices[1:5]:
    node = node.append(i)

removed, price_1 = price_1.pop(0)
removed, price_1 = price_1.pop(3)

print(price_1[2].value)


## Mission 16

