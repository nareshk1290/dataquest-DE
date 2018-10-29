################ Vacuuming Postgres Databases ################

## Mission 1

conn = psycopg2.connect(dbname="dq", user="hud_admin", password="abc123")
cur = conn.cursor()
cur.execute("DELETE FROM homeless_by_coc")
filename = 'homeless_by_coc.csv'
with open(filename) as f:
    statement = cur.mogrify('COPY homeless_by_coc FROM STDIN WITH CSV HEADER', (AsIs(filename.split('.')[0]), ))
    cur.copy_expert(statement, f)
cur.execute("SELECT COUNT(*) as total from homeless_by_coc")
homeless_rows = cur.fetchone()

## Mission 3

conn = psycopg2.connect(dbname="dq", user="hud_admin", password="abc123")
cur = conn.cursor()

cur.execute("SELECT n_dead_tup FROM pg_stat_all_tables WHERE relname='homeless_by_coc'")
print(cur.fetchone()[0])
cur.execute("DELETE FROM homeless_by_coc")
with open('homeless_by_coc.csv') as f:
    cur.copy_expert('COPY homeless_by_coc FROM STDIN WITH CSV HEADER', f)
conn.commit()
cur.execute("SELECT n_dead_tup FROM pg_stat_all_tables WHERE relname='homeless_by_coc'")
homeless_dead_rows = cur.fetchone()[0]

## Mission 5

conn = psycopg2.connect(dbname="dq", user="hud_admin", password="abc123")
conn.autocommit = True
cur = conn.cursor()
cur.execute("SELECT count(n_dead_tup) as dead_rows FROM pg_stat_all_tables WHERE relname='homeless_by_coc'")
print(cur.fetchone()[0])
cur.execute("VACUUM homeless_by_coc")
cur.execute("SELECT count(n_dead_tup) as dead_rows FROM pg_stat_all_tables WHERE relname='homeless_by_coc'")
homeless_dead_rows = cur.fetchone()[0]

## Mission 6

conn = psycopg2.connect(dbname="dq", user="hud_admin", password="abc123")
conn.autocommit = True
cur = conn.cursor()
cur.execute("EXPLAIN SELECT * FROM homeless_by_coc")
pp.pprint(cur.fetchall())
cur.execute("VACUUM homeless_by_coc")
cur.execute("EXPLAIN SELECT * FROM homeless_by_coc")
pp.pprint(cur.fetchall())

## Mission 7

conn = psycopg2.connect(dbname="dq", user="hud_admin", password="abc123")
conn.autocommit = True
cur = conn.cursor()
cur.execute("VACUUM FULL")