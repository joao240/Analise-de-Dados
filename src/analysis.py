from extract import extract_data

def main():
    df = extract_data()
    print(df)
    return df

def total_value(df):
    quantidade = df['QUANTITYORDERED']
    preco = df['PRICEEACH']
    faturamento_total = (quantidade * preco).sum()
    print(faturamento_total)

def produtos_mais_vendidos(df):
    print("\n🏆 TOP 10 PRODUTOS MAIS VENDIDOS:")
    ranking = df.groupby('PRODUCTCODE')['QUANTITYORDERED'].sum().sort_values(ascending=False)
    print(ranking.head(10))
# finalizar aqui pra baixo
def paises_com_mais_vendas(df):
    vendas_por_pais = df.groupby('COUNTRY')['TOTAL_VALUE'].sum()
    vendas_por_pais = vendas_por_pais.sort_values(ascending=False)
    print(vendas_por_pais.head(10).info())
    
if __name__ == "__main__":
    meu_df = main()
    total_value(meu_df)
    produtos_mais_vendidos(meu_df)