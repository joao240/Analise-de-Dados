import pandas as pd

# Ler o arquivo CSV com pandas.

df = pd.read_csv('sales_data_sample.csv', encoding='latin-1') # encoding definido prara evitar erros
print(df.head())

# Lidando com contagem de valores ausentes
print("Valores ausentes por coluna:")
print(df.isnull().sum())

# Validar e converter tipos de dados
df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'])

df['MONTHID'] = df['MONTHID'].astype(int)

df['YEARID'] = df['YEARID'].astype(int)

print("\nNOME E TIPO: =========================")
print(df.dtypes)
