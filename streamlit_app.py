import streamlit as st

about_page = st.Page(
    page="views/about_me.py",
    title="About Me",
    icon="",
    default=True
)

transport_dash = st.Page(
    page="views/transport_dash.py",
    title="Dashboard ",
    icon="",
)

acidentes_dash = st.Page(
    page="views/acidentes_dash.py",
    title="Acidentes ",
    icon="",
)

# Navigation Section
pg = st.navigation(pages=[about_page, transport_dash, acidentes_dash])

pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [transport_dash, acidentes_dash]
    }
)

pg.run()