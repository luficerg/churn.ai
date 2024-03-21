# End-to-end-BANK-CHURN-with-MLflow

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
export MLFLOW_TRACKING_URI=https://dagshub.com/luficerg/Kaggle-Competitions.mlflow 

export MLFLOW_TRACKING_USERNAME= ##USERNAME

export MLFLOW_TRACKING_PASSWORD= ##PASSWORD

```