import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("-----------\n")
s = pd.Series([1,3,5,np.nan,6,8])
print("pd.Series \n{}\n-----------".format(s))

dates = pd.date_range('20130101', periods=6)
print("date_range \n{}\n----------".format(dates))

df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print("random DataFrame of array\n{}\n----------".format(df))

df2 = pd.DataFrame({ 'A' : 1.,
    'B' : pd.Timestamp('20130102'),
    'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
    'D' : np.array([3] * 4,dtype='int32'),
    'E' : pd.Categorical(["test","train","test","train"]),
    'F' : 'foo' })

print("DataFrame of dict \n{}\n----------".format(df2))

print("df2.dtypes  \n{}\n----------".format(df2.dtypes))


# View
print("df.head(3) \n{}\n----------".format(df.head(3)))
print("df.tail(3) \n{}\n----------".format(df.tail(3)))
print("df.index \n{}\n----------".format(df.index))
print("df.columns \n{}\n----------".format(df.columns))
print("df.values \n{}\n----------".format(df.values))
print("df.describe() \n{}\n----------".format(df.describe()))
print("df.T \n{}\n----------".format(df.T))
print("df.sort_index() \n{}\n----------".format(df.sort_index(axis=1, ascending=False)))
print("df.sort_values() \n{}\n----------".format(df.sort_values(by='B')))

# Selection
print("df['A'] \n{}\n----------".format(df['A']))
print("df[0:3] \n{}\n----------".format(df[0:3]))
print("df['20130102':'20130104'] \n{}\n----------".format(df['20130102':'20130104']))
print("df.loc[dates[0]] \n{}\n----------".format(df.loc[dates[0]]))
print("df.loc[:,['A','B']] \n{}\n----------".format(df.loc[:,['A','B']]))
print("df.loc['20130102':'20130104',['A','B']] \n{}\n----------".format(df.loc['20130102':'20130104',['A','B']]))
print("df.loc['20130102',['A','B']] \n{}\n----------".format(df.loc['20130102',['A','B']]))
print("df.loc[dates[0],'A'] \n{}\n----------".format(df.loc[dates[0],'A']))
print("df.at[dates[0],'A'] \n{}\n----------".format(df.at[dates[0],'A']))
print("df.iloc[3] \n{}\n----------".format(df.iloc[3]))
print("df.iloc[3:5,0:2] \n{}\n----------".format(df.iloc[3:5,0:2]))
print("df.iloc[[1,2,4],[0,2]] \n{}\n----------".format(df.iloc[[1,2,4],[0,2]]))
print("df.iloc[1:3,:] \n{}\n----------".format(df.iloc[1:3,:]))
print("df.iloc[:,1:3] \n{}\n----------".format(df.iloc[:,1:3]))
print("df.iloc[1,1] \n{}\n----------".format(df.iloc[1,1]))
print("df.iat[1,1] \n{}\n----------".format(df.iat[1,1]))

# Boolean index
print("df[df.A > 0] \n{}\n----------".format(df[df.A > 0]))
print("df[df > 0] \n{}\n----------".format(df[df > 0]))

df2 = df.copy()
df2['E'] = ['one', 'one', 'two', 'three', 'four', 'three']
print("df2 is \n{}\n----------".format(df2))
print("df2[df2['E'].isin(['two','four'])] \n{}\n----------".format(df2[df2['E'].isin(['two','four'])]))

# Setting

s1 = pd.Series([1,2,3,4,5,6], index=pd.date_range('20130102', periods=6))
print("pd.Series([1,2,3,4,5,6], index=pd.date_range('20130102', periods=6)) \n{}\n----------".format(s1))
df['F'] = s1
print("add s1 to df['F'] ---- df['F'] = s1 \n{}\n----------".format(df))

df.at[dates[0],'A'] = 0
print("df.at[dates[0],'A'] = 0\n{}\n----------".format(df))

df.iat[0,1] = 0
print("df.iat[0,1] = 0 \n{}\n----------".format(df))

