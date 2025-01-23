import pandas as pd
import numpy as np
# default olarak 0,1,2 diye index ataması yapılır

data=[10,20,30]
s=pd.Series(data)
# print("Series\n",s)

data2={'name': ['Ali', 'Ayşe', 'Mehmet'],
        'age': [25, 30, 35],
        'price':[12.3,10.3,32.2]}
df=pd.DataFrame(data2)
# print("Data Frame\n",df)

s=pd.Series(data,index=['name','date','shares'])
# print(s)
# print(s[['shares','name']])

df['owner']='Unknown'
df.index=['one','two','three']
# print("Data Frame\n",df)
# print(df['name'])
# print(df.loc['one']) #key üzerinden erişim
# print(df.iloc[0]) # index üzerinden erişim


# array=np.arange(9).reshape(3,-1)
# # print(array)
# print("\n")
# frame=pd.DataFrame(array,index=['r1','r2','r3'],columns=['c1','c2','c3'])
# print(frame)
# print(frame['c1'])
# print(frame.loc['r1'])
# print(frame['c1']['r1']) 
# print(frame[['c1','c2']]) 
# print(frame.iloc[:2])