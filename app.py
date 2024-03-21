import streamlit as st
from src.data_validation import DataValidation
import pandas as pd
import random
from pathlib import Path
from predict import PredictionPipeline
from PIL import Image

@st.cache_data
def import_img(path):
    data = Image.open(Path(path))
    return data

####STREAMLIT CODE #####
hide = """
    <style>
    #MainMenu {visibility:hidden;}
    footer {visibility:hidden;}
    </style>"""

st.markdown(hide, unsafe_allow_html=True)

st.title("Churn Bank Model Trainer")
st.write("""
This app will help you to train a machine learning model to predict whether a customer will churn or not.
Here are some examples of the test data , you can test model , [here is original file](https://www.kaggle.com/competitions/playground-series-s4e1/data)
""")

df = pd.read_csv(Path('app\\small_example.csv'))

st.dataframe(df)

# Define the choice for the user
choice = st.radio("Choose an option:", ("Select a Random or Your example", "Enter your own inputs"))

if choice == "Select a Random or Your example":

    example = st.button("Take a Random example", type="primary")

    if example:
        # generate a random number between 0 and 74
        num = random.randint(0, 74)
        st.write("This is the testing example:",num)
        df_example = df.iloc[num]
        print(df_example)

    else:
        # user specified a random number
        num = st.number_input("Enter a random number between 0 and 74", step = 1, min_value = 0, max_value = 74)
        df_example = df.iloc[num]
        print(df_example)

    #  reading the inputs given by the user
    CustomerId = st.number_input('CustomerID', step = 1, value = df_example.CustomerId)
    Surname = st.text_input('Surname', value = df_example.Surname)
    CreditScore = st.number_input('CreditScore', step = 1, min_value = 300, max_value = 900 , value = df_example.CreditScore)

    Geo = ('France', 'Germany', 'Spain', 'Others')
    Geography = st.selectbox(
        'Geography', Geo, index = Geo.index(df_example.Geography))
    
    Gen = ('Male', 'Female','Others')
    Gender = st.selectbox(
        'Gender', Gen, index = Gen.index(df_example.Gender))
    
    Age = st.number_input('Age', step = 1., min_value = 1., max_value = 150., value = df_example.Age)
    Tenure = st.number_input('Tenure', step = 1, min_value = 0, max_value = 15, value = df_example.Tenure)
    Balance = st.number_input('Balance', value = df_example.Balance)
    NumOfProducts = st.number_input('NumOfProducts', step = 1, value = df_example.NumOfProducts)
    HasCrCard = st.selectbox('HasCrCard', (0.,1.), index = (0.,1.).index(df_example.HasCrCard))
    IsActiveMember = st.selectbox('IsActiveMember', (0.,1.), index = (0.,1.).index(df_example.IsActiveMember))
    EstimatedSalary = st.number_input('EstimatedSalary', min_value = 1., step = 1000., value = df_example.EstimatedSalary)

else:

    #  reading the inputs given by the user
    CustomerId = st.number_input('CustomerID', step = 1)
    Surname = st.text_input('Surname')
    CreditScore = st.number_input('CreditScore', step = 1, min_value = 300, max_value = 900)
    Geography = st.selectbox(
        'Geography', ('France', 'Germany', 'Spain', 'Others'))

    Gender = st.selectbox(
        'Gender', ('Male', 'Female','Others'))
    Age = st.number_input('Age', step = 1., min_value = 1., max_value = 150.)
    Tenure = st.number_input('Tenure', step = 1, min_value = 0, max_value = 15)
    Balance = st.number_input('Balance')
    NumOfProducts = st.number_input('NumOfProducts', step = 1)
    HasCrCard = st.selectbox('HasCrCard', (0.,1.))
    IsActiveMember = st.selectbox('IsActiveMember', (0.,1.))
    EstimatedSalary = st.number_input('EstimatedSalary', step = 1000., min_value = 1.)

predict = st.button("Predict", type="primary")
 
if predict:
    # Create a DataFrame from the input data
    data = {
        'CustomerId': [CustomerId], 'Surname': [Surname], 'CreditScore': [CreditScore],
        'Geography': [Geography], 'Gender': [Gender], 'Age': [Age], 'Tenure': [Tenure],
        'Balance': [Balance], 'NumOfProducts': [NumOfProducts], 'HasCrCard': [HasCrCard],
        'IsActiveMember': [IsActiveMember], 'EstimatedSalary': [EstimatedSalary]
    }
    df = pd.DataFrame(data)

    # Validate the DataFrame from the input data
    data_validation = DataValidation(df, 'schema.yaml')
    status = data_validation.validate_data()
    st.write(status, "validation for data validation(it matches input with its datatype..) ")

    if status:
        obj = PredictionPipeline()
        preds = obj.predict(df)
        print(preds)
    else:
        print('error: %s' % status)

    st.write('Prediction For Customer Churn: ',str(preds))

    corr = import_img('app\correlation-coefficient.webp')
    img = import_img('app\corr.png')

    st.header('How to check for correlation')
    st.image(corr, caption = 'correlation')
    st.header('Check the correlation of feature here')
    st.image(img, caption='actual correlation')
    st.write('Here, Age feature has highest positive correlation with Bank Churn (Exited), so age have highest predictive power for Churn (Exited)')

else:
    st.write('Prediction For Customer Churn: -')