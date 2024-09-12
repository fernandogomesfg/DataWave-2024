import streamlit as st

st.sidebar.markdown("Made with ❤️ by [Fernando Gomes](https://www.linkedin.com/in/fernandogomesfg/)")

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/gomes.png")

with col2:
    st.title("Fernando Gomes", anchor=False)
    st.write(
        "Analista de Dados, orientando empresas na optimização de estratégias com soluções analíticas e visualizações de dados precisas."
    )


# --- EXPERIENCE & QUALIFICATIONS ---
st.write("\n")
st.subheader("Experiência e Qualificações", anchor=False)
st.write(
    """
    - Experiência na extração de insights a partir de dados 
    - Conhecimento em Python e ferramentas GIS como QGIS e ArcGIS
    - Bom entendimento dos princípios estatísticos e suas aplicações em análise de dados espaciais
    """
)

# --- SKILLS ---
st.write("\n")
st.subheader("Hard Skills", anchor=False)
st.write(
    """
    - Programação: Python, JavaScript (LeafletJS), R, SQL, MATLAB
    - Visualização de Dados: Power BI, Microsoft Office Excel, Plotly, Matplotlib
    - Base de Dados: PostgreSQL, MongoDB, MySQL, SQLite
    - Ferramentas GIS: QGIS, ArcGIS, Google Earth Engine, ERDAS Imagine, GRASS GIS, GeoServer
    """
)