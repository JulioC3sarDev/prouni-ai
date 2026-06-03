# 🎓 PROUNI Scholarship Prediction

## Overview

This project was developed as part of the Artificial Intelligence and Data Science course.

The objective is to predict the type of scholarship granted by the Brazilian University for All Program (PROUNI) using Machine Learning techniques and historical data from the PROUNI 2017 dataset.

The application allows users to enter student information through a web interface and receive a prediction of the scholarship type.

---

## Team Members

- Ariel Barbosa
- Cézar Bezerra
- Júlio César Ferreira
- Maria Eduarda
- Lucas Nascimento

---

## Problem Statement

The PROUNI program offers scholarships to students enrolled in higher education institutions in Brazil.

This project aims to predict the scholarship type based on student characteristics such as:

- Gender
- Race
- Region
- State (UF)
- Teaching Modality
- Course Shift
- Physical Disability Status

The target variable is:

- Scholarship Type (TIPO_BOLSA)

---

## Dataset

Dataset used:

**PROUNI 2017 Dataset**

The dataset contains information about scholarship beneficiaries, including demographic, geographic, and educational characteristics.

---

## Features Used

The model was trained using the following features:

| Feature |
|----------|
| SEXO_BENEFICIARIO_BOLSA |
| RACA_BENEFICIARIO_BOLSA |
| REGIAO_BENEFICIARIO_BOLSA |
| SIGLA_UF_BENEFICIARIO_BOLSA |
| MODALIDADE_ENSINO_BOLSA |
| NOME_TURNO_CURSO_BOLSA |
| BENEFICIARIO_DEFICIENTE_FISICO |

### Target Variable

| Variable |
|-----------|
| TIPO_BOLSA |

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- Streamlit
- Matplotlib
- Seaborn
- Pickle

---

## Machine Learning Model

The chosen algorithm was:

### Random Forest Classifier

Reasons for choosing Random Forest:

- Good performance on classification problems
- Handles categorical data effectively after encoding
- Robust against overfitting
- Easy to implement and interpret

---

## Data Preparation

The following preprocessing steps were applied:

1. Data loading using Pandas
2. Selection of relevant features
3. Encoding categorical variables using LabelEncoder
4. Splitting data into training and testing sets
5. Model training
6. Model evaluation
7. Model serialization using Pickle

---

## Project Structure

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

## Installation

### Clone Repository

```bash
git clone https://github.com/JulioC3sarDev/prouni-ai.git
```

### Access Project Folder

```bash
cd prouni-ai
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Training the Model

To train the model:

```bash
cd model

python train_model.py
```

After execution, the following file will be generated:

```text
prouni_model.pkl
```

---

## Running the Application

Navigate to the application folder:

```bash
cd app
```

Run Streamlit:

```bash
streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

---

## Application Workflow

```text
PROUNI Dataset
        ↓
Data Preparation
        ↓
Random Forest Training
        ↓
Model Serialization (.pkl)
        ↓
Streamlit Interface
        ↓
Scholarship Prediction
```

---

## Example Prediction

Input:

- Gender: F
- Race: Parda
- Region: Nordeste
- UF: PE
- Teaching Modality: Presencial
- Course Shift: Noturno
- Physical Disability: N

Output:

```text
Predicted Scholarship Type:
Bolsa Integral
```

---

## Results

The model performance is evaluated using:

- Accuracy Score

Example:

```text
Accuracy: 0.84
```

(The actual value may vary depending on training execution.)

---

## Future Improvements

Possible future enhancements include:

- Hyperparameter tuning
- Additional feature engineering
- Confusion matrix visualization
- Feature importance analysis
- Cloud deployment
- Real-time API integration

---

## Conclusion

This project demonstrates the application of Machine Learning techniques to predict scholarship types using educational data.

The solution integrates:

- Data Analysis
- Machine Learning
- Model Serialization
- Web Application Development

providing a complete end-to-end Artificial Intelligence solution.

---

## License

This project was developed for academic purposes only.