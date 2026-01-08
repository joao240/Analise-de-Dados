🛠️ Metodologia

O projeto foi estruturado em etapas bem definidas:

1. Extract

Leitura dos dados a partir de um arquivo CSV contendo informações de vendas.

Validação inicial dos dados e verificação de valores ausentes.

2. Transform

Conversão e validação de tipos de dados.

Tratamento de valores vazios.

Tratamento de outliers.

Criação da métrica TOTAL_VALUE, representando o valor total de cada venda.

3. Load

Armazenamento dos dados tratados em um banco MySQL.

Criação e substituição da tabela sales, garantindo consistência dos dados.

4. Analysis

Análise dos dados já limpos e consolidados.

Cálculo de métricas de negócio.

Criação de gráficos utilizando Matplotlib, aprendido do zero durante esta etapa do projeto.

📌 Principais Métricas

Faturamento Total: soma do valor total de todas as vendas.

Ticket Médio: média de faturamento por pedido.

Top 10 Produtos Mais Vendidos: produtos com maior volume de vendas.

Top 10 Países com Mais Vendas: países que concentram a maior parte das vendas.

Evolução das Vendas Mensais: comportamento das vendas ao longo do tempo.

Essas métricas ajudam a entender tanto o desempenho geral quanto padrões específicos do negócio.

📈 Insights Obtidos

Poucos produtos concentram uma grande parte do volume total de vendas.

Alguns países se destacam claramente como os principais mercados.

A evolução mensal das vendas permite identificar períodos de crescimento e possíveis quedas.

O ticket médio fornece uma boa visão sobre o valor médio gasto por pedido, ajudando na análise de comportamento do cliente.

Esses insights demonstram como os dados podem apoiar decisões estratégicas de negócio.

📊 Gráficos Gerados

Foram criados gráficos para facilitar a visualização e interpretação dos dados:

Gráfico de barras: Top 10 Produtos Mais Vendidos

Gráfico de pizza: Participação dos Top 10 Países nas Vendas

Gráfico de linha: Evolução das Vendas Mensais

Todos os gráficos foram gerados com Matplotlib, consolidando o aprendizado prático da biblioteca desde o zero.

(Os gráficos estão exportados em formato PNG e incluídos neste relatório.)

🚀 Próximos Passos

Como evolução natural do projeto, alguns próximos passos possíveis são:

Automatizar o pipeline ETL.

Fazer testes com Pytest

Melhoria na estrutura pra um codigo limpo

🎯 Conclusão

Este projeto permitiu aplicar conceitos essenciais de dados de forma prática, passando por todas as etapas de um pipeline real, desde a extração até a análise visual.

Além do aprendizado técnico, o projeto reforçou a importância de organização, clareza e responsabilidade única em cada módulo, aproximando a prática de cenários reais do mercado de dados.