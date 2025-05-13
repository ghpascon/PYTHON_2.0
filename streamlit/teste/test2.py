import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import time

st.set_page_config(
    page_title="Exemplo de Streamlit",
    layout="wide",
    page_icon="teste/smartx_branco_250px.png",
    initial_sidebar_state="expanded"
)

# Cabeçalho
st.title("Exemplo de funcionalidades do Streamlit")
st.write("Explore diferentes funcionalidades interativas do Streamlit.")

# Barra lateral
st.sidebar.title("Menu")
opcao = st.sidebar.selectbox(
    "Selecione uma funcionalidade",
    ["Introdução", "Exibir Texto", "Gráficos", "Interatividade", "Upload de Arquivos", "Progresso", "Formulários"]
)

# Introdução
if opcao == "Introdução":
    st.header("Bem-vindo ao Streamlit!")
    st.write("""
        Este aplicativo demonstra várias funcionalidades do Streamlit.
        Use a barra lateral para navegar pelas seções.
    """)
    st.image("https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png", width=300)

# Exibir Texto
elif opcao == "Exibir Texto":
    st.header("Exibição de Texto")
    st.write("Você pode usar diferentes métodos para exibir texto:")
    st.text("Este é um texto básico.")
    st.markdown("**Markdown**: Texto em **negrito**, *itálico* e links como [Streamlit](https://streamlit.io).")
    st.code("print('Este é um código!')", language="python")

# Gráficos
elif opcao == "Gráficos":
    st.header("Gráficos")
    st.write("Exemplos de gráficos gerados com Streamlit e bibliotecas externas:")

    # Gráfico de linha com Streamlit
    st.subheader("Gráfico de linha")
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["A", "B", "C"])
    st.line_chart(chart_data)

    # Gráfico com Matplotlib
    st.subheader("Gráfico com Matplotlib")
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    fig, ax = plt.subplots()
    ax.plot(x, y, label="Seno")
    ax.set_title("Função Seno")
    ax.legend()
    st.pyplot(fig)

# Interatividade
elif opcao == "Interatividade":
    st.header("Interatividade")
    
    # Botões
    if st.button("Clique aqui"):
        st.write("Você clicou no botão!")
    
    # Caixa de texto
    texto = st.text_input("Digite algo:")
    if texto:
        st.write(f"Você digitou: {texto}")
    
    # Slider
    valor = st.slider("Escolha um valor", 0, 100, 50)
    st.write(f"Valor selecionado: {valor}")
    
    # Seleção de múltiplas opções
    opcoes = st.multiselect("Escolha suas frutas favoritas", ["Maçã", "Banana", "Laranja", "Uva"])
    st.write(f"Frutas selecionadas: {opcoes}")

# Upload de Arquivos
elif opcao == "Upload de Arquivos":
    st.header("Upload de Arquivos")
    st.write("Envie um arquivo para exibição.")
    arquivo = st.file_uploader("Envie seu arquivo aqui", type=["csv", "txt", "jpg", "png"])
    
    if arquivo is not None:
        if arquivo.type in ["image/jpeg", "image/png"]:
            imagem = Image.open(arquivo)
            st.image(imagem, caption="Imagem enviada", use_container_width=True)
        elif arquivo.type in ["text/csv", "text/plain"]:
            df = pd.read_csv(arquivo) if ".csv" in arquivo.name else pd.read_table(arquivo)
            st.write("Dados do arquivo:")
            st.dataframe(df)

# Progresso
elif opcao == "Progresso":
    st.header("Barra de Progresso")
    progresso = st.empty()
    barra = st.progress(0)

    for i in range(101):
        progresso.text(f"Progresso: {i}%")
        barra.progress(i)
        time.sleep(0.05)

# Formulários
elif opcao == "Formulários":
    st.header("Formulários")
    with st.form("formulario"):
        nome = st.text_input("Digite seu nome:")
        idade = st.number_input("Digite sua idade:", min_value=0, max_value=120, step=1)
        enviado = st.form_submit_button("Enviar")
        
        if enviado:
            st.write(f"Nome: {nome}")
            st.write(f"Idade: {idade}")

# Rodapé
st.sidebar.write("---")
st.sidebar.write("**Desenvolvido com ❤️ por Streamlit**")

#streamlit run teste/test2.py

