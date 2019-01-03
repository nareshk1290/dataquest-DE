################ CPU Bounds Program  ################

## Mission 3

import pandas as pd

data = pd.read_csv("ecommerce5000.csv", encoding="Latin-1")
data.head()

## Mission 5

iz_operations = 0
item_operations = 0
duplicates_init = 1
duplicates_false = 0
duplicates_true = 0
if_duplicate = 0
duplicates_append = 0

# Initialize a list to store our duplicates
duplicates = []

# Loop through each item in the query column.
for i, item in enumerate(query):
    duplicates_false += 1
    duplicate = False
    
    # Loop through each item in the query column.
    for z, item2 in enumerate(query):
        # If the outer and inner loops are on the same value, keep going.
        # Without this, we'll falsely detect rows as duplicates.
        iz_operations += 1
        if i == z:
            continue
        # Mark as duplicate if we find a match.
        item_operations += 1
        if item == item2:
            duplicates_true += 1
            duplicate = True
    if_duplicate += 1
    # Add to the duplicates list.
    if duplicate:
        duplicates_append += 1
        duplicates.append(item)
		
## Mission 6

sum_increments = 0
total = 0

for i, item in enumerate(query):
    total += len(item)
    sum_increments += 1
	
## Mission 7

counts_increments = 0
value_checks = 0
counts = {}
for i, item in enumerate(query):
    if item not in counts:
        counts[item] = 0
    counts_increments += 1
    counts[item] += 1
    
duplicates = []
for key, val in counts.items():
    value_checks += 1
    if val > 1:
        duplicates.append(key)

print(counts_increments)
print(value_checks)

## Mission 8

import time

start = time.time()

duplicate_series = query_series.duplicated()
duplicate_values_series = query_series[duplicate_series]

pandas_elapsed = time.time() - start
print(pandas_elapsed)

start = time.time()

counts = {}
for i, item in enumerate(query):
    if item not in counts:
        counts[item] = 0
    counts_increments += 1
    counts[item] += 1
    
duplicates = []
for key, val in counts.items():
    value_checks += 1
    if val > 1:
        duplicates.append(key)

elapsed = time.time() - start
print(elapsed)

## Mission 9

import time
import statistics
import matplotlib.pyplot as plt

def pandas_algo():
    duplicate_series = query_series.duplicated()
    duplicate_values_series = query_series[duplicate_series]
    
def algo():
    counts = {}
    for i, item in enumerate(query):
        if item not in counts:
            counts[item] = 0
        counts[item] += 1

    duplicates = []
    for key, val in counts.items():
        if val > 1:
            duplicates.append(key)
        
pandas_elapsed = []
for i in range(1000):
    start = time.time()
    pandas_algo()
    pandas_elapsed.append(time.time() - start)

elapsed = []
for i in range(1000):
    start = time.time()
    algo()
    elapsed.append(time.time() - start)

print(statistics.median(pandas_elapsed))
print(statistics.median(elapsed))

plt.hist(pandas_elapsed)
plt.show()
plt.hist(elapsed)

## Mission 10

import time
import statistics

def algo():
    unique = set()
    duplicates = set()
    for item in query:
        if item in unique:
            duplicates.add(item)
        else:
            unique.add(item)

elapsed = []
for i in range(1000):
    start = time.time()
    algo()
    elapsed.append(time.time() - start)
    
print(statistics.median(elapsed))

## Mission 12

def algo():
    unique = set()
    duplicates = set()
    for item in query:
        if item in unique:
            duplicates.add(item)
        else:
            unique.add(item)
            
import cProfile
cProfile.run("algo()")

## Mission 13

import time 
import statistics

def run_with_timing(func):
    elapsed = []
    for i in range(10):
        start = time.time()
        func()
        elapsed.append(time.time() - start)
    return statistics.median(elapsed)

def pandas_algo():
    get_max_relevance = lambda x: x.loc[x["relevance"].idxmax(), "product_link"]
    return data.groupby("query").apply(get_max_relevance)

def algo():
    links = {}
    for i, row in enumerate(query):
        if row not in links:
            links[row] = [0, ""]
        if relevance[i] > links[row][0]:
            links[row] = [relevance[i], product_link[i]]
    return links

print(run_with_timing(pandas_algo))
print(run_with_timing(algo))

## Mission 14

import re
import statistics

algo1_time_complexity = 0
algo1_space_complexity = 0

def algo1(data):
    total = 0
    for index, row in data.iterrows():
        total += int(row["rank"])
    return total

algo2_time_complexity = 0
algo2_space_complexity = 0

def algo2(data):
    prices = []
    for index, row in data.iterrows():
        price_search = re.search('.*(\d+).*', row["product_price"], re.IGNORECASE)

        if price_search:
            price = float(price_search.group(1))
        else:
            price = None
        prices.append(price)
    price_avg = statistics.mean([p for p in prices if p is not None])
    weighted_relevance = []
    for index, row in data.iterrows():
        if prices[index] is not None:
            price = prices[index] / price_avg
        else:
            price = price_avg
        weighted_relevance.append(float(row["relevance"]) * price)
    return weighted_relevance

algo1_time_complexity = 1
algo1_space_complexity = 0

algo2_time_complexity = 1
algo2_space_complexity = 1
