import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import os
from utils import Data_Saving_Func


class Feature_Engineering_Configuration:
    """
    This class is used to perform the feature engineering on the data. It takes in the data and performs the necessary steps to prepare the data for training the model.

    Args:
        data (pd.DataFrame): The data that needs to be transformed.

    Attributes:
        data (pd.DataFrame): The data that needs to be transformed.
        data_path (str): The path where the transformed data needs to be saved.

    """

    def __init__(self, data: pd.DataFrame):
        self.data = data
        self.data_path = os.path.join(
            "/mnt/d/my projects/consignment_pricing_prediction_using_mlops_cicd/models/transform_pipeine.pickle"
        )

    def Numarics_catagorics_cols(self):
        """
        This function is used to get the list of numeric and categorical columns in the data.

        Returns:
            tuple: A tuple containing the list of numeric and categorical columns.

        """
        try:
            catagorical_fe_cols = []
            numaric_fe_cols = []
            for col in self.data.columns:
                if self.data[col].dtype == "category":
                    catagorical_fe_cols.append(col)
                else:
                    numaric_fe_cols.append(col)
            return (numaric_fe_cols, catagorical_fe_cols)
        except Exception as e:
            print(f"error in {e}")
            raise e

    def NumricPipeline(self):
        """
        This function is used to create the pipeline for the numeric features.

        Returns:
            Pipeline: The pipeline for the numeric features.

        """
        return Pipeline([("scaler", StandardScaler())])

    def CatagoicalPipeline(self):
        return Pipeline([("onehot", OneHotEncoder())])

    def Feture_Eng_Config_Pipeline(self):
        """
        This function is used to perform the feature engineering on the data. It creates the pipelines for the numeric and categorical features, applies the pipelines to the data, and saves the transformed data.

        Returns:
            np.ndarray: The transformed data.

        """
        try:
            numaric_fe_cols, catagorical_fe_cols = self.Numarics_catagorics_cols()
            numaric_fe_cols.remove("Line Item Insurance (USD)")
            col_Transformer = ColumnTransformer(
                [
                    ("numarics", self.NumricPipeline(), numaric_fe_cols),
                    ("catagoricals", self.CatagoicalPipeline(), catagorical_fe_cols),
                ]
            )
            data_r = self.data.drop(["Line Item Insurance (USD)"], axis=1)
            target_data_r = self.data["Line Item Insurance (USD)"].values
            transformed_data = col_Transformer.fit_transform(data_r).toarray()
            Data_Saving_Func(file=transformed_data, data_path=self.data_path)
            print("Transformed data Pipeline is Saved....")
            target_data_r = np.array(target_data_r)
            data_array = np.c_[transformed_data, target_data_r]
            return data_array

        except Exception as e:
            print(f"error in {e}")
            raise e


def Feature_Engg_Func(cl_data: pd.DataFrame) -> np.ndarray:
    """
    This function is used to perform the feature engineering on the data.

    Args:
        cl_data (pd.DataFrame): The data that needs to be transformed.

    Returns:
        np.ndarray: The transformed data.

    Raises:
        Exception: If there is an error during the feature engineering process.

    """
    try:
        Feature_Engineering_Configuration_obj = Feature_Engineering_Configuration(
            data=cl_data
        )

        return Feature_Engineering_Configuration_obj.Feture_Eng_Config_Pipeline()
    except Exception as e:
        print(f"error in {e}")
        raise e
