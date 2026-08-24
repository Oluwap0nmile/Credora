# Credora
End-to-end machine learning application for predicting customer loan default risk.
The project combines data preprocessing, feature engineering, class-imbalance handling with SMOTE, model training, and an interactive Streamlit application for loan risk assessment.

## Live Demo

Try the deployed application here:

https://credora-loanprediction.streamlit.app/

## Project Overview

The goal of this project is to build a machine learning solution that can estimate a customer's probability of defaulting on a loan and classify the customer into a risk category.

The application allows users to enter customer information and receive:

- Predicted loan default outcome
- Probability of default
- Low, Medium, or High risk classification
- Customer assessment summary

## Machine Learning Approach

The project uses a Gradient Boosting Classifier as the final model.

Key steps in the machine learning workflow include:

1. Data cleaning and exploration
2. Feature engineering
3. Handling class imbalance using SMOTE
4. Feature scaling
5. Model training and evaluation
6. Saving the trained model and scaler
7. Building an interactive Streamlit application

## Feature Engineering

Three additional features were created from the customer's historical billing and payment information:

- `MAX_PAY_DELAY` — Maximum payment delay across the previous six months
- `AVG_BILL_AMT` — Average bill amount across the previous six months
- `AVG_PAY_AMT` — Average payment amount across the previous six months

## Model Performance

The final Gradient Boosting model achieved the following evaluation results:

| Metric | Score |
|---|---:|
| Accuracy | 74.8% |
| Precision | 44.5% |
| Recall | 60.9% |
| F1 Score | 51.4% |
| ROC-AUC | 69.8% |

## Key Features

The most influential features identified during model evaluation were:

| Feature | Importance |
|---|---:|
| MAX_PAY_DELAY | 55.85% |
| LIMIT_BAL | 25.56% |
| AGE | 7.28% |


















| AVG_PAY_AMT | 5.51% |
| AVG_BILL_AMT | 4.65% |
