import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

st.set_page_config(page_title='Análise de Transporte e Logística: Visão Geral de Frete e Viagens',
                   page_icon=':bar_chart:',
                   layout='wide')

df = pd.read_csv('./data/dataset.csv', encoding='utf-8')
# st.dataframe(df)

# Sidebar
st.sidebar.header('Por favor, filtre por aqui:')

# Cidade de Origem
cidade_origem = st.sidebar.multiselect(
    'Seleccione a cidade de origem',
    options=df['Origem_Cidade'].unique(),
    default=df['Origem_Cidade'].unique()
)

# Transportadora
transportadora = st.sidebar.multiselect(
    'Seleccione a Transportadora',
    options=df['Transportadora'].unique(),
    default=df['Transportadora'].unique()
)

# Tipo de Transporte
transporte = st.sidebar.multiselect(
    'Seleccione o Tipo Transporte',
    options=df['Tipo_Transporte'].unique(),
    default=df['Tipo_Transporte'].unique()
)

df_selection = df.query(
    "Origem_Cidade == @cidade_origem & Transportadora == @transportadora & Tipo_Transporte == @transporte"
)

# Main Page
st.title(":bar_chart: Análise de Transporte e Logística")
st.subheader("Visão Geral de Frete e Viagens")
st.markdown("##")

# Top KPI's
valor_total_transporte = int(df_selection['Valor do Frete (MT)'].sum())
total_cubagem = df_selection['Cubagem'].sum()
total_peso_bruto = df_selection['Peso Bruto (kg)'].sum()

# Formatando os valores com separadores de milhares
valor_total_transporte_formatado = "{:,}".format(valor_total_transporte)
total_cubagem_formatado = "{:,.2f}".format(total_cubagem)
total_peso_bruto_formatado = "{:,.2f}".format(total_peso_bruto)

left_column, middle_column, right_column = st.columns(3)

with left_column:
    st.subheader('Custo - Transporte')
    st.subheader(f"{valor_total_transporte_formatado} MZN")
with middle_column:
    st.subheader('Cubagem')
    st.subheader(f"{total_cubagem_formatado} m³")
with right_column:
    st.subheader('Peso Bruto')
    st.subheader(f"{total_peso_bruto_formatado} kg")

st.markdown("---")

# Certificar que a coluna 'Data de Coleta' está no formato datetime
df_selection['Data de Coleta'] = pd.to_datetime(df_selection['Data de Coleta'])

# Configurar o índice como 'Data de Coleta'
df_selection.set_index('Data de Coleta', inplace=True)

# Análise de Tendências Temporais
df_monthly = df_selection.resample('M').sum().reset_index()

fig_tendencias_mensais = px.line(df_monthly,
                                 x='Data de Coleta',
                                 y=['Valor do Frete (MT)'],
                                 title='Tendências Mensais de Frete',
                                 labels={'Valor do Frete (MT)': 'Valor do Frete (MT)'})
st.plotly_chart(fig_tendencias_mensais)

st.markdown("---")

graphic1, graphic2 = st.columns(2)

# Gráfico de distribuição de status de transporte
color_map = {
    "Dentro do Prazo": "lightgreen",   # Verde claro
    "Atraso": "red"         # Vermelho
}
with graphic1:
    # Criando o gráfico de pizza
    fig_status = px.pie(df_selection, names="Status Transporte", title="Distribuição de Status de Transporte",
                        color="Status Transporte", color_discrete_map=color_map)
    # Exibindo o gráfico no Streamlit
    st.plotly_chart(fig_status)
with graphic2:
    df_atrasos = (df_selection.groupby("Transportadora", as_index=False)[
                  "Prazo Realizado"].count()).sort_values('Prazo Realizado', ascending=True)
    # Gráfico de atrasos por transportadora
    fig_atrasos = px.bar(
        df_atrasos,
        x="Transportadora",
        y="Prazo Realizado",
        title="Atrasos por Transportadora",
        color="Transportadora",  # Opcional: adicionar cores diferentes para cada transportadora
        labels={"Prazo Realizado": "Quantidade de Atrasos"}
    )
    # Exibindo o gráfico no Streamlit
    st.plotly_chart(fig_atrasos)

# Calcular o OTD
try:
    total_viagens = df_selection.shape[0]
    entregas_no_prazo = df_selection[df_selection['Status Transporte'] == 'Dentro do Prazo'].shape[0]
    if total_viagens == 0:
        otd = 0
    else:
        otd = (entregas_no_prazo / total_viagens) * 100  # Percentual de entregas no prazo

except ZeroDivisionError:
    otd = 0     # atribuir um valor padrao 

# Gráfico tipo manômetro
fig_manometro = go.Figure()
fig_manometro.add_trace(go.Indicator(
    mode="gauge+number",
    value=otd,
    title={'text': "On-Time Delivery (%)"},
    gauge={
        'axis': {'range': [0, 100]},
        'bar': {'color': "cyan"},
        'bgcolor': "lightgray",
        'steps': [
            {'range': [0, 50], 'color': "red"},
            {'range': [50, 75], 'color': "yellow"},
            {'range': [75, 100], 'color': "green"}
        ]
    }
))

fig_manometro.update_layout(
    margin={'l': 20, 'r': 20, 't': 50, 'b': 20},
    height=400,
)

# Streamlit App
st.subheader("Entregas feitas dentro do prazo em relação ao total de entregas")
st.markdown("### On-Time Delivery (OTD)")

# Exibir o gráfico tipo manômetro
st.plotly_chart(fig_manometro)

st.dataframe(df_selection)
