################ Sorting Arrays and Lists ################

## Mission 3

def swap(array, pos1, pos2):
    store = array[pos1]
    array[pos1] = array[pos2]
    array[pos2] = store
    
first_amounts = amounts[:10]
swap(first_amounts, 1, 2)


## Mission 4

def selection_sort(array):
    for i in range(len(array)):
        lowest_index = i
        for z in range(i, len(array)):
            if array[z] < array[lowest_index]:
                lowest_index = z
        swap(array, lowest_index, i)
        
first_amounts = amounts[:10]
selection_sort(first_amounts)


## Mission 5

import matplotlib.pyplot as plt

def selection_sort(array):
    counter = 0
    for i in range(len(array)):
        lowest_index = i
        for z in range(i, len(array)):
            counter += 1
            if array[z] < array[lowest_index]:
                lowest_index = z
        swap(array, lowest_index, i)
    return counter

counters = []
lengths = [10,100,1000,10000]
for i in lengths:
    first_amounts = amounts[:i]
    counter = selection_sort(first_amounts)
    counters.append(counter)
    
plt.plot(lengths, counters)

## Mission 6

def bubble_sort(array):
    swaps = 1
    while swaps > 0:
        swaps = 0
        for i in range(len(array) - 1):
            if array[i] > array[i+1]:
                swap(array, i, i+1)
                swaps += 1
            
first_amounts = amounts[:10]
bubble_sort(first_amounts)

## Mission 7

import matplotlib.pyplot as plt

def bubble_sort(array):
    swaps = 1
    counter = 0
    while swaps > 0:
        swaps = 0
        for i in range(len(array) - 1):
            counter += 1
            if array[i] > array[i+1]:
                swap(array, i, i+1)
                swaps += 1
    return counter

lengths = [10,100,1000,10000]

counters = []
for i in lengths:
    first_amounts = amounts[:i]
    counter = bubble_sort(first_amounts)
    counters.append(counter)
    
plt.plot(lengths, counters)


## Mission 9

def insertion_sort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j-1] > array[j]:
            swap(array, j, j-1)
            j -= 1 
    
first_amounts = amounts[:10]
insertion_sort(first_amounts)

## Mission 10

