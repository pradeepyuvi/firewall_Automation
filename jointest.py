import pandas as pd
import numpy as np
from operator import itemgetter
import openpyxl
import csv

df3 = pd.ExcelFile('firewall3.csv')
sheet_names=['firewall3']
#sheet2=df3.sheet_names
df5=pd.DataFrame()
#print(sheet2)

for i in sheet_names:

     df4= pd.read_csv(df3, sheet_name=i,usecols = "A", names=['env'])
     df5 = df5.append(df4)     
  
print(df5)

# with open('countries1.csv', 'w', encoding='UTF8', newline='') as f:
#     writer = csv.writer(f)

#     # write the header
#     writer.writerow(df5)

