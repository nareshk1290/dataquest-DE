################ Overcoming the Limitations of Threads ################

## Mission 1

import threading
import time
import statistics

def read_data():
    with open("Emails.csv") as f:
        data = f.read()
        
times = []
for i in range(100):
    start = time.time()
    read_data()
    end = time.time()
    times.append(end - start)
    
threaded_times = []
for i in range(100):
    start = time.time()
    
    t1 = threading.Thread(target=read_data)
    t2 = threading.Thread(target=read_data)
    
    t1.start()
    t2.start()
    
    for thread in [t1, t2]:
        thread.join()
        
    end = time.time()
    threaded_times.append(end - start)
    
print(statistics.median(times))
print(statistics.median(threaded_times))

## Mission 4

import pandas
import time

emails = pandas.read_csv("Emails.csv")
capital_letters = []

start = time.time()
for email in emails["RawText"]:
    capital_letters.append(len([letter for letter in email if letter.isupper()]))

total = time.time() - start
print(total)

## Mission 6

import threading

capital_letters1 = []
capital_letters2 = []

start = time.time()

def count_capital_letters(email):
    return len([letter for letter in email if letter.isupper()])

def count_capitals_in_emails(start, finish, capital_letters):
    for email in emails["RawText"][start:finish]:
        capital_letters.append(count_capital_letters(email))
        
t1 = threading.Thread(target=count_capitals_in_emails, args=(0, 3972, capital_letters1))
t2 = threading.Thread(target=count_capitals_in_emails, args=(3972, 7946, capital_letters2))

t1.start()
t2.start()

for thread in [t1, t2]:
    thread.join()
    
total = time.time() - start

print(total)

## Mission 9

import threading
import multiprocessing

capital_letters1 = []
capital_letters2 = []

start = time.time()

def count_capital_letters(email):
    return len([letter for letter in email if letter.isupper()])

def count_capitals_in_emails(start, finish, capital_letters):
    for email in emails["RawText"][start:finish]:
        capital_letters.append(count_capital_letters(email))
        
p1 = multiprocessing.Process(target=count_capitals_in_emails, args=(0, 3972, capital_letters1))
p2 = multiprocessing.Process(target=count_capitals_in_emails, args=(3972, 7946, capital_letters2))

p1.start()
p2.start()

for process in [p1, p2]:
    process.join()
    
total = time.time() - start

print(total)
print(capital_letters1)

## Mission 11

import threading
import multiprocessing

def count_capital_letters(email):
    return len([letter for letter in email if letter.isupper()])

def count_capitals_in_emails(start, finish, capital_letters):
    for email in emails["RawText"][start:finish]:
        capital_letters.append(count_capital_letters(email))
        
p1 = multiprocessing.Process(target=count_capitals_in_emails, args=(0, 1986, capital_letters1))
p2 = multiprocessing.Process(target=count_capitals_in_emails, args=(1986, 3972, capital_letters1))
p3 = multiprocessing.Process(target=count_capitals_in_emails, args=(3972, 5958, capital_letters2))
p4 = multiprocessing.Process(target=count_capitals_in_emails, args=(5958, 7946, capital_letters2))

p1.start()
p2.start()
p3.start()
p4.start()

for process in [p1, p2, p3, p4]:
    process.join()
    
total = time.time() - start

print(total)

## Mission 13

import multiprocessing

def count_capital_letters(email):
    return len([letter for letter in email if letter.isupper()])

def count_capitals_in_emails(start, finish, conn):
    capital_letters = []
    for email in emails["RawText"][start:finish]:
        capital_letters.append(count_capital_letters(email))
    conn.send(capital_letters)
    conn.close()

start = time.time()
parent_conn1, child_conn1 = multiprocessing.Pipe()
parent_conn2, child_conn2 = multiprocessing.Pipe()

p1 = multiprocessing.Process(target=count_capitals_in_emails, args=(0, 3972, child_conn1))
p2 = multiprocessing.Process(target=count_capitals_in_emails, args=(3972, 7946, child_conn2))
p1.start()
p2.start()

capital_letters1 = parent_conn1.recv()
capital_letters2 = parent_conn2.recv()

for process in [p1, p2]:
    process.join()
    
total = time.time() - start

print(total)

## Mission 15

from multiprocessing import Pool
import time

p = Pool(2)

def count_capital_letters(email):
    return len([letter for letter in email if letter.isupper()])

start = time.time()

capital_letters = p.map(count_capital_letters, emails["RawText"])
total = time.time() - start
print(total)