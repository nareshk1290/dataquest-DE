################ Optimizing Datafram Memory Footprint ################

## Mission 2

import pandas as pd
moma = pd.read_csv('moma.csv')
moma.info()

## Mission 3

import pandas as pd
moma = pd.read_csv("moma.csv")
print(moma._data)

## Mission 5

import pandas as pd
moma = pd.read_csv("moma.csv")
total_bytes = moma.size*8
total_megabytes = total_bytes / (1024*1024)
print(total_bytes)
print(total_megabytes)

## Mission 7

obj_cols = moma.select_dtypes(include=['object'])
obj_cols_mem = obj_cols.memory_usage(deep=True)
print(obj_cols_mem)
obj_cols_sum = obj_cols_mem.sum() / (1024*1024)
print(obj_cols_sum)

## Mission 9

import numpy as np
col_min = moma['ExhibitionSortOrder'].min()
col_max = moma['ExhibitionSortOrder'].max()

if col_min > np.iinfo("int8").min and col_max <  np.iinfo("int8").max:
    moma['ExhibitionSortOrder'] = moma['ExhibitionSortOrder'].astype("int8")
elif col_min > np.iinfo("int16").min and col_max <  np.iinfo("int16").max:
    moma['ExhibitionSortOrder'] = moma['ExhibitionSortOrder'].astype("int16")
elif col_min > np.iinfo("int32").min and col_max <  np.iinfo("int32").max:
    moma['ExhibitionSortOrder'] = moma['ExhibitionSortOrder'].astype("int32")
elif col_min > np.iinfo("int64").min and col_max <  np.iinfo("int64").max:
    moma['ExhibitionSortOrder'] = moma['ExhibitionSortOrder'].astype("int64")
print(moma['ExhibitionSortOrder'].dtype)
print(moma['ExhibitionSortOrder'].memory_usage(deep=True))

## Mission 10

moma = pd.read_csv("moma.csv")
moma['ExhibitionSortOrder'] = moma['ExhibitionSortOrder'].astype("int16")
float_cols = moma.select_dtypes(include=['float'])
print(float_cols.dtypes)
for column in float_cols.columns:
    moma[column] = pd.to_numeric(moma[column], downcast='float')
print(moma.select_dtypes(include=['float']))

## Mission 12

moma['ExhibitionBeginDate'] = pd.to_datetime(moma['ExhibitionBeginDate'])
moma['ExhibitionEndDate'] = pd.to_datetime(moma['ExhibitionEndDate'])
print(moma['ExhibitionBeginDate'].memory_usage())
print(moma['ExhibitionEndDate'].memory_usage())

## Mission 14

obj_cols = moma.select_dtypes(include=['object'])

for col in obj_cols.columns:
    unique_total = len(obj_cols[col].unique())
    total_all = len(obj_cols[col])
    if (unique_total / total_all) < 0.5:
        moma[col] = moma[col].astype('category')
print(moma.info(memory_usage='deep'))

## Mission 15

keep_cols = ['ExhibitionID', 'ExhibitionNumber', 'ExhibitionBeginDate', 'ExhibitionEndDate', 'ExhibitionSortOrder', 'ExhibitionRole', 'ConstituentType', 'DisplayName', 'Institution', 'Nationality', 'Gender']

moma = pd.read_csv('moma.csv', parse_dates=["ExhibitionBeginDate", "ExhibitionEndDate"], usecols=keep_cols)
print(moma.memory_usage(deep=True).sum() / (1024*1024))