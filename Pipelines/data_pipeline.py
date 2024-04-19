import numpy as np
import pandas as pd
from src.data_ingestion import Data_processing_config
from src.steps.clean_data import Data_transformation
from src.evaluation import Data_evaluation
from src.preprocess import Process_post
from src.preprocess2 import Feature_Engg_Func
from src.data_split import Data_Split_Process_post
from src.data_training import Model_trainings_Process_post


def data_pipeline(data_path: str) -> pd.DataFrame:
    """
    Runs the pipeline on the given data.

    Args:
        data_path (str): The path to the data file.

    Returns:
        pd.DataFrame: The cleaned data.

    Raises:
        Exception: If there is an error during the pipeline.
    """
    try:
        # instantiate the data processing class
        data = Data_processing_config(data_path=data_path)
        print("Data Ingestion Compleate....")

        # instantiate the data transformation class
        cleaned_data = Process_post(data_path=data)
        print("Data Cleaning is Complete....")

        cleaned_data_arr = Feature_Engg_Func(cl_data=cleaned_data)
        print("Feature Engineering is Complete....")

        Model_trainings_Process_post(data=cleaned_data_arr)

    except Exception as e:
        print(f"error in {e}")
        raise e
