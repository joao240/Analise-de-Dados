import pandas as pd


def transform_data(df: pd.DataFrame, inplace: bool = True) -> pd.DataFrame:

    

    # Calcular o valor total do pedido e colocando no DataFrame
    quantidade = pd.to_numeric(df.get('QUANTITYORDERED'), errors='coerce')
    preco = pd.to_numeric(df.get('PRICEEACH'), errors='coerce')
    df['TOTAL_VALUE'] = quantidade * preco

    # Tratar outliers.
    # ---- OUTLIERS QUANTITYORDERED ----
    Q1_qtd = df['QUANTITYORDERED'].quantile(0.25)
    Q3_qtd = df['QUANTITYORDERED'].quantile(0.75)
    IQR_qtd = Q3_qtd - Q1_qtd
    baixo_qtd = Q1_qtd - 1.5 * IQR_qtd
    alto_qtd = Q3_qtd + 1.5 * IQR_qtd

    # ---- OUTLIERS PRICEEACH ----
    Q1_preco = df['PRICEEACH'].quantile(0.25)
    Q3_preco = df['PRICEEACH'].quantile(0.75)
    IQR_preco = Q3_preco - Q1_preco
    baixo_preco = Q1_preco - 1.5 * IQR_preco
    alto_preco = Q3_preco + 1.5 * IQR_preco

    # Removendo valores fora dos limites
    df = df[
        (df['QUANTITYORDERED'] >= baixo_qtd) &
        (df['QUANTITYORDERED'] <= alto_qtd) &
        (df['PRICEEACH'] >= baixo_preco) &
        (df['PRICEEACH'] <= alto_preco)
    ]  

    return df
