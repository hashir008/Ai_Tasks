import pandas as pd

df = pd.read_csv('smartphones.csv')
                 
df[df.select_dtypes(include='number').columns] = df.select_dtypes(include='number').fillna(df.mean(numeric_only=True))

for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].fillna(df[col].mode()[0])

print("datatype before conversion:")
print(df.dtypes)

for col in df.select_dtypes(include='float').columns:
    df[col] = df[col].astype(int)

print("datatype after converison")
print(df.dtypes)
