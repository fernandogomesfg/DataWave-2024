import streamlit as st

about_page = st.Page(
    page="views/about_me.py",
    title="About Me",
    icon="",
    default=True
)

transport_dash = st.Page(
    page="views/transport_dash.py",
    title="Frete e Logística",
    icon="",
)

acidentes_dash = st.Page(
    page="views/acidentes_dash.py",
    title="Acidentes ",
    icon="",
)

rede_transporte = st.Page(
    page="views/rede_transporte.py",
    title="Rede de Transporte ",
    icon="",
)

acessibilidade = st.Page(
    page="views/acessibilidade.py",
    title="Acessibilidade",
    icon="",
)

obrigado = st.Page(
    page="views/obrigado.py",
    title="Fim",
    icon="",
)

# Navigation Section
pg = st.navigation(pages=[about_page, transport_dash, acidentes_dash, rede_transporte, acessibilidade, obrigado])

pg = st.navigation(
    {
        "Info": [about_page, rede_transporte],
        "Projects": [transport_dash, acidentes_dash, acessibilidade],
        "Obrigado": [obrigado]
    }
)

pg.run()