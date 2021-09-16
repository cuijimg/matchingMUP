# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 15:48:50 2021

@author: F-CUI
"""

import pandas as pd
from pathlib import Path
from pandas import DataFrame

file1 = Path(r'I:\!Hiwis\f-cui\matchingMUP\mupdata.csv')
file2 = Path (r'I:\!Hiwis\f-kraeme\Internship\readability_sample_withoutnas.csv')
file3 = Path(r'I:\!Hiwis\f-cui\matchingMUP\readability_sample_wonas_wwz.csv.csv')
df1 = pd.read_csv(file1,usecols=['crefo','wzdig5'], encoding='utf-8')
print(df1,type(df1))

df2 = pd.read_csv(file2, encoding='utf-8')
df2['wz'] = ''
print(df2)

# for index,row1 in df2.iterrows():
#     print(index)
#     for ind,row in df1.iterrows():
#         print(ind)
#         if str(row1['firm identifier'])[:10] == str(row['crefo']):
#             df2.loc[index,'wz'] = row['wzdig5']
#             break
print(type(df1.loc[2,'crefo']))
for index,row in df2.iterrows():
    print(index)
    print(str(row['firm identifier'])[:10])
    # print(df1['wzdig5'][df1['crefo'] ==int(str(row['firm identifier'])[:10])])

    try:
        wz = df1['wzdig5'][df1['crefo']==int(str(row['firm identifier'])[:10])].values[0]
        df2.loc[index,'wz'] = wz
    except Exception as e:
        print(index, e)

df2.to_csv(file3, encoding = 'utf-8')