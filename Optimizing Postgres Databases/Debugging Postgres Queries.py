################ Debugging Postgres Queries ################

## Mission 1

import pprint as pp
conn = psycopg2.connect(dbname="dq", user="hud_admin", password="abc123")
cur = conn.cursor()
cur.execute("EXPLAIN Select * from homeless_by_coc")
pp.pprint(cur.fetchall())

## Mission 2

conn = psycopg2.connect(dbname="dq", user="hud_admin", password="abc123")
cur = conn.cursor()
cur.execute("EXPLAIN Select count(*) from homeless_by_coc where year > '2012-01-01'")
pp.pprint(cur.fetchall())

## Mission 3

conn = psycopg2.connect(dbname="dq", user="hud_admin", password="abc123")
cur = conn.cursor()
cur.execute("EXPLAIN (format json) Select count(*) from homeless_by_coc where year > '2012-01-01'")
pp.pprint(cur.fetchall())

## Mission 5

conn = psycopg2.connect(dbname="dq", user="hud_admin", password="abc123")
cur = conn.cursor()
cur.execute("EXPLAIN (ANALYZE, FORMAT json) Select count(*) from homeless_by_coc where year > '2012-01-01'")
pp.pprint(cur.fetchall())

## Mission 6

conn = psycopg2.connect(dbname="dq", user="hud_admin", password="abc123")
cur = conn.cursor()
cur.execute("EXPLAIN (ANALYZE, FORMAT json) DELETE FROM state_household_incomes")
conn.rollback()
pp.pprint(cur.fetchall())

## Mission 7

conn = psycopg2.connect(dbname="dq", user="hud_admin", password="abc123")
cur = conn.cursor()
cur.execute("EXPLAIN (ANALYZE, FORMAT json) SELECT hbc.state, hbc.coc_number, hbc.coc_name FROM homeless_by_coc as hbc, state_info as sta where hbc.state = sta.postal")
pp.pprint(cur.fetchall())