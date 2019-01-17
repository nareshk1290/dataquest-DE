################ Searching Arrays and Lists ################

## Mission 2

import pandas as pd

data = pd.read_csv("amounts.csv")
amounts = list(data["Amount"])
times = [int(i) for i in list(data["Time"])]
first_4554 = times.index(4554)

## Mission 3

def linear_search(array, search):
    indexes = []
    for i, item in enumerate(array):
        if item == search:
            indexes.append(i)
    return indexes

sevens = linear_search(times, 7)

## Mission 4

def linear_multi_search(array, search):
    indexes = []
    for i, item in enumerate(array):
        if item == search:
            indexes.append(i)
    return indexes

transactions = [[times[i], amounts[i]] for i in range(len(amounts))]
results = linear_multi_search(transactions, [56, 10.84])

## Mission 5

import matplotlib.pyplot as plt

def linear_search(array, search):
    counter = 0
    indexes = []
    for i, item in enumerate(array):
        counter += 1
        if item == search:
            indexes.append(i)
    return counter

counters = []
lengths = [10,100,1000,10000]
for i in lengths:
    first_amounts = amounts[:i]
    counter = linear_search(first_amounts, 7)
    counters.append(counter)
    
plt.plot(lengths, counters)

## Mission 7

import math

def swap(array, pos1, pos2):
    store = array[pos1]
    array[pos1] = array[pos2]
    array[pos2] = store

def insertion_sort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j - 1] > array[j]:
            swap(array, j, j-1)
            j-=1

def binary_search(array, search):
    insertion_sort(array)
    m = 0
    i = 0
    z = len(array) -1
    while i <= z:
        m = math.floor(i+ ((z-i) / 2))
        if array[m] == search:
            return m
        elif array[m] < search:
            i = m + 1
        elif array[m] > search:
            z = m - 1

result = binary_search(times, 56)

## Mission 8

def insertion_sort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j - 1] > array[j]:
            swap(array, j, j-1)
            j-=1

def binary_search(array, search):
    array.sort()
    m = 0
    i = 0
    z = len(array) - 1
    while i<= z:
        m = math.floor(i + ((z - i) / 2))
        if array[m] == search:
            return m
        elif array[m] < search:
            i = m + 1
        elif array[m] > search:
            z = m - 1
            
transactions = ["{}_{}".format(times[i], amounts[i]) for i in range(len(amounts))]
result = binary_search(transactions, "56_10.84")

## Mission 9

def binary_search(array, search):
    array.sort()
    m = 0
    i = 0
    z = len(array) - 1
    while i<= z:
        m = math.floor(i + ((z - i) / 2))
        if array[m] == search:
            return m
        elif array[m] < search:
            i = m + 1
        elif array[m] > search:
            z = m - 1
    return m

def fuzzy_match(array, lower, upper, m):
    j = m
    l = m + 1
    matches = []
    while j > 0 and lower <= array[j] <= upper:
        matches.append(array[j])
        j -= 1
        
    while l < len(array) and lower <= array[l] <= upper:
        matches.append(array[l])
        l += 1
    return matches

m = binary_search(amounts, 150)
matches = fuzzy_match(amounts, 100, 2000, m)

## Mission 10

import matplotlib.pyplot as plt

def binary_search(array, search):
    counter = 0
    array.sort()
    m = 0
    i = 0
    z = len(array) - 1
    while i<= z:
        counter += 1
        m = math.floor(i + ((z - i) / 2))
        if array[m] == search:
            return m
        elif array[m] < search:
            i = m + 1
        elif array[m] > search:
            z = m - 1
    return counter

counters = []
lengths = [10,100,1000,10000]
for i in lengths:
    first_amounts = amounts[:i]
    counter = binary_search(first_amounts, -1)
    counters.append(counter)
    
plt.plot(lengths, counters)

## Mission 11

def insertion_sort(array):
    counter = 0
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j - 1] > array[j]:
            counter += 1
            swap(array, j, j-1)
            j-=1
    return counter

def binary_search(array, search):
    counter = insertion_sort(array)
    insertion_sort(array)
    m = 0
    i = 0
    z = len(array) - 1
    while i<= z:
        counter += 1
        m = math.floor(i + ((z - i) / 2))
        if array[m] == search:
            return m
        elif array[m] < search:
            i = m + 1
        elif array[m] > search:
            z = m - 1
    return counter

lengths = [10,100,1000,10000]

counters = []
for i in lengths:
    first_amounts = sorted(amounts[:i], reverse=True)
    counter = binary_search(first_amounts, -1)
    counters.append(counter)

plt.plot(lengths, counters)