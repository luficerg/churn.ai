from src_python.components.data_transformation import DataTransformation
from sklearn.model_selection import train_test_split
from lightgbm import LGBMClassifier
from catboost import CatBoostClassifier
from xgboost import XGBClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score
from ensure import ensure_annotations
from sklearn.pipeline import Pipeline
from pathlib import Path
import pickle
import pandas as pd
from sklearn.model_selection import train_test_split

class ModelTrainer:
    """
    Class for training and evaluating models for a given dataset.
    """

    @ensure_annotations
    def __init__(self, model: str):
        """
        Initializes the ModelTrainer with the specified model type.

        Parameters:
        - model (str): Type of model to train ("Cat", "XGB", or "LGBM") and rest of is voting.
        """
        self.model = model

    @ensure_annotations
    def train(self, train: pd.DataFrame):
        """
        Trains the specified model on the provided training dataset.

        Parameters:
        - train (pd.DataFrame): Training dataset.

        Returns:
        - trained_model: Trained model or pipeline.
        """
        # Data preprocessing
        trans = DataTransformation()
        train = trans.drop_duplicate(train)
        train = trans.surname(train)
        X = train.drop('Exited', axis=1)
        y = train['Exited']
        preprocessor = trans.sklearn_pipeline(X)

        # Split data into training and validation sets
        X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

        # Define models with best hyperparameters
        best_xgb_model = XGBClassifier(**{
            'n_estimators': 810, 'learning_rate': 0.07921079869615913,
            'max_depth': 5, 'min_child_weight': 8, 'gamma': 0.27423983829634263,
            'random_state': 42, 'objective': 'binary:logistic',
            'eval_metric': 'auc', 'n_jobs': -1})
        XGB_best = Pipeline(steps=[('preprocessor', preprocessor), ('model', best_xgb_model)])

        best_catboost_model = CatBoostClassifier(**{
            'iterations': 830, 'learning_rate': 0.08238714339235984,
            'depth': 5, 'l2_leaf_reg': 0.8106903985997884,
            'random_state': 42, 'verbose': 0})
        Cat_best = Pipeline(steps=[('preprocessor', preprocessor), ('model', best_catboost_model)])

        best_lgbm_model = LGBMClassifier(**{
            'n_estimators': 960, 'learning_rate': 0.031725771326186744,
            'max_depth': 8, 'min_child_samples': 8,
            'subsample': 0.7458307885861184, 'colsample_bytree': 0.5111460378911089,
            'random_state': 42})
        LGBM_best = Pipeline(steps=[('preprocessor', preprocessor), ('model', best_lgbm_model)])

        # Train and evaluate the specified model
        if self.model == "Cat":
            Cat_best.fit(X_train, y_train)
            predictions = Cat_best.predict(X_val)
            acu = accuracy_score(y_val, predictions)
            print(acu)
            return Cat_best
        elif self.model == "XGB":
            XGB_best.fit(X_train, y_train)
            predictions = XGB_best.predict(X_val)
            acu = accuracy_score(y_val, predictions)
            print(acu)
            return XGB_best
        elif self.model == "LGBM":
            LGBM_best.fit(X_train, y_train)
            predictions = LGBM_best.predict(X_val)
            acu = accuracy_score(y_val, predictions)
            print(acu)
            return LGBM_best

        # Create a voting classifier if model type is not specified
        voting = VotingClassifier(estimators=[
            ('Model1', LGBM_best),
            ('Model2', XGB_best),
            ('Model3', Cat_best)
        ], voting='soft', weights=[0.5, 0.3, 0.2])

        # Train and evaluate the voting classifier
        voting.fit(X_train, y_train)
        predictions = voting.predict(X_val)
        acu = accuracy_score(y_val, predictions)
        print(acu)
        return voting

if __name__ == '__main__':
    try:
        train = pd.read_csv(Path('artifacts\data_ingestion\\train.csv'))
        model_name = Path('artifacts/model_trainer/model.pkl')


        model_trainer = ModelTrainer(model = "vote")
        vote = model_trainer.train(train = train)

        # Open the file in binary write mode
        with open(model_name, "wb") as f:
            pickle.dump(vote, f)
    
    except Exception as e:
        raise e

