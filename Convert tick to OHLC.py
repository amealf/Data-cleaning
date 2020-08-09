# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 19:39:42 2020

@author: aafym
"""

import pandas as pd
import numpy as np

df = pd.read_csv('result.csv', usecols=['day','time','price'])
df['day_time'] = df['day'].map(str) + ' ' + df['time']

df.index = pd.to_datetime(df['day_time'])
df.drop(['day','time','day_time'],axis=1,inplace=True)
print(df)
#df.to_csv('df.csv')

df1 = df.resample('20S').ohlc()
diffs = np.setdiff1d(df1.index, df.index)
df3 = df1[~np.in1d(df1.index, diffs)]
df3.ffill()
print(df3)


#data = left_msg[(pd.to_datetime(left_msg['Time'] ,format = '%H:%M:%S')>= pd.to_datetime('16:23:42',format = '%H:%M:%S')) & (pd.to_datetime(left_msg['Time'] ,format = '%H:%M:%S') <= pd.to_datetime('16:23:52',format = '%H:%M:%S'))]
#


df3.to_csv('clean_data.csv')