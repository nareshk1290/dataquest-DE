################ Hash Tables ################

## Mission 2

import os
quotes = {}
directory = "lines"
for filename in os.listdir(directory):
    with open(os.path.join(directory, filename)) as f:
        quotes[filename.replace(".txt", "")] = f.read()
		
## Mission 3

def simple_hash(key):
    key = str(key)
    return ord(key[0])

xmen_hash = simple_hash("xmen")
things_hash = simple_hash("10thingsihateaboutyou")

## Mission 4

def simple_hash(key):
    key = str(key)
    code = ord(key[0])
    return code % 20

xmen_hash = simple_hash("xmen")
things_hash = simple_hash("10thingsihateaboutyou")

## Mission 5

import numpy as np

def simple_hash(key):
    key = str(key)
    code = ord(key[0])
    return code % 20

class HashTable():
    
    def __init__(self, size):
        self.array = np.zeros(size, dtype=np.object)
        self.size = size
    
    def __getitem__(self, key):
        ind = simple_hash(key)
        return self.array[ind]
    
    def __setitem__(self, key, value):
        ind = simple_hash(key)
        self.array[ind] = value
        
hash_table = HashTable(20)

with open("lines/xmen.txt", 'r') as f:
    hash_table["xmen"] = f.read()
	
## Mission 6

class HashTable():
    
    def __init__(self, size):
        self.array = np.zeros(size, dtype=np.object)
        self.size = size
    
    def __getitem__(self, key):
        ind = simple_hash(key)
        return self.array[ind]
    
    def __setitem__(self, key, value):
        ind = simple_hash(key)
        if not isinstance(self.array[ind], list):
            self.array[ind] = []
        self.array[ind].append(value)

hash_table = HashTable(20)

with open("lines/xmen.txt", 'r') as f:
    hash_table["xmen"] = f.read()
    
with open("lines/xmenoriginswolverine.txt", 'r') as f:
    hash_table["xmenoriginswolverine"] = f.read()  
	
## Mission 7

class HashTable():
    
    def __init__(self, size):
        self.array = np.zeros(size, dtype=np.object)
        self.size = size
    
    def __getitem__(self, key):
        ind = simple_hash(key)
        for k,v in self.array[ind]:
            if key == k:
                return v
    
    def __setitem__(self, key, value):
        ind = simple_hash(key)
        if not isinstance(self.array[ind], list):
            self.array[ind] = []
        self.array[ind].append((key, value))
        
hash_table = HashTable(20)

with open("lines/xmen.txt", 'r') as f:
    hash_table["xmen"] = f.read()
    
with open("lines/xmenoriginswolverine.txt", 'r') as f:
    hash_table["xmenoriginswolverine"] = f.read() 
	
## Mission 8

class HashTable():
    
    def __init__(self, size):
        self.array = np.zeros(size, dtype=np.object)
        self.size = size
    
    def __getitem__(self, key):
        ind = simple_hash(key)
        for k,v in self.array[ind]:
            if key == k:
                return v
    
    def __setitem__(self, key, value):
        ind = simple_hash(key)
        if not isinstance(self.array[ind], list):
            self.array[ind] = []
        replace = None
        for i,data in enumerate(self.array[ind]):
            if data[0] == key:
                replace = i
        if replace is None:
            self.array[ind].append((key,value))
        else:
            self.array[ind][replace] = (key, value)
            
hash_table = HashTable(20)

with open("lines/xmen.txt", 'r') as f:
    hash_table["xmen"] = f.read()
    
with open("lines/xmenoriginswolverine.txt", 'r') as f:
    hash_table["xmen"] = f.read() 
	
## Mission 9

def simple_hash(key):
    key = str(key)
    code = ord(key[0])
    return code % 1

class HashTable():
    
    def __init__(self, size):
        self.array = np.zeros(size, dtype=np.object)
        self.size = size
    
    def __getitem__(self, key):
        counter = 0
        ind = simple_hash(key)
        for k,v in self.array[ind]:
            counter += 1
            if key == k:
                return counter
    
    def __setitem__(self, key, value):
        ind = simple_hash(key)
        if not isinstance(self.array[ind], list):
            self.array[ind] = []
        replace = None
        for i,data in enumerate(self.array[ind]):
            if data[0] == key:
                replace = i
        if replace is None:
            self.array[ind].append((key,value))
        else:
            self.array[ind][replace] = (key, value)

data = [
    ("xmen", "Wolverine"), 
    ("xmenoriginswolverine", "Superman"), 
    ("vanillasky", "Thor"), 
    ("tremors", "Aquaman")
]

hash_table = HashTable(1)
for k, v in data:
    hash_table[k] = v
    
counter = hash_table[k]

## Mission 10

import time
import os
import matplotlib.pyplot as plt

class HashTable():
    
    def __init__(self, size):
        self.array = np.zeros(size, dtype=np.object)
        self.size = size
    
    def __getitem__(self, key):
        ind = hash(key) % self.size
        for k,v in self.array[ind]:
            if key == k:
                return v
    
    def __setitem__(self, key, value):
        ind = hash(key) % self.size
        if not isinstance(self.array[ind], list):
            self.array[ind] = []
        replace = None
        for i,data in enumerate(self.array[ind]):
            if data[0] == key:
                replace = i
        if replace is None:
            self.array[ind].append((key,value))
        else:
            self.array[ind][replace] = (key, value)

def profile_table(size):
    start = time.time()
    hash_table = HashTable(size)
    directory = "lines"
    
    for filename in os.listdir(directory):
        name = filename.replace(".txt", "")
        hash_table[name] = quotes[name]
    
    duration = time.time() - start
    return duration

lengths = [1,10,20,30,40,50]
times = []
for l in lengths:
    times.append(profile_table(l))

plt.plot(lengths, times)