import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor

from src.exceptions import CustomException
from src.logger import logging
from src.utils import save_object, evaluate_model

from dataclasses import dataclass
import os, sys

@dataclass
class ModelTrainingConfig:
    trained_model_file_path = os.path.join('artifacts', 'model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainingConfig()

    def initiate_model_training(self, train_array, test_array):
        try:
            logging.info('Splitting dependent and independent variables from train and test data')
            logging.info(f'train_array {len(train_array)} tes_array {len(test_array)}')
            x_train, y_train, x_test, y_test = (
                train_array[:, :-1],
                train_array[:, -1],
                test_array[:, :-1],
                test_array[:, -1],
            )
            logging.info('dfshg')
            models = {
                'LinearRegression': LinearRegression(),
                'Lasso': Lasso(),
                'Ridge': Ridge(),
                'ElasticNet': ElasticNet(),
                'DecisionTree': DecisionTreeRegressor()
            }
            logging.info('fykjghj')
            model_report:dict = evaluate_model(x_train, y_train, x_test, y_test, models)
            logging.info('hgkjhk')
            print(model_report)
            print('\n===================================================================================================')
            logging.info(f'Model Report: {model_report}')

            # To get best model score from dict

            best_model_score = max(sorted(model_report.values()))

            best_model_name = list(model_report.keys()) [
                list(model_report.values()).index(best_model_score)
            ]

            best_model = models[best_model_name]

            print(f'Best model found, model name: {best_model_name}, r2 Score {best_model_score}')
            print('\n===================================================================================================')
            logging.info(f'Best model found, model name: {best_model_name}, r2 Score {best_model_score}')

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj = best_model
            )

        except Exception as e:
            logging.info("Error occured when training the data")
            raise CustomException(e, sys)