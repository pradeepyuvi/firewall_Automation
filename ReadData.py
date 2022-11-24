from csv import excel
import pandas as pd
import numpy as np
from operator import itemgetter
import csv

df = pd.ExcelFile('firewall1.xlsx')
df3 = pd.ExcelFile('firewall2.xlsx')
# header="envin"
sheet1=df.sheet_names
df2=pd.DataFrame()
#print(sheet1)
sheet2=df3.sheet_names
df5=pd.DataFrame()
#print(sheet2)

for i in sheet1:
     df1= pd.read_excel(df, sheet_name=i,usecols = "A",names=['ipaddress'])
     df2 = df2.append(df1)
 

for i in sheet2:

     df4= pd.read_excel(df3, sheet_name=i,usecols = "B",names=['names'])
     df5 = df5.append(df4)     
  
print(df2)
print(df5)

with open('countries2.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(df5)