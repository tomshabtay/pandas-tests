# import pandas as pd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# load file
data = pd.read_csv("vgsales.csv")

# print(data[['Platform', 'Year']].head()['Platform'].shape)
# print(data['Platform'].shape)
thres = 1.5
jpSalesGreaterThenThreshord = data['JP_Sales'] > thres
jpSalesLowerThenThreshord = data['JP_Sales'] < thres
jpSalesLowerThenOne = data['JP_Sales'] < 1
nes = data['Platform'] == 'NES'
wii = data['Platform'] == 'Wii'

nesOrWii = data['Platform'].isin(['NES', 'Wii'])

query = jpSalesGreaterThenThreshord & nesOrWii

data.loc[query, ['new']] = 0
print(data[query][['JP_Sales', 'Platform', 'new']].head())
col1 = data[query]['Platform']
col2 = data[query]['JP_Sales']
plt.bar(col1, col2)
plt.show()
# print(data.loc[query, ['JP_Sales', 'Platform']].head())
# print(data[jpSalesLowerThenThreshord]['JP_Sales'].head())

# print(data.info())


# print file
# file = open("vgsales.csv", "r")
# print(file.read())
