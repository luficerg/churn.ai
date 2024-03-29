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

# 1. Streamlit Life

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


# 2. AWS-CICD-Deployment-with-Github-Actions(Complex Step)

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 727204150125.dkr.ecr.ap-south-1.amazonaws.com/churn.ai

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = ap-south-1

    AWS_ECR_LOGIN_URI = demo>>  727204150125.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = churn.ai