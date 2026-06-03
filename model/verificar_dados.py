import pandas as pd

df = pd.read_csv(
    "../dataset/Equipe-05_pda-prouni-2017.csv",
    sep=";"
)

colunas = [
    'SEXO_BENEFICIARIO_BOLSA',
    'RACA_BENEFICIARIO_BOLSA',
    'REGIAO_BENEFICIARIO_BOLSA',
    'SIGLA_UF_BENEFICIARIO_BOLSA',
    'MODALIDADE_ENSINO_BOLSA',
    'NOME_TURNO_CURSO_BOLSA',
    'BENEFICIARIO_DEFICIENTE_FISICO'
]

for coluna in colunas:
    print("\n")
    print(coluna)
    print(df[coluna].dropna().unique())