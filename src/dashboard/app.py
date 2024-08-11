import streamlit as st
import duckdb


# conectar com o banco de dados duckdb
conn = duckdb.connect('data/output.db')
df = conn.execute("SELECT * FROM mercadolivre_item_carros").fetch_df()
conn.close()

st.title('Pesquisa de Mercado - Carros de até 30K no Mercado Livre')

st.subheader('KPIs Principais do sistema')
col1, col2 = st.columns([4, 2])


# KPI 1: Número total de veiculos
total_itens = df.shape[0]
col1.metric(label="Número total de veiculos", value=total_itens)

# KPI 2: Média dos preços
average_price = df['money_amount'].str.replace('.','.').astype(float).mean()
col2.metric(label="Preço Médio (R$)", value=f"{average_price:.2f}K")

st.subheader("Localidade top 10 com mais vendas")
col1, col2 = st.columns([4, 2])
# Quais sao as cidades com mais anuncia de venda
top_10_location_sales = df['location'].value_counts().sort_values(ascending=False)
col1.bar_chart(top_10_location_sales)
col2.write(top_10_location_sales)