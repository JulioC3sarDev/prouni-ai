import streamlit as st
import pickle
import pandas as pd

# ==================================
# CONFIGURAÇÃO DA PÁGINA
# ==================================

st.set_page_config(
    page_title="PROUNI AI",
    layout="wide"
)

# ==================================
# CARREGAR MODELO
# ==================================

data = pickle.load(
    open("../model/prouni_model.pkl", "rb")
)

model = data["model"]
encoders = data["encoders"]
target_encoder = data["target_encoder"]

# ==================================
# CABEÇALHO
# ==================================

st.title("Sistema de Predição de Bolsas PROUNI")

st.markdown("""
Esta aplicação utiliza técnicas de Machine Learning para prever o tipo de bolsa
concedida pelo PROUNI com base nas características do estudante.

**Modelo utilizado:** Random Forest Classifier
""")

# ==================================
# FORMULÁRIO
# ==================================

col_esq, col_dir = st.columns(2)

with col_esq:

    sexo = st.selectbox(
        "Sexo",
        ["F", "M"],
        index=None,
        placeholder="Selecione o sexo"
    )

    raca = st.selectbox(
        "Raça",
        [
            "Branca",
            "Parda",
            "Preta",
            "Amarela",
            "Indígena",
            "Não Informada"
        ],
        index=None,
        placeholder="Selecione a raça"
    )

    regiao = st.selectbox(
        "Região",
        [
            "Sul",
            "Sudeste",
            "Norte",
            "Nordeste",
            "Centro-Oeste"
        ],
        index=None,
        placeholder="Selecione a região"
    )

    uf = st.selectbox(
        "UF",
        [
            "PR", "SP", "RO", "MG", "SC", "ES", "PE",
            "RS", "RJ", "BA", "PA", "MA", "MT", "SE",
            "DF", "GO", "CE", "MS", "AC", "RR", "TO",
            "AM", "AL", "PB", "RN", "PI", "AP"
        ],
        index=None,
        placeholder="Selecione a UF"
    )

with col_dir:

    modalidade = st.selectbox(
        "Modalidade de Ensino",
        [
            "Presencial",
            "EAD"
        ],
        index=None,
        placeholder="Selecione a modalidade"
    )

    turno = st.selectbox(
        "Turno do Curso",
        [
            "Noturno",
            "Matutino",
            "Vespertino",
            "Curso a distância",
            "Integral"
        ],
        index=None,
        placeholder="Selecione o turno"
    )

    deficiente = st.selectbox(
        "Possui Deficiência Física?",
        [
            "N",
            "S"
        ],
        index=None,
        placeholder="Selecione uma opção"
    )

st.markdown("")

# ==================================
# PREVISÃO
# ==================================

if st.button("Prever Bolsa"):

    if None in [
        sexo,
        raca,
        regiao,
        uf,
        modalidade,
        turno,
        deficiente
    ]:

        st.warning(
            "Preencha todos os campos antes de realizar a previsão."
        )

        st.stop()

    entrada = pd.DataFrame([{
        "SEXO_BENEFICIARIO_BOLSA": sexo,
        "RACA_BENEFICIARIO_BOLSA": raca,
        "REGIAO_BENEFICIARIO_BOLSA": regiao,
        "SIGLA_UF_BENEFICIARIO_BOLSA": uf,
        "MODALIDADE_ENSINO_BOLSA": modalidade,
        "NOME_TURNO_CURSO_BOLSA": turno,
        "BENEFICIARIO_DEFICIENTE_FISICO": deficiente
    }])

    try:

        for col in entrada.columns:
            entrada[col] = encoders[col].transform(
                entrada[col]
            )

        previsao = model.predict(
            entrada
        )

        resultado = target_encoder.inverse_transform(
            previsao
        )[0]

        st.success(
            f"Tipo de bolsa previsto: {resultado}"
        )

    except Exception as e:

        st.error(
            f"Erro ao realizar previsão: {e}"
        )
