################ Loading and Extracting Data with Tables ################

## Mission 1

conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
from datetime import date
with open('ign.csv', 'r') as f:
    next(f)
    reader = csv.reader(f)
    next_row = []
    for row in reader:
        cur.execute('INSERT INTO ign_reviews VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)', row)
conn.commit()

## Mission 2

conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
with open('ign.csv', 'r') as f:
    next(f)
    reader = csv.reader(f)
    mogrified = [ 
        cur.mogrify("(%s, %s, %s, %s, %s, %s, %s, %s, %s)", row).decode('utf-8')
        for row in reader
    ]
mogrified_values = ",".join(mogrified) 
cur.execute('INSERT INTO ign_reviews VALUES ' + mogrified_values)
conn.commit() 

## Mission 3

conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
with open('ign.csv', 'r') as f:
    cur.copy_expert('COPY ign_reviews FROM STDIN WITH CSV HEADER', f)
conn.commit() 

## Mission 4

import time

conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()

# Multiple single insert statements.
start = time.time()
with open('ign.csv', 'r') as f:
    next(f)
    reader = csv.reader(f)
    for row in reader:
        cur.execute(
            "INSERT INTO ign_reviews VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
            row
        )
conn.rollback()
print("Single statment insert: ", time.time() - start)
        
# Multiple mogrify insert.
start = time.time()
with open('ign.csv', 'r') as f:
    next(f)
    reader = csv.reader(f)
    mogrified = [ 
        cur.mogrify("(%s, %s, %s, %s, %s, %s, %s, %s, %s)", row).decode('utf-8')
        for row in reader
    ] 
    mogrified_values = ",".join(mogrified) 
    cur.execute('INSERT INTO ign_reviews VALUES ' + mogrified_values)
conn.rollback()
print("Multiple mogrify insert: ", time.time() - start)

        
# Copy expert method.
start = time.time()
with open('ign.csv', 'r') as f:
    cur.copy_expert('COPY ign_reviews FROM STDIN WITH CSV HEADER', f)
conn.rollback()
print("Copy expert method: ", time.time() - start)


## Mission 5

conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
with open('old_ign_reviews.csv', 'w') as f:
    cur.copy_expert('COPY old_ign_reviews TO STDOUT WITH CSV HEADER', f)
conn.commit()

## Mission 6

import csv
from datetime import date
conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
with open('old_ign_reviews.csv', 'r+') as f:
    cur.copy_expert('COPY old_ign_reviews TO STDOUT WITH CSV HEADER', f)
    f.seek(0)
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        updated_row = row[:8]
        updated_row.append(date(int(row[8]), int(row[9]), int(row[10])))
        cur.execute("INSERT INTO ign_reviews VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", updated_row)
    conn.commit()
	
## Mission 7

conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
cur.execute("""
INSERT INTO ign_reviews (
    id, score_phrase, title, url, platform, score,
    genre, editors_choice, release_date
)
SELECT id, score_phrase, title_of_game_review as title,
    url, platform, score, genre, editors_choice,
    to_date(release_day || '-' || release_month || '-' || release_year, 'DD-MM-YYYY') as release_date
FROM old_ign_reviews
""")
conn.commit()
