################ Exploring Postgres Databases ################

## Mission 1

import psycopg2
conn = psycopg2.connect(dbname="dq", user="hud_admin", password="eRqg123EEkl")
print(conn)

## Mission 2

conn = psycopg2.connect(dbname="dq", user="hud_admin", password="eRqg123EEkl")
cur = conn.cursor()
cur.execute("SELECT table_name from information_schema.tables order by table_name")
table_names = cur.fetchall()
for table_name in table_names:
    print(table_name)
	
## Mission 3

conn = psycopg2.connect(dbname="dq", user="hud_admin", password="eRqg123EEkl")
cur = conn.cursor()
cur.execute("SELECT table_name from information_schema.tables WHERE table_schema='public' order by table_name")
for table_name in cur.fetchall():
    print(table_name[0])
	
## Mission 4

conn = psycopg2.connect(dbname="dq", user="hud_admin", password="eRqg123EEkl")
cur = conn.cursor()
from psycopg2.extensions import AsIs
cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public'")
for table in cur.fetchall(): 
    table = table[0]
    proper_interpolation = cur.execute("SELECT * FROM %s LIMIT 0", [AsIs(table)])
    print(cur.description, "\n")
	
## Mission 5

conn = psycopg2.connect(dbname="dq", user="hud_admin", password="eRqg123EEkl")
cur = conn.cursor()
cur.execute("SELECT oid, typname FROM pg_catalog.pg_type")
type_mappings = {
    int(oid): typname
    for oid, typname in cur.fetchall()
}

## Mission 6

from psycopg2.extensions import AsIs
conn = psycopg2.connect(dbname="dq", user="hud_admin", password="eRqg123EEkl")
cur = conn.cursor()
readable_description = {}
for table in table_names:
    cur.execute("SELECT * FROM %s LIMIT 0", [AsIs(table)])
    readable_description[table] = dict(
        columns=[
            dict(
                name=col.name,
                type=type_mappings[col.type_code],
                length=col.internal_size
            )
            for col in cur.description
        ]
    )
print(readable_description)

## Mission 7

from psycopg2.extensions import AsIs
conn = psycopg2.connect(dbname="dq", user="hud_admin", password="eRqg123EEkl")
cur = conn.cursor()
for table in readable_description.keys():
    cur.execute("SELECT COUNT(*) FROM %s", [AsIs(table)])
    readable_description[table]["total"] = cur.fetchone()
print(readable_description)

## Mission 8

from psycopg2.extensions import AsIs
conn = psycopg2.connect(dbname="dq", user="hud_admin", password="eRqg123EEkl")
cur = conn.cursor()
for table in readable_description.keys():
    cur.execute("SELECT * FROM %s LIMIT 100", [AsIs(table)])
    readable_description[table]["sample_rows"] = cur.fetchall()
print(readable_description)
