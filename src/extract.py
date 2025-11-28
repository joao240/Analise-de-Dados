import pandas as pd

def extract_data():
    # Ler o arquivo CSV com pandas.
    df = pd.read_csv('sales_data_sample.csv', encoding='latin-1') # encoding definido prara evitar erros
    print(df.head())
    
    # Lidando com contagem de valores ausentes
    print("Valores ausentes por coluna:")
    print(df.isnull().sum())

    # Validar e converter tipos de dados
    df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'], errors='coerce')

    df['MONTH_ID'] = df['MONTH_ID'].astype(int)

    df['YEAR_ID'] = df['YEAR_ID'].astype(int)

    df['PRODUCTLINE'] = df['PRODUCTLINE'].astype('category')

    df['STATUS'] = df['STATUS'].astype('category')

    df['CUSTOMERNAME'] = df['CUSTOMERNAME'].astype(str)

    df['CITY'] = df['CITY'].astype(str)

    df['STATE'] = df['STATE'].astype(str)

    df['COUNTRY'] = df['COUNTRY'].astype(str)

    df['TERRITORY'] = df['TERRITORY'].astype(str)

    df['CONTACTLASTNAME'] = df['CONTACTLASTNAME'].astype(str)

    df['CONTACTFIRSTNAME'] = df['CONTACTFIRSTNAME'].astype(str)

    df['DEALSIZE'] = df['DEALSIZE'].astype(str)

    print("\nNOME E TIPO: =========================")
    print(df.dtypes)

    return df