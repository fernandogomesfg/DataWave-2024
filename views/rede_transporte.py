import streamlit as st

st.title("Rede de Transporte")

col1, col2 = st.columns(2)

with col1:
    # Infraestrutura Física
    st.header("Infraestrutura")
    st.write("""
        - Rodovias
        - Ferrovias
        - Portos
        - Aeroportos
        - Ciclovias
        - Vias pedonais.""")
with col2:
    # Meios de Transporte
    st.header("Meios de Transporte")
    st.write("""
            - Terrestre 
            - Ferroviário
            - Aéreo
            - Marítimo.
             """)

# Operadores e Provedores de Serviços
st.header("Operadores e Provedores de Serviços")
st.write("""
        - Empresas de transporte público
        - Companhias aéreas
        - Logística
        - Táxis""")

# Agências Reguladoras e Governamentais
st.header("Agências Reguladoras e Governamentais")
st.write("Governos e agências reguladoras.")

# Usuários
st.header("Usuários")
st.write("Passageiros, motoristas e empresas.")
