import pandas as pd
import numpy as np
# from operator import itemgetter
# import openpyxl
import csv
# import json

df1 = pd.read_csv('firewall3.csv')
# print(df1)
df2 = pd.read_csv('firewall4.csv')
# print(df2)

df3 = pd.merge(df1, df2, on ='ipaddress',how ='left')
 
print(df3)
df6=df3.to_numpy()
# print(df6)
# df4=df3.to_json()
# df5=(json.loads(df4))
# print(df5)
for i in df6:
#     print(i[1]=='unknown')
    if(i[1]=='uknown'):
        print(i)
        i[1]=i[4]
# headers = ['ipaddress', 'hostname', 'environment', 'CI','host'] 
with open('countries7.csv', 'w', newline='') as f:
      
    # using csv.writer method from CSV package
    write = csv.writer(f)
      
    write.writerow(df3)
    write.writerows(df6)




# print(df6)
# df7=pd.DataFrame()
# df7=df6.tolist()
# # df7= df7.append(df6)
# print(df7)

# with open('countries3.csv', 'w', encoding='UTF8', newline='') as f:
#     writer = csv.writer(f)

#     # write the header
#     writer.writerow(df6)

# #     # write the data
# #     writer.writerow(df2)

