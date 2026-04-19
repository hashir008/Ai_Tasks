import pandas as pd

df = pd.read_csv('smartphones.csv)
                 
df[df.select_dtypes(include='number') = df.select_dtypes(include='number').fillna(df.mean(numeric_only="True"))

for col in df[df.select_dtypes(include='object').columns :
    df[col] = df[col].fillna(df[col].mode()[0])
      
