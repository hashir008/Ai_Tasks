import pandas as pd

df = pd.read_csv('Smartphones.csv')

print("Shape of Dataset:", df.shape)

print("\nFirst 5 Rows:")
print(df.head())

print("\nLast 5 Rows:")
print(df.tail())

print('rows: ', df.shape[0])
print('columns: ', df.shape[1])

print("\nNull Values:")
print(df.isnull().sum())

print("\nDatatypes:")
print(df.dtypes)
