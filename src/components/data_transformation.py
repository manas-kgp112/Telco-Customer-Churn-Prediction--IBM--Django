# Importing libraries
import os
import sys
import pandas as pd
import numpy as np
from dataclasses import dataclass
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split



# Importing Custom Exception and Logger
from src.exception import CustomException
from src.logger import logging
from src.utils import save_object


# Importing custom modules



'''
    This script contains the data_transformation pipeline : performs preprocessing on the data.
    Steps done in this script include :
        1} Label Encoding for categorical data
        2} Dummy variables
        3}

'''


# specifies path to store preprocessor model file
@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join("artifacts", "transformer", "preprocessor.pkl")



# DataTransformation() class processes the data
class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    # This function exports the data transformation features
    def data_transformation_object(self):
        try:

            dummy_cat_features = [
                'Gender', 'Senior Citizen', 'Partner', 'Dependents', 'Phone Service', 'Multiple Lines',
                'Internet Service','Online Security', 'Online Backup', 'Device Protection', 'Tech Support', 
                'Streaming TV', 'Streaming Movies', 'Contract','Paperless Billing', 'Payment Method'
            ]

            drop_features = [
                'CustomerID', 'Lat Long', 'Churn Reason', 'Country', 'State',
                'City', 'Zip Code', 'Churn Label', 'Count', 'Churn Score'
            ]

            transformation_pipeline = Pipeline(
                steps=[
                    ("one hot encoder", OneHotEncoder())
                ]
            )

            preprocessor = ColumnTransformer([
                ("transformation_pipeline", transformation_pipeline, dummy_cat_features)
            ], remainder='passthrough')

            logging.info("Data transformation object extracted.")


            return (
                preprocessor,
                drop_features
            )
        except Exception as e:
            raise CustomException(e, sys)
        



    # This function collects the data_transformation object() and applies it on the dataset
    def initiate_data_transformation(self, data:pd.DataFrame):
        try:
            logging.info("Initiating data transformation sequence...")
            preprocessor, drop_features = self.data_transformation_object()

            # Dumping some features and changing dtypes
            data_new = data.drop(drop_features, axis=1)
            data_new['Total Charges'] = pd.to_numeric(data_new['Total Charges'], errors='coerce')

            # Dumping all null values
            data_new.dropna(axis=0, inplace=True)

            # Splitting the dataset into train and test dataset
            X_train, X_val, Y_train, Y_val = self.split_dataset(data_new)

            logging.info("Applying preprocessing object on training dataframe")
            train_data = preprocessor.fit_transform(X_train)
            val_data = preprocessor.transform(X_val)      
            logging.info("Data transformed successfully")

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessor
            )

            return (
                train_data,
                Y_train,
                val_data,
                Y_val
            )

        except Exception as e:
            raise CustomException(e, sys)




    # This function splits the data into train and validation set
    def split_dataset(self, data):
        try:
            X = data.drop(['Churn Value'], axis=1)
            Y = data['Churn Value']

            X_train, X_val, Y_train, Y_val = train_test_split(X, Y, test_size=0.2, random_state=42)

            return (
                X_train,
                X_val,
                Y_train,
                Y_val
            )
        except Exception as e:
            raise CustomException(e, sys)