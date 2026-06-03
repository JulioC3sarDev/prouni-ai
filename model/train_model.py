import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv(
    "../dataset/Equipe-05_pda-prouni-2017.csv",
    sep=";"
)

features = [
    'SEXO_BENEFICIARIO_BOLSA',
    'RACA_BENEFICIARIO_BOLSA',
    'REGIAO_BENEFICIARIO_BOLSA',
    'SIGLA_UF_BENEFICIARIO_BOLSA',
    'MODALIDADE_ENSINO_BOLSA',
    'NOME_TURNO_CURSO_BOLSA',
    'BENEFICIARIO_DEFICIENTE_FISICO'
]

target = "TIPO_BOLSA"

encoders = {}

for col in features:
    le = LabelEncoder()

    df[col] = df[col].astype(str)

    df[col] = le.fit_transform(df[col])

    encoders[col] = le

target_encoder = LabelEncoder()

df[target] = target_encoder.fit_transform(
    df[target]
)

X = df[features]

y = df[target]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

pred = model.predict(X_test)

acc = accuracy_score(
    y_test,
    pred
)

print("Accuracy:", acc)

pickle.dump(
    {
        "model": model,
        "encoders": encoders,
        "target_encoder": target_encoder
    },
    open("prouni_model.pkl", "wb")
)

print("Modelo salvo!")