df.loc[:,'D'] = np.array([5] * len(df))
print(len(df))
print("assigning with a NumPy array\ndf.loc[:,'D'] = np.array([5] * len(df)) \n{}\n----------".format(df))

df2 = df.copy()
df2[df2 > 0] = -df2
print("df2 = df.copy()\ndf2[df2 > 0] = -df2\n{}\n----------".format(df2))

df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])
df1.loc[dates[0]:dates[1],'E'] = 1
print("df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])\ndf1.loc[dates[0]:dates[1],'E'] = 1\n{}\n----------".format(df1))

print("df1.dropna(how='any')\n{}\n----------".format(df1.dropna(how='any')))

print("df1.fillna(value=5)\n{}\n----------".format(df1.fillna(value=5)))

print("pd.isna(df1)\n{}\n----------".format(pd.isna(df1)))

# Stats
print(df)
print("df.mean()\n{}\n----------".format(df.mean()))
print("df.mean(1)\n{}\n----------".format(df.mean(1)))

s = pd.Series([1,3,5,np.nan,6,8], index=dates).shift(2)
print("pd.Series([1,3,5,np.nan,6,8], index=dates).shift(2)\n{}\n----------".format(s))


print("df.sub(s, axis='index')\n{}\n----------".format(df.sub(s, axis='index')))

print("df.apply(np.cumsum)\n{}\n----------".format(df.apply(np.cumsum)))
print("df.apply(lambda x: x.max() - x.min())\n{}\n----------".format(df.apply(lambda x: x.max() - x.min())))

s = pd.Series(np.random.randint(0, 7, size=10))
print("s=pd.Series(np.random.randint(0, 7, size=10))\n{}\n----------".format(s))
print("s.value_counts()\n{}\n----------".format(s.value_counts()))
s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
print("s.str.lower()\n{}\n----------".format(s.str.lower()))


df = pd.DataFrame(np.random.randn(10, 4))
print("df = pd.DataFrame(np.random.randn(10, 4))\n{}\n----------".format(df))
pieces = [df[:3], df[3:7], df[7:]]
print("pieces = [df[:3], df[3:7], df[7:]]\n{}\n----------".format(pieces))
pd.concat(pieces)
print("pd.concat(pieces)\n{}\n----------".format(pd))

print("SQL style merges. See the Database style joining section.\n")
left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})
right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})
print("left = pd.DataFrame()\n{}\n----------".format(left))
print("right = pd.DataFrame()\n{}\n----------".format(right))
print("pd.merge(left, right, on='key')\n{}\n----------".format(pd.merge(left, right, on='key')))

left = pd.DataFrame({'key': ['foo', 'bar'], 'lval': [1, 2]})
right = pd.DataFrame({'key': ['foo', 'bar'], 'rval': [4, 5]})
print("left = pd.DataFrame()\n{}\n----------".format(left))
print("right = pd.DataFrame()\n{}\n----------".format(right))
print("pd.merge(left, right, on='key')\n{}\n----------".format(pd.merge(left, right, on='key')))


print("Append rows to a dataframe. See the Appending section.\n")
df = pd.DataFrame(np.random.randn(8, 4), columns=['A','B','C','D'])
print("pd.DataFrame(np.random.randn(8, 4), columns=['A','B','C','D'])\n{}\n----------".format(df))
s = df.iloc[3]
print("s = df.iloc[3]\n{}\n----------".format(s))
print("df.append(s, ignore_index=True)\n{}\n----------".format(df.append(s, ignore_index=True)))

'''
By “group by” we are referring to a process involving one or more of the following steps:
Splitting the data into groups based on some criteria
Applying a function to each group independently
Combining the results into a data structure
'''

df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar',
                         'foo', 'bar', 'foo', 'foo'],
                   'B': ['one', 'one', 'two', 'three',
                         'two', 'two', 'one', 'three'],
                   'C': np.random.randn(8),
                   'D': np.random.randn(8)})

print("df\n{}\n----------".format(df))
print("df.groupby('A').sum()\n{}\n----------".format(df.groupby('A').sum()))

