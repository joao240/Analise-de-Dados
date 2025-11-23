import pandas as pd


def transform_data(df: pd.DataFrame, inplace: bool = True) -> pd.DataFrame:
    quantidade = pd.to_numeric(df.get('QUANTITYORDERED'), errors='coerce')
    preco = pd.to_numeric(df.get('PRICEEACH'), errors='coerce')
    df['TOTAL_VALUE'] = quantidade * preco
    
    return df