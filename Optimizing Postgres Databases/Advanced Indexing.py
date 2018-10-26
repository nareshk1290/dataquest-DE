################ Advanced Indexing ################

## Mission 1

conn = psycopg2.connect(dbname="dq", user="hud_admin", password="abc123")
cur = conn.cursor()
cur.execute("CREATE INDEX state_idx ON homeless_by_coc(state)")
conn.commit()
cur.execute("EXPLAIN (format json) SELECT * FROM homeless_by_coc WHERE state='CA' AND year > '1991-01-01' ")
pp.pprint(cur.fetchall())

## Mission 3

conn = psycopg2.connect(dbname="dq", user="hud_admin", password="abc123")
cur = conn.cursor()
cur.execute("CREATE INDEX state_idx ON homeless_by_coc(state)")
conn.commit()
cur.execute("EXPLAIN (format json) SELECT * FROM homeless_by_coc WHERE state='CA' AND year > '1991-01-01' ")
pp.pprint(cur.fetchall())
cur.execute("DROP INDEX IF EXISTS state_idx")
conn.commit()
cur.execute("EXPLAIN (format json) SELECT * FROM homeless_by_coc WHERE state='CA' AND year > '1991-01-01' ")
pp.pprint(cur.fetchall())
cur.execute("CREATE INDEX state_year_idx ON homeless_by_coc(state, year)")
conn.commit()
cur.execute("EXPLAIN (format json) SELECT * FROM homeless_by_coc WHERE state='CA' AND year > '1991-01-01' ")
pp.pprint(cur.fetchall())

## Mission 4

conn = psycopg2.connect(dbname="dq", user="hud_admin", password="abc123")
cur = conn.cursor()
cur.execute("CREATE INDEX state_year_coc_number_idx ON homeless_by_coc(state, year, coc_number)")
conn.commit()

## Mission 5

import time
conn = psycopg2.connect(dbname="dq", user="hud_admin", password="abc123")
cur = conn.cursor()
filename = 'homeless_by_coc.csv'

start_time = time.time()
with open(filename) as f:
    statement = cur.mogrify('COPY %s FROM STDIN WITH CSV HEADER', (AsIs(filename.split('.')[0]), ))
    cur.copy_expert(statement, f)
print(time.time() - start_time)
cur.execute("DELETE FROM homeless_by_coc")
cur.execute("CREATE INDEX state_year_idx ON homeless_by_coc(state, year)")

start_time = time.time()
with open(filename) as f:
    statement = cur.mogrify('COPY %s FROM STDIN WITH CSV HEADER', (AsIs(filename.split('.')[0]), ))
    cur.copy_expert(statement, f)
print(time.time() - start_time)

## Mission 6

conn = psycopg2.connect(dbname="dq", user="hud_admin", password="abc123")
cur = conn.cursor()
cur.execute("CREATE INDEX state_year_idx ON homeless_by_coc(state, year DESC)")
conn.commit()
cur.execute("SELECT DISTINCT year from homeless_by_coc where state = 'CA' AND year > '1991-01-01' ")
ordered_years = cur.fetchall()
pp.pprint(ordered_years)

## Mission 7

conn = psycopg2.connect(dbname="dq", user="hud_admin", password="abc123")
cur = conn.cursor()
cur.execute("DROP INDEX IF EXISTS measures_lower_idx")
cur.execute("CREATE INDEX measures_lower_idx ON homeless_by_coc(lower(measures))")
conn.commit()
cur.execute("SELECT * from homeless_by_coc where lower(measures) = 'unsheltered homeless people in families'")
unsheltered_row = cur.fetchone()

## Mission 8

conn = psycopg2.connect(dbname="dq", user="hud_admin", password="abc123")
cur = conn.cursor()
cur.execute("DROP INDEX IF EXISTS state_count_greater_0")
cur.execute("CREATE INDEX state_count_greater_0 ON homeless_by_coc(state) WHERE count > 0")
conn.commit()
cur.execute("EXPLAIN (ANALYZE) SELECT * from homeless_by_coc as hbc where hbc.state = 'CA' and count > 0")
pp.pprint(cur.fetchall())

## Mission 9

conn = psycopg2.connect(dbname="dq", user="hud_admin", password="abc123")
cur = conn.cursor()
cur.execute("DROP INDEX IF EXISTS state_year_measures_idx")
cur.execute("CREATE INDEX state_year_measures_idx ON homeless_by_coc(state, lower(measures)) WHERE year > '2007-01-01'")
conn.commit()
cur.execute("EXPLAIN ANALYZE SELECT hbc.year, si.name, hbc.count FROM homeless_by_coc hbc, state_info si WHERE hbc.state = si.postal AND hbc.year > '2007-01-01' AND hbc.measures != 'total homeless'")
pp.pprint(cur.fetchall())