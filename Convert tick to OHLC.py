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
#print(df)
#df.to_csv('df.csv')

df_resample = df.resample('20S').ohlc() # 将tick转为20s的OHLC。此操作会在index中自动填充不存在的日期，需要进一步操作将其删除
diffs = np.setdiff1d(df_resample.index, df.index) # 两者index的区别
df_outcome = df_resample[~np.in1d(df_resample.index, diffs)] # 在df_resmaple里删掉df中没有的index
df_outcome = df_outcome.ffill() # 空缺值继承前值
#print(df_outcome)

df_outcome.to_csv('convert outcome.csv')
#open
