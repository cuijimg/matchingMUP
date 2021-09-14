# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 15:48:50 2021

@author: F-CUI
"""

import pandas as pd
from pathlib import Path

file1 = Path(r'I:\!Hiwis\f-cui\mupdata.csv')
file2 = Path (r'I:\!Hiwis\f-kraeme\Internship\readability_sample_withoutnas.csv')

df1 = pd.read_csv(file1,usecols=['crefo','wzdig5'], encoding='utf-8')
print(df1)
df2 = pd.read_csv(file2, encoding='utf-8')
df2['wz'] = ''

# for i in range(len(df2)):
#     df2.loc[i,'wz'] = df1.loc