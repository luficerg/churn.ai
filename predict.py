from pathlib import Path
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import pickle
from ensure import ensure_annotations

# Path to the trained model file
model_name = Path('artifacts/model_trainer/model.pkl')

# Initialize LabelEncoder for processing categorical data
label_encoder = LabelEncoder()

class PredictionPipeline:
    """Class for making predictions using a trained machine learning model."""

    def __init__(self):
        """
        Initialize PredictionPipeline with a trained model.

        Loads the trained model from the specified file path.
        """
        with open(model_name, "rb") as f:
            self.model = pickle.load(f)

    @ensure_annotations
    def predict(self, data: pd.DataFrame) -> str:
        """
        Make predictions on new data.

        Args:
            data (pd.DataFrame): Input data for making predictions.

        Returns:
            str: Prediction result as a string ('1' for churn, '0' for non-churn).

        Raises:
            Exception: If an error occurs during prediction.
        """
        try:
            # Encode categorical feature 'Surname' using LabelEncoder
            data['Surname'] = label_encoder.fit_transform(data['Surname'])
            
            # Make predictions using the loaded model
            prediction = self.model.predict_proba(data)[:,1]
            
            # Convert prediction to '1' for atleast 0.25 probability churn, '0' for non-churn
            prediction = '1' if prediction >= 0.25 else '0'

            return prediction
        
        except Exception as e:
            # Print error message if an exception occurs during prediction
            print('The Exception message is: ', e)
            return 'something is wrong'  # Return error message
