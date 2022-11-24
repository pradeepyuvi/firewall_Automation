import pandas as pd
import numpy as np
import csv

df1 = pd.read_csv("firewall3.csv")
df2 = pd.read_csv("firewall4.csv")
df3 = df1.merge(df2[['ipaddress', 'Environment', 'Primarly_related_CI', 'Hostname']], on = 'ipaddress', how = 'left')
# print(df3)

for key,values in df3.iterrows():
    
    # print(key)
    # print(values)

    if values['Remote_Host'] == 'unknown':

        # df3 = df3.iloc[key].replace(to_replace= unknown, value = values['Hostname'])
        df3.loc[key].at['Remote_Host'] = values['Hostname']

print(df3)
