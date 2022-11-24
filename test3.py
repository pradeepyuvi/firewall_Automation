import pandas as pd
import numpy as np
import csv


df1 = pd.read_csv('firewall3.csv')
# print(df1)
df2 = pd.read_csv('firewall4.csv')
# print(df2)

df3 = pd.merge(df1, df2, on ='ipaddress',how ='left')
 
print(df3)
df6=df3.to_numpy()


for i in df6:
    if(i[1]=='uknown'):
        i[1]=i[4]

with open('countries7.csv', 'w', newline='') as f:
    write = csv.writer(f)     
    write.writerow(df3)
    write.writerows(df6)



