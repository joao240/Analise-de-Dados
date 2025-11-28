import pandas as pd
from sqlalchemy import create_engine
import pymysql
from extract import extract_data

# O PyMySQL é importado mas não é usado diretamente,
# ele é o driver que o SQLAlchemy usa por baixo dos panos (mysql+pymysql)

## 1. DADOS DE CONEXÃO E DATAFRAME
# ----------------------------------

# ⚠️ Substitua 'seu_usuario', 'sua_senha' e 'seu_banco_de_dados' pelos seus dados
DB_USER = "root"
DB_HOST = "localhost" 
DB_PORT = "3306" 
DB_NAME = "analiseDados" 
TABELA = "sales"

# Data frame
df = extract_data()
print(df.head())

## 2. CONFIGURAÇÃO DA CONEXÃO E INSERÇÃO
# ---------------------------------------

try:
    # 🔗 Cria a string de conexão no formato 'dialect+driver://user:pass@host:port/database'
    CONN_STRING = f"mysql+pymysql://{DB_USER}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    # ⚙️ Cria o engine de conexão usando o SQLAlchemy
    engine = create_engine(CONN_STRING)

    # 🚀 Chama to_sql() para criar a tabela e inserir os dados
    df.to_sql(
        name=TABELA,       # Nome da tabela será 'sales'
        con=engine,         # Usa o engine criado
        if_exists='replace', # Ação: Se a tabela existir, apaga e recria. Se não, apenas cria.
        index=False         # Não inclui o índice do DataFrame como coluna na tabela
    )

    print(f"✅ Sucesso! O DataFrame foi inserido na tabela '{TABELA}' do MySQL.")
    print("Verifique seu banco de dados.")

except Exception as e:
    print("❌ ERRO! Não foi possível conectar ou inserir os dados.")
    print(f"Detalhes do erro: {e}")