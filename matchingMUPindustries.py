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

for index,row1 in df2.iterrows():
    print(index)
    for ind,row in df1.iterrows():
        print(ind)
        if str(row1['firm identifier'])[:10] == str(row['crefo']):
            df2.loc[index,'wz'] = row['wzdig5']
            break

df2.to_csv(file3, encoding = 'utf-8')