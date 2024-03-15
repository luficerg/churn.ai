import os
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, roc_auc_score, f1_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import pickle
import json
from pathlib import Path

os.environ["MLFLOW_TRACKING_URI"]="https://dagshub.com/luficerg/Kaggle-Competitions.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"]="luficerg"
os.environ["MLFLOW_TRACKING_PASSWORD"]="251c01a63af78636ff098c62735d662f759756ce"

class ModelEvaluation:
    """
    Class for evaluating and logging metrics for machine learning models.
    """

    def __init__(self):
        """
        Initializes the ModelEvaluation class.
        """
        pass
    
    def eval_metrics_classification(self, actual, pred):
        """
        Computes classification metrics for the given predictions and ground truth labels.

        Parameters:
        - actual: True labels.
        - pred: Predicted labels.

        Returns:
        - Tuple of classification metrics: accuracy, precision, recall, ROC AUC, F1 score.
        """
        accuracy = accuracy_score(actual, pred)
        precision = precision_score(actual, pred)
        recall = recall_score(actual, pred)
        roc_auc = roc_auc_score(actual, pred)
        f1 = f1_score(actual, pred)
        return accuracy, precision, recall, roc_auc, f1

    def test_log_into_mlflow(self, test_x: pd.DataFrame, test_y: pd.DataFrame, model_name: str):
        """
        Tests the specified model on test data and logs evaluation metrics into MLflow.

        Parameters:
        - test_x (pd.DataFrame): Test features.
        - test_y (pd.DataFrame): True labels of the test data.
        - model_name (str): Path to the trained model file.
        """
        # Load the trained model from the file
        with open(model_name, "rb") as f:
            model = pickle.load(f)

        # Initialize MLflow tracking
        mlflow.set_registry_uri("MLFLOW_TRACKING_URI")
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():
            # Make predictions on test data
            predicted_qualities = model.predict(test_x)

            # Compute evaluation metrics
            accuracy, precision, recall, roc_auc, f1 = self.eval_metrics_classification(test_y, predicted_qualities)

            # Log metrics to MLflow
            mlflow.log_metric("accuracy", accuracy)
            mlflow.log_metric("precision", precision)
            mlflow.log_metric("recall", recall)
            mlflow.log_metric("roc_auc", roc_auc)
            mlflow.log_metric("f1", f1)

            # Save metrics as a local JSON file
            scores = {"accuracy": accuracy, "precision": precision, "recall": recall, "roc_auc": roc_auc, "f1": f1}
            with open("artifacts//model_evaluation//metrics.json", "w") as out_file:
                json.dump(scores, out_file, indent=4)

            # Log the trained model into MLflow
            if tracking_url_type_store != "file":
                # Register the model in the Model Registry if not using file store
                mlflow.sklearn.log_model(model, "model", registered_model_name="Voting")
            else:
                mlflow.sklearn.log_model(model, "model")


if __name__ == "__main__":
    try:
        test = pd.read_csv(Path('artifacts\data_ingestion\\test.csv'))
        model_name = Path('artifacts/model_trainer/model.pkl')
        X_test = test.drop('Exited', axis = 1)
        y_test = test['Exited']

        config = ModelEvaluation()
        config.test_log_into_mlflow(X_test, y_test, model_name)

    except Exception as e:
        raise e