import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,MinMaxScaler, LabelEncoder
from ensure import ensure_annotations
from pathlib import Path



class DataTransformation:
    def __init__(self):
        pass

    
    @ensure_annotations
    def drop_duplicate(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        """
        This method drops duplicate rows from the given DataFrame
        ."""

        dataframe = dataframe.drop_duplicates()
        return dataframe
    
    
    @ensure_annotations
    def surname(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        """
        This method encodes the 'Surname' column using LabelEncoder.
        """

        label_encoder = LabelEncoder()
        dataframe = dataframe.copy()
        dataframe['Surname'] = label_encoder.fit_transform(dataframe['Surname'])
        return dataframe
    
    
    @ensure_annotations
    def sklearn_pipeline(self, dataframe: pd.DataFrame):
        """
        This method constructs a preprocessing pipeline using sklearn's ColumnTransformer for both numerical and categorical data.
        """
        try:
            num = dataframe.select_dtypes(include=['int64', 'float64']).columns
            col = dataframe.select_dtypes(include=['object']).columns

            # Preprocessing for numerical data: imputation and scaling
            numerical_transformer = Pipeline(steps=[
                ('imputer', SimpleImputer(strategy='median')),
                ('scaler', MinMaxScaler())])

            # Preprocessing for categorical data: imputation and one-hot encoding
            categorical_transformer = Pipeline(steps=[
                ('imputer', SimpleImputer(strategy='most_frequent')),
                ('onehot', OneHotEncoder(handle_unknown='ignore'))])

            preprocessor = ColumnTransformer(
                transformers=[
                    ('num', numerical_transformer, num),
                    ('cat', categorical_transformer, col)])
        
            return preprocessor


        
        except Exception as e:
            raise print(e)

if __name__ ==   '__main__':
    try:
        train = pd.read_csv(Path('artifacts\data_ingestion\\train.csv'))
        test = pd.read_csv(Path('artifacts\data_ingestion\\test.csv'))

        trans = DataTransformation()
        dataframe = trans.drop_duplicate(train)
        dataframe = trans.surname(dataframe)
        X_train = trans.sklearn_pipeline(dataframe)

        print('Data Transformation Successfully')

    except Exception as e:
        print('Data Transformation Failure')
        raise e