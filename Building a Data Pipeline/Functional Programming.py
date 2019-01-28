################ Functional Programming ################

## Mission 2

class LineCounter:
    def __init__(self, filename):
        self.file = open(filename, 'r')
        self.lines = []

    def read(self):
        self.lines = [line for line in self.file]

    def count(self):
        return len(self.lines)
    
lc = LineCounter('example_log.txt')
lc.read()
example_lines = lc.lines
lines_count = lc.count()


## Mission 4

def read(filename):
    with open(filename, 'r') as f:
        return [line for line in f]

lines = read('example_log.txt')
sorted_lines = sorted(lines, key = lambda x : x.split(' ')[5])
print(sorted_lines)


## Mission 5

lines = read('example_log.txt')
ip_addresses = list(map(lambda x : x.split()[0], lines))
print(ip_addresses)

## Mission 6

lines = read('example_log.txt')
ip_addresses = list(map(lambda x: x.split()[0], lines))

filtered_ips = list(filter(lambda x : int(x.split('.')[0]) <= 20, ip_addresses))
print(filtered_ips)

## Mission 7

from functools import reduce

lines = read('example_log.txt')
ip_addresses = list(map(lambda x: x.split()[0], lines))
filtered_ips = list(filter(lambda x: int(x.split('.')[0]) <= 20, ip_addresses))

count_all = reduce(lambda x, _: 2 if isinstance(x, str) else x + 1, lines)
count_filtered = reduce(lambda x, _: 2 if isinstance(x, str) else x + 1, filtered_ips)

ratio = count_filtered / count_all

print(ratio)

## Mission 8

lines = read('example_log.txt')
ip_addresses = [line.split()[0] for line in lines]
filtered_ips = [
    ip.split('.')[0]
    for ip in ip_addresses if int(ip.split('.')[0]) <= 20
]
count_all = reduce(lambda x, _: 2 if isinstance(x, str) else x + 1, lines)
count_filtered = reduce(lambda x, _: 2 if isinstance(x, str) else x + 1, filtered_ips)
ratio = count_filtered / count_all
print(ratio)

## Mission 9

from functools import partial

count = partial(
    reduce,
    lambda x, _: 2 if isinstance(x, str) else x + 1
)

lines = read('example_log.txt')
ip_addresses = [line.split()[0] for line in lines]
filtered_ips = [
    ip.split('.')[0]
    for ip in ip_addresses if int(ip.split('.')[0]) <= 20
]
count_all = count(lines)
count_filtered =  count(filtered_ips)
ratio = count_filtered / count_all
print(ratio)

## Mission 10

lines = read('example_log.txt')
ip_addresses = list(map(lambda x: x.split()[0], lines))
filtered_ips = list(filter(lambda x: int(x.split('.')[0]) <= 20, ip_addresses))

ratio = count_filtered / count_all

extract_ips = partial(
    map,
    lambda x: x.split()[0]
)
filter_ips = partial(
    filter,
    lambda x: int(x.split('.')[0]) <= 20
)
count = partial(
    reduce,
    lambda x, _: 2 if isinstance(x, str) else x + 1
)

composed = compose(
    extract_ips,
    filter_ips,
    count
)
counted = composed(lines)
