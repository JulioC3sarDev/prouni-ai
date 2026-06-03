# Predição de Bolsa do PROUNI

## Visão Geral

Este projeto foi desenvolvido como parte da disciplina de Ciência de Dados e Inteligência Artificial.

O objetivo é prever o tipo de bolsa concedida pelo Programa Universidade para Todos (PROUNI) utilizando técnicas de Machine Learning e dados históricos do PROUNI 2017.

A aplicação permite que o usuário informe características de um estudante e receba uma previsão do tipo de bolsa por meio de uma interface web desenvolvida com Streamlit.

---

## Integrantes da Equipe

- Ariel Barbosa
- Cézar Bezerra
- Júlio César Ferreira
- Maria Eduarda
- Lucas Nascimento

---

## Problema Proposto

O PROUNI oferece bolsas de estudo para estudantes em instituições de ensino superior no Brasil.

Este projeto tem como objetivo prever o tipo de bolsa concedida com base em características do estudante, tais como:

- Sexo
- Raça
- Região
- Unidade Federativa (UF)
- Modalidade de Ensino
- Turno do Curso
- Deficiência Física

A variável alvo utilizada foi:

- Tipo de Bolsa (TIPO_BOLSA)

---

## Base de Dados

Base utilizada:

**PROUNI 2017**

A base contém informações sobre beneficiários do PROUNI, incluindo características demográficas, geográficas e educacionais.

---

## Variáveis Utilizadas

O modelo foi treinado utilizando as seguintes variáveis:

| Variável |
|-----------|
| SEXO_BENEFICIARIO_BOLSA |
| RACA_BENEFICIARIO_BOLSA |
| REGIAO_BENEFICIARIO_BOLSA |
| SIGLA_UF_BENEFICIARIO_BOLSA |
| MODALIDADE_ENSINO_BOLSA |
| NOME_TURNO_CURSO_BOLSA |
| BENEFICIARIO_DEFICIENTE_FISICO |

### Variável Alvo

| Variável |
|-----------|
| TIPO_BOLSA |

---

## Tecnologias Utilizadas

- Python
- Pandas
- NumPy
- Scikit-Learn
- Streamlit
- Matplotlib
- Seaborn
- Pickle

---

## Modelo de Machine Learning

O algoritmo escolhido foi:

### Random Forest Classifier

Motivos da escolha:

- Bom desempenho em problemas de classificação.
- Facilidade de implementação.
- Menor tendência ao overfitting.
- Boa capacidade de generalização.

---

## Preparação dos Dados

As seguintes etapas foram realizadas:

1. Carregamento da base de dados.
2. Seleção das variáveis relevantes.
3. Conversão de variáveis categóricas utilizando LabelEncoder.
4. Divisão dos dados em treino e teste.
5. Treinamento do modelo.
6. Avaliação da acurácia.
7. Serialização do modelo utilizando Pickle.

---

## Estrutura do Projeto

```text
Projeto Data Science/
│
├── app/
│   └── app.py
│
├── dataset/
│   └── Equipe-05_pda-prouni-2017.csv
│
├── model/
│   ├── train_model.py
│   └── prouni_model.pkl
│
├── requirements.txt
│
└── README.md
```

---

## Instalação

### Clonar o Repositório

```bash
git clone https://github.com/JulioC3sarDev/prouni-ai.git
```

### Acessar a Pasta do Projeto

```bash
cd prouni-ai
```

### Criar Ambiente Virtual

```bash
python -m venv venv
```

### Ativar Ambiente Virtual

Windows:

```bash
venv\Scripts\activate
```

### Instalar Dependências

```bash
pip install -r requirements.txt
```

---

## Treinamento do Modelo

Para treinar o modelo:

```bash
cd model

python train_model.py
```

Ao final da execução será criado o arquivo:

```text
prouni_model.pkl
```

---

## Execução da Aplicação

Acesse a pasta da aplicação:

```bash
cd app
```

Execute o Streamlit:

```bash
streamlit run app.py
```

A aplicação ficará disponível em:

```text
http://localhost:8501
```

---

## Fluxo da Solução

```text
Base PROUNI 2017
        ↓
Tratamento dos Dados
        ↓
Treinamento do Modelo
        ↓
Random Forest
        ↓
Arquivo .pkl
        ↓
Interface Streamlit
        ↓
Predição do Tipo de Bolsa
```

---

## Exemplo de Utilização

Entrada:

- Sexo: F
- Raça: Parda
- Região: Nordeste
- UF: PE
- Modalidade: Presencial
- Turno: Noturno
- Deficiência Física: N

Saída:

```text
Tipo de Bolsa Previsto:
Bolsa Integral
```

---

## Resultados

O desempenho do modelo foi avaliado utilizando:

- Accuracy Score (Acurácia)

Exemplo:

```text
Accuracy: 0.84
```

(O valor pode variar dependendo do treinamento realizado.)

---

## Possíveis Melhorias Futuras

- Ajuste de hiperparâmetros.
- Inclusão de novas variáveis.
- Matriz de confusão.
- Gráficos de importância das variáveis.
- Publicação em nuvem.
- Integração com APIs.

---

## Conclusão

Este projeto demonstra a aplicação prática de técnicas de Machine Learning para prever o tipo de bolsa concedida pelo PROUNI.

A solução integra:

- Análise de Dados
- Machine Learning
- Serialização de Modelos
- Desenvolvimento Web

resultando em uma aplicação completa de Inteligência Artificial.

---

## Licença

Projeto desenvolvido exclusivamente para fins acadêmicos.