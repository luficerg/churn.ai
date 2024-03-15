from src_python.components.data_validation import DataValidation
from src_python.components.data_transformation import DataTransformation 
from src_python.components.model_trainer import ModelTrainer
from src_python.components.model_evaluation import ModelEvaluation
import pandas as pd
import pickle
from pathlib import Path

train = pd.read_csv(Path('artifacts\data_ingestion\\train.csv'))
test = pd.read_csv(Path('artifacts\data_ingestion\\test.csv'))
model_name = Path('artifacts/model_trainer/model.pkl')

X = train.drop('Exited', axis=1)
y = train['Exited']
X_test = test.drop('Exited', axis = 1)
y_test = test['Exited']



STAGE_NAME = "Data Validation stage"
try:
   print(f">>>>>> stage {STAGE_NAME} started <<<<<<") 

   data_validation = DataValidation(train, 'schema.yaml')
   data_validation.run_validation()

   print(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        print(e)
        raise e



STAGE_NAME = "Data Transformation stage"
try:
   print(f">>>>>> stage {STAGE_NAME} started <<<<<<") 

   trans = DataTransformation()
   dataframe = trans.drop_duplicate(X)
   dataframe = trans.surname(dataframe)
   X_train = trans.sklearn_pipeline(dataframe)

   print(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        print(e)
        raise e




STAGE_NAME = "Model Trainer stage"
try:
   print(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   
   model_trainer = ModelTrainer(model = "vote")
   vote = model_trainer.train(train = train)
   # Open the file in binary write mode
   with open(model_name, "wb") as f:
      pickle.dump(vote, f)

   print(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        print(e)
        raise e



STAGE_NAME = "Model evaluation stage"
try:
   print(f">>>>>> stage {STAGE_NAME} started <<<<<<") 

   config = ModelEvaluation()
   config.test_log_into_mlflow(X_test, y_test, model_name)

   print(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        print(e)
        raise e