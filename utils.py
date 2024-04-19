import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
import os
import pickle


def Data_Saving_Func(file, data_path):
    try:
        os.makedirs(os.path.dirname(data_path), exist_ok=True)
        with open(data_path, "wb") as f:
            pickle.dump(file, f)
    except Exception as e:
        print("Error in {}".format(e))
        raise e
