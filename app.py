from flask import Flask, render_template, request, jsonify
import os 
import streamlit as st
from streamlit.components import v1 as components
import pandas as pd
from src_python.pipeline.prediction import PredictionPipeline

app = Flask(__name__) # initializing a flask app

# @app.route('/train',methods=['GET'])  # route to train the pipeline
# def training():
#     os.system("python main.py")
#     return "Training Successful!" 

# @app.route('/',methods=['GET'])  # route to display the home page
# def homePage():
#     return render_template("index.html")


def main():
    st.title("Embedding React App in Streamlit")

    print(os.getcwd())
    # Load your React app's HTML content
    with open("build\\index.html", "r") as f:
        react_html = f.read()

    my_component = components.declare_component("build", url = "https://localhost:3000")
    # Render the HTML content using Streamlit components
    components.html(react_html, height=800)

# @app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
# def index():
#     if request.method == 'POST':
#         try:
#             #  reading the inputs given by the user
#             CustomerId = int(request.form['CustomerId'])
#             Surname = request.form['Surname']
#             CreditScore = int(request.form['CreditScore'])
#             Geography = request.form['Geography']
#             Gender = request.form['Gender']
#             Age = float(request.form['Age'])
#             Tenure = int(request.form['Tenure'])
#             Balance = float(request.form['Balance'])
#             NumOfProducts = int(request.form['NumOfProducts'])
#             HasCrCard = float(request.form['HasCrCard'])
#             IsActiveMember = float(request.form['IsActiveMember'])
#             EstimatedSalary = float(request.form['EstimatedSalary'])

#             # Create a DataFrame from the input data
#             data = {
#                 'CustomerId': [CustomerId], 'Surname': [Surname], 'CreditScore': [CreditScore],
#                 'Geography': [Geography], 'Gender': [Gender], 'Age': [Age], 'Tenure': [Tenure],
#                 'Balance': [Balance], 'NumOfProducts': [NumOfProducts], 'HasCrCard': [HasCrCard],
#                 'IsActiveMember': [IsActiveMember], 'EstimatedSalary': [EstimatedSalary]
#             }
#             df = pd.DataFrame(data)

            
#             obj = PredictionPipeline()
#             predict = obj.predict(df)
#             print(predict)


#             return jsonify({"prediction": predict})

#         except Exception as e:
#             print('The Exception message is: ',e)
#             return 'something is wrong'

#     else:
#         return render_template("index.html")



if __name__ == "__main__":
    main()
	