import streamlit as st
import pandas as pd
import plotly.express as px
import folium
from streamlit_folium import st_folium
from folium.plugins import HeatMap


st.title('🚧 Análise de Acidentes na Cidade de Maputo')

df = pd.read_csv('./data/dataset_acidentes.csv', sep=',', encoding='latin1')

# Quantificação do Total de Eventos
st.subheader('Quanto acidentes foram registrados?')
total_eventos = df.shape[0]
st.write(f"O total de eventos registrados é: {total_eventos}")


top_causas = df['causa_acidente'].value_counts().head(5).reset_index()
top_causas.columns = ['Causa do Acidente', 'Número de Ocorrências']

# Criação do gráfico
fig = px.bar(
    top_causas,
    x='Causa do Acidente',
    y='Número de Ocorrências',
    labels={'Causa do Acidente': 'Causa do Acidente', 'Número de Ocorrências': 'Número de Ocorrências'},
    title='Maiores Causas de Acidentes',
    color='Número de Ocorrências',  # Adiciona cor baseada nos valores
    color_continuous_scale=px.colors.sequential.Plasma  # Escolha uma paleta de cores
)

#   layout
fig.update_xaxes(
    tickangle=45,
    title_font_size=14
)
fig.update_yaxes(
    title_font_size=14,
    tickfont_size=12
)
fig.update_layout(
    title_font_size=16,
    title_x=0.5,  # Centraliza o título
    xaxis_title='Causa do Acidente',
    yaxis_title='Número de Ocorrências',
    xaxis=dict(tickmode='array', tickvals=top_causas['Causa do Acidente']),
    margin=dict(l=50, r=50, t=50, b=50),  # Ajusta as margens
    bargap=0.2  # Ajusta o espaço entre as barras (0.2 = 20% de espaço)
)

# Adicionar rótulos de valor nas barras
fig.update_traces(
    texttemplate='%{y}',
    textposition='auto',
    marker=dict(line=dict(color='black', width=1))  # Adiciona borda preta às barras
)

# Mostrar o gráfico
st.plotly_chart(fig)


# Gerar o mapa base
st.subheader('Geolocalização dos Eventos')
map_center = [df['latitude'].mean(), df['longitude'].mean()]
m = folium.Map(location=map_center, zoom_start=10)

# Adicionar o mapa de calor
heat_data = [[row['latitude'], row['longitude']] for i, row in df.iterrows()]
HeatMap(heat_data, radius=8).add_to(m)

# Exibir o mapa no Streamlit
st_folium(m, width=700, height=500)


# Ocorrências com Mais de 3 Óbitos
st.subheader('Ocorrências com Mais de 3 Óbitos')
ocorrencias_3_obitos = df[df['mortos'] > 5]
st.write(f"Total de ocorrências com mais de 3 óbitos: {ocorrencias_3_obitos.shape[0]}")
st.dataframe(ocorrencias_3_obitos[['data', 'hora', 'causa_acidente', 'mortos', 'latitude', 'longitude']])
