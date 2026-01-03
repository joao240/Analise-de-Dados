from src.extract import extract_data
from src.transform import calculation_total_value
import pandas as pd

def main():
    df = extract_data()
    df = calculation_total_value(df)
    print(df)
    return df

def total_value(df):
    if 'TOTAL_VALUE' in df.columns:
        faturamento_total = df['TOTAL_VALUE'].sum()
    else:
        faturamento_total = (df['QUANTITYORDERED'] * df['PRICEEACH']).sum()
    print(f"Faturamento total: {faturamento_total}")

def produtos_mais_vendidos(df):
    print("\n🏆 TOP 10 PRODUTOS MAIS VENDIDOS:")
    ranking = df.groupby('PRODUCTCODE')['QUANTITYORDERED'].sum().sort_values(ascending=False)
    print(ranking.head(10))

def paises_com_mais_vendas(df):
    print("\n🌍 TOP 10 PAÍSES COM MAIS VENDAS:")
    ranking = df.groupby('COUNTRY')['QUANTITYORDERED'].sum().sort_values(ascending=False)
    print(ranking.head(10))

def evolucao_vendas_mensal(df):
    df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'])
    df['YEAR_MONTH'] = df['ORDERDATE'].dt.to_period('M')
    vendas_mensais = df.groupby('YEAR_MONTH')['TOTAL_VALUE'].sum()
    print("\n📈 EVOLUÇÃO DAS VENDAS MENSAIS:")
    print(vendas_mensais.head(10))
    
def ticket_medio(df):
    faturamento_total = df['TOTAL_VALUE'].sum()
    numero_pedidos = df['ORDERNUMBER'].nunique()
    ticket_medio = faturamento_total / numero_pedidos
    print(f"\n🎟️ TICKET MÉDIO: {ticket_medio}")
    
