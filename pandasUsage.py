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

left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})
right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})
print("left = pd.DataFrame()\n{}\n----------".format(left))
print("right = pd.DataFrame()\n{}\n----------".format(right))
print("pd.merge(left, right, on='key')\n{}\n----------".format(pd.merge(left, right, on='key')))



