import yaml
from ensure import ensure_annotations
import pandas as pd
from pathlib import Path



class DataValidation:

    """
    Example usage:
    Assuming you have a DataFrame named 'data' and the path to the schema file is 'schema.yaml'
    data_validation = DataValidation(data, 'schema.yaml')
    data_validation.run_validation()
    The following reasons for ensure_annotation is given in reason.ipynb
    """
    
    @ensure_annotations
    def __init__(self, dataframe: pd.DataFrame, schema_path: str):
        self.dataframe = dataframe
        self.schema_path = schema_path
        self.validation_status = False
    
    @ensure_annotations
    def read_schema(self)-> dict:
        """
        Args:
            path_to_yaml (str): path like input

        Raises:
            ValueError: if yaml file is empty
            e: empty file

        Returns:
            ConfigBox: ConfigBox type
        """
        try:    
            with open(self.schema_path) as schema_file:
                schema = yaml.safe_load(schema_file)

        except:
            raise ValueError("Schema file is empty")
    
        return schema
        
    @ensure_annotations
    def validate_data(self)-> bool :
        schema = self.read_schema()
        columns = schema.keys()
        # Check if all columns in schema are present in dataframe
        if not set(columns).issubset(set(self.dataframe.columns)):
            print("Validation Failed for columns, columns are not matching in dataframe")
            return False
        
        # Check data types
        for column, dtype in schema.items():
            if self.dataframe[column].dtype.name != dtype:
                print("Validation Failed for columns, datatypes do not match")
                return False
        
        print("Validation Succedded for columns")
        return True
    
    def save_validation_status(self):

        """save validation status into file """

        status_path = "artifacts/data_validation/status.txt"
        with open(status_path, "w") as status_file:
             status_file.write("Validation Status: " + str(self.validation_status))
    
    def run_validation(self):
        self.validation_status = self.validate_data()
        self.save_validation_status()
        

if __name__ ==   '__main__':
    try:
        data = pd.read_csv(Path('artifacts\data_ingestion\\train.csv'))

        data_validation = DataValidation(data, 'schema.yaml')
        data_validation.run_validation()

    except Exception as e:
        raise e
