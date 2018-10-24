################ Intro To Postgres ################

## Mission 2

import psycopg2
conn = psycopg2.connect("dbname=dq user=dq")
print(conn)
conn.close()

## Mission 3

import psycopg2
conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
cur.execute('SELECT * FROM notes')
notes = cur.fetchall()
conn.close()

## Mission 4

import psycopg2
conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS users")
cur.execute("""CREATE TABLE users(
           id INTEGER PRIMARY KEY,
           email TEXT,
           name TEXT,
           address TEXT
           )""")
		   
## Mission 5

import psycopg2
conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS users")
cur.execute("""CREATE TABLE users(
           id INTEGER PRIMARY KEY,
           email TEXT,
           name TEXT,
           address TEXT
           )""")

conn.commit()
conn.close()

		   
## Mission 6

import csv
import psycopg2

with open('user_accounts.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    rows = [row for row in reader]
        
conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
for row in rows:
    cur.execute("INSERT INTO users VALUES(%s, %s, %s, %s)", row)
conn.commit()

cur.execute("SELECT * from users")
users = cur.fetchall()
conn.close()

## Mission 7

conn = psycopg2.connect('dbname=dq user=dq')
cur = conn.cursor()
with open('user_accounts.csv', 'r') as f:
    next(f)
    cur.copy_from(f, 'users', sep=',')
conn.commit()
cur.execute("SELECT * from users")
users = cur.fetchall()
conn.close()
