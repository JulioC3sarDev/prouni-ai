import streamlit as st
import pickle
import pandas as pd
import unicodedata

# ==================================
# CONFIGURAÇÃO DA PÁGINA
# ==================================

st.set_page_config(
    page_title="PROUNI AI",
    page_icon="🎓",
    layout="wide"
)

# ==================================
# ESTILOS CUSTOMIZADOS
# ==================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@300;400;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

html, body, [class*="css"] { font-family: 'Sora', sans-serif; }
.stApp { background: #0a0f1e; color: #e8eaf6; }
[data-testid="stToolbar"] { visibility: hidden; }

/* ---- HERO HEADER ---- */
.hero {
    background: linear-gradient(135deg, #0d1b4b 0%, #0a0f1e 60%);
    border: 1px solid rgba(99, 130, 255, 0.25);
    border-radius: 16px;
    padding: 40px 48px;
    margin-bottom: 28px;
    position: relative;
    overflow: hidden;
}
.hero::before {
    content: '';
    position: absolute;
    top: -60px; right: -60px;
    width: 240px; height: 240px;
    background: radial-gradient(circle, rgba(99,130,255,0.18) 0%, transparent 70%);
    pointer-events: none;
}
.hero-badge {
    display: inline-flex; align-items: center; gap: 6px;
    background: rgba(99,130,255,0.12);
    border: 1px solid rgba(99,130,255,0.3);
    border-radius: 20px; padding: 4px 14px;
    font-size: 12px; font-weight: 600; color: #8fa8ff;
    letter-spacing: 0.8px; text-transform: uppercase; margin-bottom: 16px;
}
.hero h1 { font-size: 2.2rem; font-weight: 700; color: #fff; margin: 0 0 10px 0; line-height: 1.2; }
.hero h1 span { background: linear-gradient(90deg, #6382ff, #a78bfa); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
.hero p { color: #8892b8; font-size: 0.95rem; line-height: 1.7; max-width: 600px; margin: 0; }
.hero-model-tag {
    display: inline-flex; align-items: center; gap: 6px; margin-top: 18px;
    background: rgba(16,185,129,0.1); border: 1px solid rgba(16,185,129,0.25);
    border-radius: 8px; padding: 5px 12px;
    font-family: 'JetBrains Mono', monospace; font-size: 11.5px; color: #34d399;
}

/* ---- SECTION LABEL ---- */
.section-label {
    font-size: 11px; font-weight: 600; letter-spacing: 1.5px;
    text-transform: uppercase; color: #5a6aaa; margin-bottom: 18px; margin-top: 8px;
    display: flex; align-items: center; gap: 8px;
}
.section-label::after { content: ''; flex: 1; height: 1px; background: rgba(99,130,255,0.15); }

/* ---- INPUTS ---- */
div[data-testid="stSelectbox"] > label,
div[data-testid="stTextInput"] > label {
    font-size: 12.5px !important; font-weight: 600 !important;
    color: #8892b8 !important; letter-spacing: 0.4px; text-transform: uppercase;
}
div[data-baseweb="select"] > div {
    background: #111827 !important;
    border: 1px solid rgba(99,130,255,0.2) !important;
    border-radius: 10px !important; color: #e8eaf6 !important;
    transition: border-color 0.2s ease;
}
div[data-baseweb="select"] > div:hover { border-color: rgba(99,130,255,0.5) !important; }
div[data-baseweb="select"] > div:focus-within {
    border-color: #6382ff !important;
    box-shadow: 0 0 0 3px rgba(99,130,255,0.1) !important;
}
div[data-baseweb="popover"] {
    background: #111827 !important;
    border: 1px solid rgba(99,130,255,0.2) !important;
    border-radius: 10px !important;
}
li[data-testid="stSelectboxOption"] { color: #c9d1f5 !important; }
li[data-testid="stSelectboxOption"]:hover { background: rgba(99,130,255,0.12) !important; }

div[data-testid="stTextInput"] > div > input {
    background: #111827 !important;
    border: 1px solid rgba(99,130,255,0.2) !important;
    border-radius: 10px !important; color: #e8eaf6 !important;
    font-family: 'Sora', sans-serif !important;
    padding: 10px 14px !important;
}
div[data-testid="stTextInput"] > div > input:focus {
    border-color: #6382ff !important;
    box-shadow: 0 0 0 3px rgba(99,130,255,0.1) !important;
}

/* ---- BOTÃO ---- */
div[data-testid="stButton"] > button {
    width: 100%;
    background: linear-gradient(135deg, #4a6cf7, #6c47ff) !important;
    color: white !important; border: none !important;
    border-radius: 12px !important; padding: 14px 28px !important;
    font-family: 'Sora', sans-serif !important; font-size: 15px !important;
    font-weight: 600 !important; cursor: pointer;
    transition: all 0.25s ease !important;
    box-shadow: 0 4px 20px rgba(74,108,247,0.35) !important;
}
div[data-testid="stButton"] > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 28px rgba(74,108,247,0.5) !important;
}

/* ---- RESULTADO ---- */
.result-card {
    background: linear-gradient(135deg, rgba(16,185,129,0.08), rgba(16,185,129,0.03));
    border: 1px solid rgba(16,185,129,0.3);
    border-radius: 14px; padding: 24px 28px; margin-top: 24px;
    display: flex; align-items: center; gap: 18px;
}
.result-icon { font-size: 2.4rem; flex-shrink: 0; }
.result-label { font-size: 11px; font-weight: 600; letter-spacing: 1.2px; text-transform: uppercase; color: #34d399; margin-bottom: 4px; }
.result-value { font-size: 1.4rem; font-weight: 700; color: #ffffff; }

/* ---- STATS ---- */
.stats-row { display: flex; gap: 16px; margin-bottom: 24px; flex-wrap: wrap; }
.stat-card {
    flex: 1; min-width: 140px;
    background: #111827;
    border: 1px solid rgba(99,130,255,0.15);
    border-radius: 12px; padding: 16px 20px;
}
.stat-value { font-size: 1.6rem; font-weight: 700; color: #fff; }
.stat-value span { background: linear-gradient(90deg, #6382ff, #a78bfa); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
.stat-label { font-size: 11px; color: #5a6aaa; font-weight: 600; letter-spacing: 0.8px; text-transform: uppercase; margin-top: 4px; }

/* ---- COURSE CARDS ---- */
.course-grid { display: flex; flex-direction: column; gap: 8px; margin-top: 8px; }
.course-card {
    background: #111827;
    border: 1px solid rgba(99,130,255,0.12);
    border-radius: 10px;
    padding: 12px 18px;
    display: flex; align-items: center; justify-content: space-between;
    transition: border-color 0.2s;
}
.course-card:hover { border-color: rgba(99,130,255,0.35); }
.course-name { color: #c9d1f5; font-size: 14px; font-weight: 500; }
.course-count {
    background: rgba(99,130,255,0.1);
    border: 1px solid rgba(99,130,255,0.2);
    border-radius: 20px; padding: 2px 10px;
    font-size: 11px; font-weight: 600; color: #6382ff;
    font-family: 'JetBrains Mono', monospace;
}

hr { border-color: rgba(99,130,255,0.12) !important; }
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: #0a0f1e; }
::-webkit-scrollbar-thumb { background: #2a3470; border-radius: 3px; }
</style>
""", unsafe_allow_html=True)

# ==================================
# HELPERS
# ==================================

def remover_acentos(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    ).lower()

def renderizar_cursos(cursos_df, key_suffix):
    total = len(cursos_df)
    col_busca, col_ord = st.columns([3, 1])
    with col_busca:
        busca = st.text_input(
            "Filtrar cursos",
            placeholder="Ex: Medicina, Direito, Engenharia...",
            label_visibility="collapsed",
            key=f"busca_{key_suffix}"
        )
    with col_ord:
        ordenar = st.selectbox(
            "Ordem",
            ["Mais bolsas", "A → Z"],
            label_visibility="collapsed",
            key=f"ordem_{key_suffix}"
        )

    exibir = cursos_df
    if busca.strip():
        termo = remover_acentos(busca.strip())
        exibir = cursos_df[cursos_df["curso"].apply(lambda x: termo in remover_acentos(str(x)))]

    exibir = exibir.sort_values(
        "curso" if ordenar == "A → Z" else "bolsas",
        ascending=(ordenar == "A → Z")
    )

    st.markdown(
        f"<p style='color:#5a6aaa; font-size:12px; margin:4px 0 12px;'>{len(exibir)} de {total} cursos</p>",
        unsafe_allow_html=True
    )

    if exibir.empty:
        st.markdown("<p style='color:#5a6aaa; text-align:center; padding:20px;'>Nenhum curso encontrado.</p>", unsafe_allow_html=True)
    else:
        cards_html = '<div class="course-grid">'
        for _, row in exibir.head(200).iterrows():
            cards_html += f"""
            <div class="course-card">
                <span class="course-name">{row['curso']}</span>
                <span class="course-count">{int(row['bolsas']):,} bolsas</span>
            </div>"""
        cards_html += '</div>'
        if len(exibir) > 200:
            cards_html += f"<p style='color:#5a6aaa; font-size:12px; text-align:center; margin-top:12px;'>Exibindo 200 de {len(exibir)}. Refine a busca.</p>"
        st.markdown(cards_html, unsafe_allow_html=True)

# ==================================
# CARREGAR DADOS E MODELO
# ==================================

@st.cache_data
def carregar_cursos():
    df = pd.read_csv(
        "../dataset/Equipe-05_pda-prouni-2017.csv",
        sep=";",
        usecols=["NOME_CURSO_BOLSA", "TIPO_BOLSA"]
    )
    df["NOME_CURSO_BOLSA"] = df["NOME_CURSO_BOLSA"].str.strip().str.title()
    df["TIPO_BOLSA"] = df["TIPO_BOLSA"].str.strip()
    return df

def cursos_por_tipo(df, tipo_bolsa):
    filtrado = df[df["TIPO_BOLSA"] == tipo_bolsa]
    contagem = filtrado["NOME_CURSO_BOLSA"].value_counts().reset_index()
    contagem.columns = ["curso", "bolsas"]
    return contagem

@st.cache_resource
def carregar_modelo():
    data = pickle.load(open("../model/prouni_model.pkl", "rb"))
    return data["model"], data["encoders"], data["target_encoder"]

df_bolsas = carregar_cursos()
model, encoders, target_encoder = carregar_modelo()

# ==================================
# SESSION STATE
# ==================================

if "resultado" not in st.session_state:
    st.session_state.resultado = None

# ==================================
# HERO HEADER
# ==================================

st.markdown("""
<div class="hero">
    <div class="hero-badge">✦ Inteligência Artificial Educacional</div>
    <h1>Predição de Bolsas <span>PROUNI 2017</span></h1>
    <p>
        Informe o perfil do estudante e nosso modelo de Machine Learning prevê
        o tipo de bolsa mais provável com base em dados históricos do programa.
    </p>
    <div class="hero-model-tag">⬡ &nbsp;Random Forest Classifier &nbsp;&nbsp;</div>
</div>
""", unsafe_allow_html=True)

# ==================================
# FORMULÁRIO
# ==================================

st.markdown('<div class="section-label">Perfil do Candidato</div>', unsafe_allow_html=True)

col_esq, _, col_dir = st.columns([1, 0.06, 1])

with col_esq:
    sexo = st.selectbox("Sexo", ["F", "M"], index=None, placeholder="Selecione...")
    raca = st.selectbox(
        "Raça / Cor",
        ["Branca", "Parda", "Preta", "Amarela", "Indígena", "Não Informada"],
        index=None, placeholder="Selecione..."
    )
    regiao = st.selectbox(
        "Região",
        ["Sul", "Sudeste", "Norte", "Nordeste", "Centro-Oeste"],
        index=None, placeholder="Selecione..."
    )
    uf = st.selectbox(
        "UF",
        sorted(["AC","AL","AM","AP","BA","CE","DF","ES","GO","MA",
                "MG","MS","MT","PA","PB","PE","PI","PR","RJ","RN",
                "RO","RR","RS","SC","SE","SP","TO"]),
        index=None, placeholder="Selecione..."
    )

with col_dir:
    modalidade = st.selectbox(
        "Modalidade de Ensino", ["Presencial", "EAD"],
        index=None, placeholder="Selecione..."
    )
    turno = st.selectbox(
        "Turno do Curso",
        ["Noturno", "Matutino", "Vespertino", "Curso a distância", "Integral"],
        index=None, placeholder="Selecione..."
    )
    deficiente = st.selectbox(
        "Possui Deficiência Física?", ["N", "S"],
        index=None, placeholder="Selecione..."
    )

st.markdown("<br>", unsafe_allow_html=True)

if st.button("  Prever Tipo de Bolsa", use_container_width=True):
    if None in [sexo, raca, regiao, uf, modalidade, turno, deficiente]:
        st.warning("  Preencha todos os campos antes de realizar a previsão.")
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
            entrada[col] = encoders[col].transform(entrada[col])
        previsao = model.predict(entrada)
        st.session_state.resultado = target_encoder.inverse_transform(previsao)[0]
    except Exception as e:
        st.error(f"  Erro ao realizar previsão: {e}")

# ==================================
# RESULTADO + CURSOS
# ==================================

if st.session_state.resultado:
    resultado = st.session_state.resultado

    st.markdown(f"""
    <div class="result-card">
        <div class="result-icon">🎓</div>
        <div>
            <div class="result-label">Tipo de bolsa previsto</div>
            <div class="result-value">{resultado}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    cursos_tipo = cursos_por_tipo(df_bolsas, resultado)

    st.markdown(f"""
    <div class="stats-row">
        <div class="stat-card">
            <div class="stat-value"><span>{len(cursos_tipo):,}</span></div>
            <div class="stat-label">Cursos disponíveis</div>
        </div>
        <div class="stat-card">
            <div class="stat-value"><span>{int(cursos_tipo['bolsas'].sum()):,}</span></div>
            <div class="stat-label">Bolsas concedidas</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-label">Cursos Ofertados para Esta Bolsa</div>', unsafe_allow_html=True)
    renderizar_cursos(cursos_tipo, key_suffix="resultado")