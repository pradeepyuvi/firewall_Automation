import csv
from turtle import pd
import pandas as pd

df=pd.read_csv(r'firewall3.csv')
sheet_names=['firewall3']
#sheet1=df.sheet_names
df2=pd.DataFrame()
# print(df)

for i in sheet_names:
     df1= pd.read_excel(df, sheet_name=i,usecols = "A",names=['envvv'])
     df2 = df2.append(df1)
 
print(df2)
# with open('countries1.csv', 'w', encoding='UTF8', newline='') as f:
#     writer = csv.writer(f)

#     # write the header
#     writer.writerow(df2)

#     # # write the data
#     # writer.writerow(data)