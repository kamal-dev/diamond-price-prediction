import os
import sys
import pickle
import numpy as np
import pandas as pd

from src.exceptions import CustomException
from src.logger import logging

from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            pickle.dump(obj, file_obj)
    except Exception as e:
        logging.info(f'Error occured when writing the to the pickle file path {file_path}')
        raise CustomException(e, sys)

def evaluate_model(x_train,y_train,x_test,y_test,models):
    try:
        report = {}
        logging.info(f'x_train: {len(x_train)}')
        for i in range(len(models)):
            model = list(models.values())[i]
            # Train model
            model.fit(x_train,y_train)
            
            # Predict Testing data
            y_test_pred =model.predict(x_test)

            # Get R2 scores for train and test data
            #train_model_score = r2_score(ytrain,y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] =  test_model_score

        return report
    
    except Exception as e:
            logging.info('Exception occured during model training')
            raise CustomException(e,sys)

def load_object(file_path):
    try:
          with open(file_path, 'rb') as file_obj:
               return pickle.load(file_obj)
    except Exception as e:
         logging.info('Exception occured in load_object function utils')
         raise CustomException(e, sys)