print("df.groupby(['A','B']).sum()\n{}\n----------".format(df.groupby(['A','B']).sum()))

print("See the sections on Hierarchical Indexing and Reshaping.\n")

tuples = list(zip(*[['bar', 'bar', 'baz', 'baz',
                    'foo', 'foo', 'qux', 'qux'],
                    ['one', 'two', 'one', 'two',
                    'one', 'two', 'one', 'two']]))
index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])
df2 = df[:4]
print("df2\n{}\n----------".format(df2))

print("The stack() method “compresses” a level in the DataFrame’s columns.")
stacked = df2.stack()
print("stacked = df2.stack()\n{}\n----------".format(stacked))
print("stacked.unstack()\n{}\n----------".format(stacked.unstack()))
print("stacked.unstack(1)\n{}\n----------".format(stacked.unstack(1)))
print("stacked.unstack(0)\n{}\n----------".format(stacked.unstack(0)))

print("Pivot Tables.\n")

df = pd.DataFrame({'A' : ['one', 'one', 'two', 'three'] * 3,
                       'B' : ['A', 'B', 'C'] * 4,
                       'C' : ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
                       'D' : np.random.randn(12),
                       'E' : np.random.randn(12)})
print("df\n{}\n----------".format(df))

print("pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C'])\n{}\n----------".format(pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C'])))

print("Time Series.\n")

rng = pd.date_range('1/1/2012', periods=100, freq='S')
ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)
print(ts)
print(ts.resample('5Min'))
print("ts.resample('5Min').sum()\n{}\n----------".format(ts.resample('5Min').sum()))
rng = pd.date_range('3/6/2012 00:00', periods=5, freq='D')
print(rng)
ts = pd.Series(np.random.randn(len(rng)), rng)
print("ts = pd.Series(np.random.randn(len(rng)), rng)\n{}\n----------".format(ts))
ts_utc = ts.tz_localize('UTC')
print("ts_utc = ts.tz_localize('UTC')\n{}\n----------".format(ts_utc))
ts_utc.tz_convert('US/Eastern')
print("ts_utc.tz_convert('US/Eastern')\n{}\n----------".format(ts_utc.tz_convert('US/Eastern')))

rng = pd.date_range('1/1/2012', periods=5, freq='M')
ts = pd.Series(np.random.randn(len(rng)), index=rng)
print("pd.Series(np.random.randn(len(rng)), index=rng)\n{}\n----------".format(ts))
ps = ts.to_period()
print("ts.to_period()\n{}\n----------".format(ps))
print("ps.to_timestamp()\n{}\n----------".format(ps.to_timestamp()))

prng = pd.period_range('1990Q1', '2000Q4', freq='Q-NOV')
print(prng)
ts = pd.Series(np.random.randn(len(prng)), prng)
print(ts)
ts.index = (prng.asfreq('M', 'e') + 1).asfreq('H', 's') + 9
print(ts.index)
ts.head()
print(ts.head())

print("\nCategoricals.\n")
df = pd.DataFrame({"id":[1,2,3,4,5,6], "raw_grade":['a', 'b', 'b', 'a', 'a', 'e']})
df["grade"] = df["raw_grade"].astype("category")
print('df["raw_grade"].astype("category")\n{}\n----------'.format(df["grade"]))

df["grade"].cat.categories = ["very good", "good", "very bad"]
print(df["grade"])
print('df.sort_values(by="grade")\n{}\n----------'.format(df.sort_values(by="grade")))
print('df.groupby("grade").size()\n{}\n----------'.format(df.groupby("grade").size()))

print("\nPlotting\n")
ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()
ts.plot()
df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index,
        columns=['A', 'B', 'C', 'D'])
df = df.cumsum()
plt.figure()
df.plot()
plt.legend(loc='best')
df.to_csv('foo.csv')
df.to_hdf('foo.h5','df')
pd.read_hdf('foo.h5','df')
df.to_excel('foo.xlsx', sheet_name='Sheet1')
pd.read_excel('foo.xlsx', 'Sheet1', index_col=None, na_values=['NA'])