import pandas as pd
import numpy as np

# Replacing Missing Value with Mean - for Numericals
df = pd.DataFrame({'Age':[25,30,None,22,28]})
print(f'Data Before: \n{df}')
print(f'\nChecking Missing Data Before: \n{df.isnull().sum()}')

df['Age'].fillna(df['Age'].mean(), inplace=True)
print(f'\nChecking Missing Data After: \n{df.isnull().sum()}')

print(f'\nAfter Treating Missing Data: \n{df}')

# ------------------------------------------------------------

# Replacing with the Median
df1 = pd.DataFrame({'Salary': [50000,60000,None,55000,52000]})
df1.info()
df1.isnull().sum()
df1['Salary'].fillna(df1['Salary'].median(), inplace = True)

# ------------------------------------------------------------

# Replacing with Modal Value
import pandas as pd
df = pd.DataFrame({'Color':['Red', 'Blue', None, 'Blue', 'Red']})
df.info()
df.isnull().sum()

mode_value = df['Color'].mode()[0]
df['Color'].fillna(mode_value, inplace = True)