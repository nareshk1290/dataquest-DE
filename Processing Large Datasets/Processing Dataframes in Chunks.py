################ Processing Dataframes in Chunks ################

## Mission 2

import pandas as pd
import matplotlib.pyplot as plt

memory_footprints = []
chunk_iter = pd.read_csv("moma.csv", chunksize=250)
for chunk in chunk_iter:
    memory_footprints.append(chunk.memory_usage(deep=True).sum()/(1024*1024))

plt.hist(memory_footprints)
plt.show()

## Mission 3

num_rows = 0

chunk_iter = pd.read_csv("moma.csv", chunksize=250)
for chunk in chunk_iter:
    num_rows += len(chunk)
	
## Mission 4

dtypes = {"ConstituentBeginDate": "float", "ConstituentEndDate": "float"}
chunk_iter = pd.read_csv("moma.csv", chunksize=250, dtype=dtypes)
lifespans = []
for chunk in chunk_iter:
    diff = chunk['ConstituentEndDate'] - chunk['ConstituentBeginDate']
    lifespans.append(diff)
lifespans_dist = pd.concat(lifespans)
print(lifespans_dist)

## Mission 6

chunk_iter = pd.read_csv("moma.csv", chunksize=250, usecols=['Gender'])
overall_vc = list()
for chunk in chunk_iter:
    overall_vc.append(chunk['Gender'].value_counts())
combined_vc = pd.concat(overall_vc)
print(combined_vc)

## Mission 7

chunk_iter = pd.read_csv("moma.csv", chunksize=250, usecols=['Gender'])
overall_vc = list()
for chunk in chunk_iter:
    overall_vc.append(chunk['Gender'].value_counts())
combined_vc = pd.concat(overall_vc)
final_vc = combined_vc.groupby(combined_vc.index).sum() 

## Mission 8

chunk_iter = pd.read_csv("moma.csv", chunksize=1000)
df_list = []
for chunk in chunk_iter:
    temp = chunk['Gender'].groupby(chunk['ExhibitionID']).value_counts()
    df_list.append(temp)
final_df = pd.concat(df_list)
id_gender_counts = final_df.groupby(final_df.index).sum()