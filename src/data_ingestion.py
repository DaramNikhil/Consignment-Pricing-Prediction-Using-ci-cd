import numpy as np
import pandas as pd
import os


class Data_ingestion_config:
    """
    This class is used to configure the data ingestion process.

    Parameters:
    data_path (str): The path of the data file.

    Attributes:
    data_path (str): The path of the data file.

    """

    def __init__(self, data_path):
        """
        Initialize the class with the data path.

        Args:
        data_path (str): The path of the data file.

        """
        self.data_path = data_path

    def data_ingestion(self):
        return pd.read_csv(self.data_path)


def Data_processing_config(data_path):
    """
    This function is used to process the data from the given data path.

    Parameters:
    data_path (str): The path of the data file.

    Returns:
    data (DataFrame): The processed data.

    """
    data_ingestion_config_obj = Data_ingestion_config(data_path)
    data = data_ingestion_config_obj.data_ingestion()
    return data
