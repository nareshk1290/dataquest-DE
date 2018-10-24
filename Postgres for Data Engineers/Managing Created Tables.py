################ Managing Created Tables ################

## Mission 1

conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
cur.execute('ALTER TABLE old_ign_reviews RENAME TO ign_reviews')
conn.commit()
cur.execute('SELECT * FROM ign_reviews LIMIT 0')
print(cur.description)


## Mission 2

conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
cur.execute('ALTER TABLE ign_reviews DROP COLUMN full_url')
conn.commit()

## Mission 3

conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
cur.execute('ALTER TABLE ign_reviews ALTER COLUMN id TYPE BIGINT')
conn.commit()

## Mission 4

conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
cur.execute('ALTER TABLE ign_reviews RENAME COLUMN title_of_game_review TO title')
conn.commit()

## Mission 5

conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
cur.execute('ALTER TABLE ign_reviews ADD COLUMN release_date DATE')
conn.commit()

## Mission 6

conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
cur.execute(""" UPDATE ign_reviews SET release_date = to_date((release_day || '-' || release_month || '-' || release_year), 'DD-MM-YYYY')""")
conn.commit()

## Mission 7

conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
cur.execute('ALTER TABLE ign_reviews DROP COLUMN release_day')
cur.execute('ALTER TABLE ign_reviews DROP COLUMN release_month')
cur.execute('ALTER TABLE ign_reviews DROP COLUMN release_year')
conn.commit()