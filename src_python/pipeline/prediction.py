import pickle
from pathlib import Path
from ensure import ensure_annotations
import pandas as pd

model_name = Path('artifacts/model_trainer/model.pkl')

class PredictionPipeline:
    def __init__(self):
        # Load the trained model from the file
        with open(model_name, "rb") as f:
            self.model = pickle.load(f)

    @ensure_annotations
    def predict(self, data : pd.DataFrame):
        prediction = self.model.predict(data)

        prediction = 'Yes' if prediction == 1 else 'No'

        return prediction