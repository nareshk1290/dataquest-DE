################ Augmenting Pandas with SQLite  ################

## Mission 1

import sqlite3
import pandas as pd

conn = sqlite3.connect("moma.db")
moma_iter = pd.read_csv('moma.csv', chunksize=1000)
for chunk in moma_iter:
    chunk.to_sql("exhibitions", conn, if_exists='append', index=False)
	
## Mission 2

results_df = pd.read_sql('PRAGMA table_info(exhibitions);', conn)
print(results_df)

## Mission 3

moma_iter = pd.read_csv('moma.csv', chunksize=1000)
for chunk in moma_iter:
    chunk['ExhibitionSortOrder'] = chunk['ExhibitionSortOrder'].astype('int16')
    chunk.to_sql("exhibitions", conn, if_exists='append', index=False)
results_df = pd.read_sql('PRAGMA table_info(exhibitions);', conn)
print(results_df)

## Mission 4

eid_counts = pd.read_sql('SELECT exhibitionid, count(*) as counts from exhibitions group by exhibitionid order by counts desc', conn)
print(eid_counts[:10])

## Mission 5

eid_query = pd.read_sql('SELECT exhibitionid from exhibitions', conn)
eid_pandas_counts = eid_query['ExhibitionID'].value_counts()
print(eid_pandas_counts[:10])