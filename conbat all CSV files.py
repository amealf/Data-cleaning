#合併後仍需用excel排序時間

import os
import pandas as pd
import glob
csv_list = glob.glob('*.csv') #查看同文件夾下的csv文件數
print(u'共發現%s個CSV文件'% len(csv_list))
print(u'正在處理............')
for i in csv_list: #循環讀取同文件夾下的csv文件
    fr = open(i,'rb').read()
    with open('result.csv','ab') as f: #將結果保存爲result.csv
        f.write(fr)
print(u'合併完畢！')

# 还有对index进行order