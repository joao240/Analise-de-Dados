from src.extract import extract_data
from src.transform import calculation_total_value
import pandas as pd
import matplotlib.pyplot as plt

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
    ranking = df.groupby('PRODUCTCODE')['QUANTITYORDERED'].sum().sort_values(ascending=False).head(10)
    # 1 - Criar grafico
    plt.figure(figsize=(10,6)) # define o tamanho que vai ser o grafico 
    ranking.plot(kind='bar', color='skyblue') # Plota os dados como barras
    # 2 - Personalizar grafico
    plt.title('Top 10 Produtos Mais Vendidos') # Titulo do grafico
    plt.xlabel('Código do Produto') # Nome do eixo X
    plt.ylabel('Quantidade Vendida') # Nome do eixo Y
    plt.xticks(rotation=90) # Inclina os nomes para não amontoar
    # 3 - Exibir grafico
    plt.show() 
     
def paises_com_mais_vendas(df):
    ranking = df.groupby('COUNTRY')['QUANTITYORDERED'].sum().sort_values(ascending=False).head(10)

    plt.figure(figsize=(10, 8)) 
    
    # 1. Criar o gráfico de pizza
    ranking.plot(
        kind='pie', 
        autopct='%1.1f%%',      # Mostra a porcentagem dentro da fatia
        startangle=140,         # Gira o gráfico para começar em um ângulo melhor
        colors=plt.cm.Paired.colors # Usa uma paleta de cores variadas e bonitas
    )

    # 2. Personalizar
    plt.title('Participação dos Top 10 Países nas Vendas')
    plt.ylabel('') # Remove o nome da coluna que fica na vertical e atrapalha o grafico

    plt.show()

def evolucao_vendas_mensal(df):
    df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'])
    df['YEAR_MONTH'] = df['ORDERDATE'].dt.to_period('M')
    vendas_mensais = df.groupby('YEAR_MONTH')['TOTAL_VALUE'].sum()
    
    plt.figure(figsize=(12,5))

    vendas_mensais.index = vendas_mensais.index.astype(str)

    plt.plot(vendas_mensais.index, vendas_mensais.values, marker='o', linestyle='-')

    plt.title('Evolução das Vendas Mensais')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.xticks(rotation=45)
    plt.show()

def ticket_medio(df):
    faturamento_total = df['TOTAL_VALUE'].sum()
    numero_pedidos = df['ORDERNUMBER'].nunique()
    ticket_medio = faturamento_total / numero_pedidos
    print(f"\n🎟️ TICKET MÉDIO: {ticket_medio}")
    

