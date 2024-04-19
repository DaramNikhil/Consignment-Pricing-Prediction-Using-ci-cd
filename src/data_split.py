import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from utils import Data_Saving_Func


class Data_split_class:
    def __init__(self, data):
        self.data = data
        self.train_data_path = os.path.join(
            "/mnt/d/my projects/consignment_pricing_prediction_using_mlops_cicd/data/processed_data/train_data.csv"
        )
        self.test_data_path = os.path.join(
            "/mnt/d/my projects/consignment_pricing_prediction_using_mlops_cicd/data/processed_data/test_data.csv"
        )

    def Data_Split_Process(self):

        train_data, test_data = train_test_split(
            self.data, test_size=0.2, random_state=42, shuffle=True
        )

        Data_Saving_Func(file=train_data, data_path=self.train_data_path)
        Data_Saving_Func(file=test_data, data_path=self.test_data_path)

        return (self.train_data_path, self.test_data_path)


def Data_Split_Process_post(data):
    Data_split_class_obj = Data_split_class(data=data)
    return Data_split_class_obj.Data_Split_Process()
