from src.preprocess import Process_post
from src.preprocess2 import Feature_Engineering_Configuration
import pandas as pd
import numpy as np


def Data_transformation(data: pd.DataFrame) -> pd.DataFrame:
    try:
        Cleaned_data = Process_post(data_path=data)
        return Cleaned_data

    except Exception as e:
        print("Error in {}".format(e))
        raise e
