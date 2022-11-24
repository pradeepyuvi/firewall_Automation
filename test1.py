import pandas as pd
import numpy as np
from operator import itemgetter
import openpyxl
import csv

df1 = pd.read_csv('firewall3.csv')
# print(df1)
df2 = pd.read_csv('firewall4.csv')
# print(df2)

df3 = pd.merge(df1, df2, on ='ipaddress',how ='left')
 
# print(df3)

df4=df3.to_dict()
# print(df4)
for i in df3:
    print(i)
