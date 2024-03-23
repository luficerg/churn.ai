# End-to-end-BANK-CHURN-with-MLflow


# Motivation:
Customer churn is a critical concern for banks as retaining existing customers is often more cost-effective than acquiring new ones. Predicting customer churn can help banks identify at-risk customers and take proactive measures to retain them. This project leverages machine learning techniques to predict customer churn based on various attributes provided in the dataset. By accurately identifying customers likely to churn, banks can implement targeted retention strategies, ultimately improving customer satisfaction and reducing revenue loss.

# Features:

- **Customer ID**: Unique identifier for each customer.
- **Surname**: Customer's surname or last name.
- **Credit Score**: Numerical value representing the customer's credit score.
- **Geography**: Country where the customer resides (France, Spain, or Germany).
- **Gender**: Customer's gender (Male or Female).
- **Age**: Customer's age.
- **Tenure**: Number of years the customer has been with the bank.
- **Balance**: Customer's account balance.
- **NumOfProducts**: Number of bank products the customer uses (e.g., savings account, credit card).
- **HasCrCard**: Whether the customer has a credit card (1 = yes, 0 = no).
- **IsActiveMember**: Whether the customer is an active member (1 = yes, 0 = no).
- **EstimatedSalary**: Estimated salary of the customer.

## Solution:

The solution provided in this repository involves an end-to-end pipeline for predicting customer churn using machine learning. Here's an overview of the solution:

1. **Data Preprocessing**: 
   - Handle missing values.
   - Encode categorical variables.
   - Scale numerical features.

2. **Feature Engineering**:
   - Extract relevant features.
   - Perform feature scaling if necessary.

3. **Model Selection**:
   - Choose appropriate machine learning algorithms for classification (e.g., Random Forest, Gradient Boosting, Logistic Regression) or just use combined them all.

4. **Model Training**:
   - Train the selected models using the preprocessed data.

5. **Model Evaluation**:
   - Evaluate model performance using suitable metrics such as accuracy, precision, recall, ROC_AUC Score and F1-score.
   - Perform cross-validation to ensure generalization.

6. **Hyperparameter Tuning** :
   - Tune hyperparameters of selected models to optimize performance by using **OPTUNA**

7. **Deployment**:
   - Deploy the trained model using Streamlit for creating a user-friendly web application.
   - Users can input customer information and get predictions on whether the customer is likely to churn.
  
# How to run?
### STEPS:

Clone the repository

```bash
git clone https://github.com/luficerg/churn.ai
```
### STEP 01- Create a virtual environment after opening the repository

```bash
conda create -n venv python=3.10 -y
```

```bash
conda activate venv
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```

### STEP 03- Streamlit
```bash
streamlit run .\app.py
```

Now you can enjoy it , but if you don't have it installed streamlit and want to know more in details, you can check out src and notebook_research folder

```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/luficerg/Kaggle-Competitions.mlflow \

export MLFLOW_TRACKING_USERNAME=luficerg \

export MLFLOW_TRACKING_PASSWORD= 251c01a63af78636ff098c62735d662f759756ce \

```
