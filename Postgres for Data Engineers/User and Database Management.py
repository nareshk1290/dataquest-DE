################ User and Database Management ################

## Mission 1

import psycopg2
conn = psycopg2.connect(dbname="dq", user="postgres", password="abc123")
print(conn)

## Mission 2

import psycopg2
conn = psycopg2.connect(dbname="dq", user="postgres", password="password")
cur = conn.cursor()
cur.execute("CREATE USER data_viewer WITH CREATEUSER CREATEDB PASSWORD 'somepassword'")
conn.commit()

## Mission 3

conn = psycopg2.connect(dbname="dq", user="dq")
cur = conn.cursor()
cur.execute("REVOKE ALL on user_accounts FROM data_viewer")
conn.commit()

## Mission 4

conn = psycopg2.connect(dbname="dq", user="dq")
cur = conn.cursor()
cur.execute("GRANT SELECT ON user_accounts TO data_viewer")
conn.commit()

## Mission 5

conn = psycopg2.connect(dbname="dq", user="dq")
cur = conn.cursor()
cur.execute("CREATE GROUP readonly NOLOGIN")
cur.execute("REVOKE ALL on user_accounts FROM readonly")
cur.execute("GRANT SELECT ON user_accounts TO readonly")
cur.execute("GRANT readonly TO data_viewer")
conn.commit()

## Mission 6

conn = psycopg2.connect(dbname="dq", user="dq")
conn.autocommit = True
cur = conn.cursor()
cur.execute("CREATE DATABASE user_accounts OWNER data_viewer")

## Mission 7

conn = psycopg2.connect(dbname="dq", user="dq")
conn.autocommit = True
cur = conn.cursor()
cur.execute("CREATE DATABASE top_secret")
conn = psycopg2.connect(dbname="top_secret", user="dq")
cur = conn.cursor()
cur.execute("CREATE TABLE documents (id INT, info TEXT)")
cur.execute("CREATE GROUP spies NOLOGIN")
cur.execute("REVOKE ALL on documents FROM spies")
cur.execute("GRANT SELECT, INSERT, UPDATE ON documents TO spies")
cur.execute("CREATE USER double_o_7 WITH CREATEDB PASSWORD 'shakennotstirred' IN GROUP spies")
conn.commit()
conn_007 = psycopg2.connect(dbname="top_secret", user="double_o_7", password='shakennotstirred')