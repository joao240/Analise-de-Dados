# 📊 Análise de Dados de Vendas Globais — Projeto ETL em Python

## 📌 Visão Geral
Este projeto consiste em um **pipeline completo de ETL (Extract, Transform, Load)** aplicado a um conjunto de dados de **vendas globais**, finalizando com uma etapa de **análise e visualização de dados**.

O objetivo principal foi **consolidar conceitos fundamentais de dados na prática**, passando por todas as etapas de um fluxo real: desde a leitura e limpeza dos dados até análise, visualização e validação do código com testes automatizados.

---

## 🧠 Objetivos do Projeto
- Aplicar um pipeline **ETL completo em Python**
- Tratar dados reais (valores nulos, outliers e padronização)
- Armazenar dados tratados em um banco **MySQL**
- Realizar análises e gerar gráficos
- Implementar **testes automatizados com PyTest**
- Organizar o código seguindo o **Princípio da Responsabilidade Única**

---
## 🗂️ Estrutura do Projeto

- ANALISE-DE-DADOS/
- │
- ├── src/
- │ ├── extract.py
- │ ├── transform.py
- │ ├── load.py
- │ ├── analysis.py
- │ └── utils.py
- │
- ├── tests/
- │ └── test_transform.py
- │
- ├── data/
- │ └── sales_data_sample.csv
- │
- ├── images/
- │ └── graficos/
- │
- ├── README.md
- └── requirements.txt


## 🔄 Pipeline ETL

### 1️⃣ Extract
- Leitura do arquivo CSV de vendas
- Inspeção de valores ausentes
- Conversão e validação de tipos de dados

### 2️⃣ Transform
- Criação da métrica `TOTAL_VALUE`
- Tratamento de outliers utilizando IQR
- Preenchimento seguro de valores nulos
- Normalização de textos (lowercase e strip)
- Código modular, com funções de responsabilidade única

### 3️⃣ Load
- Armazenamento dos dados tratados em **MySQL**
- Uso de `SQLAlchemy` + `pandas.to_sql()`
- Criação/substituição da tabela `sales`

### 4️⃣ Analysis
- Cálculo de métricas de negócio
- Rankings e análises temporais
- Visualizações com **Matplotlib**
- Geração de gráficos:
  - Top produtos mais vendidos
  - Países com mais vendas
  - Evolução das vendas mensais
  - Ticket médio

---

## 📊 Principais Métricas
- Faturamento total
- Ticket médio por pedido
- Top 10 produtos mais vendidos
- Top 10 países com maior volume de vendas
- Evolução das vendas ao longo do tempo

---

## 📈 Visualizações
Os gráficos foram gerados com **Matplotlib**, aprendido do zero durante o projeto, e exportados em formato PNG para facilitar análise e documentação.

---

## 🧪 Testes Automatizados
O projeto inclui **testes unitários com PyTest**, cobrindo:
- Cálculo correto do valor total
- Remoção adequada de outliers
- Tratamento de valores nulos
- Normalização de dados textuais

Os testes garantem **confiabilidade e qualidade** no pipeline de transformação.

---

## ⚙️ Tecnologias Utilizadas
- Python
- Pandas
- Matplotlib
- MySQL
- SQLAlchemy
- PyTest

---

## ▶️ Como Executar o Projeto

### 1. Clonar o repositório
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd ANALISE-DE-DADOS
