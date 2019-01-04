################ Quickly Analyzing Data with Parallel Processing ################

## Mission 1

with open("lines/theprincessbride.txt") as f:
    print(f.read())

with open("lines/theroadwarrior.txt") as f:
    print(f.read())

with open("lines/spiderman.txt") as f:
    print(f.read())
	
	
## Mission 2

import concurrent.futures
numbers = [1,10,20,50]

import math
pool = concurrent.futures.ProcessPoolExecutor(max_workers=10)
roots = pool.map(math.sqrt, numbers)
roots = list(roots)

## Mission 3

import concurrent.futures

def file_length(filename):
    with open(filename) as f:
        counter = 0
        for line in f:
            counter += 1
    return counter

import os
results = []
pool = concurrent.futures.ProcessPoolExecutor(max_workers=5)
filenames = ["lines/{}".format(f) for f in os.listdir("lines")]
lengths = pool.map(file_length, filenames)
lengths = list(lengths)

movie_lengths = {}
for i in range(len(lengths)):
    movie_lengths[filenames[i].replace("lines/", "")] = lengths[i]

most_lines = max(movie_lengths.keys(), key=(lambda k: movie_lengths[k]))

## Mission 4

import concurrent.futures
def longest_line(filename):
    with open(filename) as f:
        max_length = 0
        longest_line = ""
        for line in f:
            line_length = len(line)
            if line_length > max_length:
                max_length = line_length
                longest_line = line
    return max_length, longest_line

results = []
pool = concurrent.futures.ThreadPoolExecutor(max_workers=5)
filenames = ["lines/{}".format(f) for f in os.listdir("lines")]
lengths = pool.map(longest_line, filenames)
lengths = list(lengths)

line_lengths = {}
for i in range(len(lengths)):
    line_lengths[filenames[i].replace("lines/", "")] = lengths[i]

longest_line_movie = max(line_lengths.keys(), key=(lambda k: line_lengths[k][0]))
longest_line = line_lengths[longest_line_movie][1]

## Mission 5

import concurrent.futures
import time

def most_common_word(filename):
    with open(filename) as f:
        words = f.read().split(" ")
    from collections import Counter
    count = Counter(words)
    return count.most_common()[0][0]

results = []
start = time.time()

pool = concurrent.futures.ThreadPoolExecutor(max_workers=5)
filenames = ["lines/{}".format(f) for f in os.listdir("lines")]
words = pool.map(most_common_word, filenames)
words = list(words)

end = time.time()

common_words = {}
for i in range(len(lengths)):
    common_words[filenames[i].replace("lines/", "")] = words[i]
    
print(end - start)

## Mission 8

import concurrent.futures

import os

def most_common_word(filename):
    with open(filename) as f:
        data = f.read().lower()
    import re
    data = re.sub("\W+", " ", data)
    words = data.split(" ")
    words = [w for w in words if len(w) >= 5]
    from collections import Counter
    count = Counter(words)
    return count.most_common()[0][0]

results = []
pool = concurrent.futures.ProcessPoolExecutor(max_workers=2)
filenames = ["lines/{}".format(f) for f in os.listdir("lines")]
words = pool.map(most_common_word, filenames)
words = list(words)

common_words = {}
for i in range(len(lengths)):
    common_words[filenames[i].replace("lines/", "")] = words[i]
	
## Mission 9

from collections import Counter

def word_frequencies(filename):
    with open(filename) as f:
        data = f.read().lower()
    import re
    data = re.sub("\W+", " ", data)
    words = data.split(" ")
    words = [w for w in words if len(w) >= 5]
    from collections import Counter
    count = Counter(words)
    return dict(count)

results = []
pool = concurrent.futures.ProcessPoolExecutor(max_workers=2)
filenames = ["lines/{}".format(f) for f in os.listdir("lines")]
word_counts = pool.map(word_frequencies, filenames)
word_counts = list(word_counts)

total_word_counts = {}

for wc in word_counts:
    for k,v in wc.items():
        if k not in total_word_counts:
            total_word_counts[k] = 0
        total_word_counts[k] += v

top_200 = Counter(total_word_counts).most_common(200)