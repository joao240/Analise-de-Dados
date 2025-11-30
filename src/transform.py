import pandas as pd

def calculation_total_value(df: pd.DataFrame) -> pd.DataFrame:
    # Calcular o valor total do pedido e colocando no DataFrame
    quantidade = pd.to_numeric(df.get('QUANTITYORDERED'), errors='coerce')
    preco = pd.to_numeric(df.get('PRICEEACH'), errors='coerce')
    df['TOTAL_VALUE'] = quantidade * preco
    return df

def Addressing_outliers(df: pd.DataFrame) -> pd.DataFrame:

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
    ].copy()

    return df
def handle_empty_values(df: pd.DataFrame) -> pd.DataFrame:
    # Preencher valores vazios de forma segura
    # Números -> mediana
    for col in df.select_dtypes(include=['number']).columns:
        if df[col].isna().any():
            df[col] = df[col].fillna(df[col].median())

    # Categóricas -> adicionar categoria 'Unknown' e preencher
    for col in df.select_dtypes(include=['category']).columns:
        df[col] = df[col].cat.add_categories(['Unknown'])
        if df[col].isna().any():
            df[col] = df[col].fillna('Unknown')

    # Objetos/texto -> 'Unknown'
    for col in df.select_dtypes(include=['object']).columns:
        if df[col].isna().any():
            df[col] = df[col].fillna('Unknown')

    # Normalizar textos (lowercase e strip) nas colunas de texto/categoria
    for col in df.select_dtypes(include=['object', 'category']).columns:
        df[col] = df[col].astype(str).str.lower().str.strip()

    return df


