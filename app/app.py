import streamlit as st
import pickle
import pandas as pd

# Carregar modelo
data = pickle.load(
    open("../model/prouni_model.pkl", "rb")
)

model = data["model"]
encoders = data["encoders"]
target_encoder = data["target_encoder"]

st.set_page_config(
    page_title="Predição de Bolsa PROUNI",
    page_icon="🎓"
)

st.title("🎓 Predição de Bolsa do PROUNI")

st.write(
    "Preencha os dados abaixo para prever o tipo de bolsa."
)

sexo = st.selectbox(
    "Sexo",
    ["F", "M"]
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
    ]
)

regiao = st.selectbox(
    "Região",
    [
        "Sul",
        "Sudeste",
        "Norte",
        "Nordeste",
        "Centro-Oeste"
    ]
)

uf = st.selectbox(
    "UF",
    [
        "PR","SP","RO","MG","SC","ES","PE","RS","RJ","BA",
        "PA","MA","MT","SE","DF","GO","CE","MS","AC","RR",
        "TO","AM","AL","PB","RN","PI","AP"
    ]
)

modalidade = st.selectbox(
    "Modalidade de Ensino",
    [
        "Presencial",
        "EAD"
    ]
)

turno = st.selectbox(
    "Turno do Curso",
    [
        "Noturno",
        "Matutino",
        "Vespertino",
        "Curso a distância",
        "Integral"
    ]
)

deficiente = st.selectbox(
    "Possui Deficiência Física?",
    [
        "N",
        "S"
    ]
)

if st.button("Prever Bolsa"):

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

        previsao = model.predict(entrada)

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