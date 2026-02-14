# Converting String to Numeric
import pandas as pd
df = pd.DataFrame({'Age':['25', '30', '22', '28']})
print(df.info())

print('*'*20)
print(df.isnull().sum())

print('*'*20)
df['Age'] = pd.to_numeric(df['Age'])
print(df)

# ------------------------------------------------------

# With Invalid Data
df = pd.DataFrame({'Age': ['25', '30', 'unknown', '28']})
print(f'Before Conversion: \n{df}')

df['Age'] = pd.to_numeric(df['Age'], errors = 'coerce')
print(f'\nAfter Converion: \n{df}')

# Treating the missing data
df['Age'].fillna(df['Age'].mean(), inplace = True)
print(f'\nAfter Treating Missing data: \n{df}')