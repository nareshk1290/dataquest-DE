################ Using an Index ################

## Mission 1

conn = psycopg2.connect(dbname="dq", user="hud_admin", password="abc123")
cur = conn.cursor()
cur.execute("EXPLAIN (format json) Select * from homeless_by_coc where id =10")
pp.pprint(cur.fetchall())

## Mission 2

conn = psycopg2.connect(dbname="dq", user="hud_admin", password="abc123")
cur = conn.cursor()
cur.execute("EXPLAIN (format json) SELECT * FROM homeless_by_coc WHERE id=5")
homeless_query_plan = cur.fetchall()
pp.pprint(homeless_query_plan)
cur.execute("EXPLAIN (format json) SELECT * FROM state_info WHERE name='Alabama'")
state_query_plan = cur.fetchall()
pp.pprint(state_query_plan)
cur.execute("EXPLAIN (format json) SELECT * FROM state_household_incomes WHERE state='Georgia'")
incomes_query_plan = cur.fetchall()
pp.pprint(incomes_query_plan)

## Mission 4

conn = psycopg2.connect(dbname="dq", user="hud_admin", password="abc123")
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS state_idx")
cur.execute("""
CREATE TABLE state_idx (state VARCHAR(2), homeless_id INTEGER)
""")
cur.execute(""" INSERT INTO state_idx SELECT state, id from homeless_by_coc """)
conn.commit()
cur.execute(""" SELECT sta.state, hbc.year, hbc.coc_number 
from homeless_by_coc as hbc, state_idx as sta 
WHERE hbc.id = sta.homeless_id
and sta.state = 'CA'
""")
pp.pprint(cur.fetchall())

## Mission 5

conn = psycopg2.connect(dbname="dq", user="hud_admin", password="abc123")
cur = conn.cursor()
cur.execute("""
SELECT hbc.id, hbc.year, hbc.coc_number FROM homeless_by_coc hbc, state_idx
WHERE state_idx.state = 'CA' AND state_idx.homeless_id = hbc.id
""")
conn = psycopg2.connect(dbname="dq", user="hud_admin", password="abc123")
cur = conn.cursor()
cur.execute("""
EXPLAIN (ANALYZE, format json) SELECT hbc.id, hbc.year, hbc.coc_number FROM homeless_by_coc hbc, state_idx
WHERE state_idx.state = 'CA' AND state_idx.homeless_id = hbc.id
""")
pp.pprint(cur.fetchall())
cur.execute("""
EXPLAIN (ANALYZE, format json) SELECT id, year, coc_number FROM homeless_by_coc WHERE state='CA'
""")
pp.pprint(cur.fetchall())

## Mission 6

conn = psycopg2.connect(dbname="dq", user="hud_admin", password="abc123")
cur = conn.cursor()
cur.execute("CREATE INDEX state_idx ON homeless_by_coc(state)")
conn.commit()
cur.execute("EXPLAIN (ANALYZE, format json) Select * from homeless_by_coc where state='CA'")
pp.pprint(cur.fetchall())

## Mission 7

conn = psycopg2.connect(dbname="dq", user="hud_admin", password="abc123")
cur = conn.cursor()
cur.execute("DROP INDEX IF EXISTS state_idx")
conn.commit()
cur.execute("EXPLAIN (ANALYZE, format json) SELECT * FROM homeless_by_coc WHERE state='CA'")
pp.pprint(cur.fetchall())

## Mission 8

conn = psycopg2.connect(dbname="dq", user="hud_admin", password="abc123")
cur = conn.cursor()
cur.execute("CREATE INDEX state_idx ON homeless_by_coc(state)")
conn.commit()
cur.execute("""EXPLAIN (ANALYZE, format json) 
SELECT hbc.state, hbc.coc_number, hbc.coc_name, si.name 
FROM homeless_by_coc as hbc, state_info as si 
WHERE hbc.state = si.postal""")
pp.pprint(cur.fetchall())
cur.execute("DROP INDEX IF EXISTS state_idx")
conn.commit()
cur.execute("""EXPLAIN (ANALYZE, format json) 
SELECT hbc.state, hbc.coc_number, hbc.coc_name, si.name 
FROM homeless_by_coc as hbc, state_info as si 
WHERE hbc.state = si.postal""")
pp.pprint(cur.fetchall())