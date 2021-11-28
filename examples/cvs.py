import pandas as pd
import numpy as np

out = pd.read_csv('data/data.csv')
# out = pd.read_excel('data/data1.xlsx')

for index, row in out.iterrows():
    print(row)
    if index > 3:
        break

print(out.head(5))
print(out.tail(3))

print(out.describe())

print(out.index)
print(out.to_numpy())

