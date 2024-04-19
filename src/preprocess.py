import pandas as pd
import numpy as np


class Feature_Engineering_Configure_Class:
    def __init__(self, data_feature) -> pd.DataFrame:
        self.data_feature = data_feature

    def Handling_Missing_Data(self):
        """
        This function fills in missing values in the dataframe with appropriate values.

        Parameters:
            data_feature (pandas.DataFrame): The input dataframe

        Returns:
            pandas.DataFrame: The input dataframe with missing values filled in

        Raises:
            Exception: If there is an error during the processing
        """
        try:
            self.data_feature["Shipment Mode"] = self.data_feature[
                "Shipment Mode"
            ].fillna("Air")
            self.data_feature["Line Item Insurance (USD)"] = self.data_feature[
                "Line Item Insurance (USD)"
            ].fillna(self.data_feature["Line Item Insurance (USD)"].median())
            self.data_feature = self.data_feature.drop("Dosage", axis=1)
            return self.data_feature
        except Exception as e:
            print("error in {}".format(e))
            raise e

    def Remove_Unwanted_data_Features(self):
        try:
            self.data = self.Handling_Missing_Data()
            self.data.drop("PQ #", axis=1, inplace=True)
            self.data.drop("Scheduled Delivery Date", axis=1, inplace=True)
            self.data.drop("ASN/DN #", axis=1, inplace=True)
            self.data.drop("PO / SO #", axis=1, inplace=True)
            self.data.drop("Dosage Form", axis=1, inplace=True)
            self.data.drop("Molecule/Test Type", axis=1, inplace=True)
            self.data.drop("Vendor", axis=1, inplace=True)
            self.data.drop("Manufacturing Site", axis=1, inplace=True)
            self.data.drop("Project Code", axis=1, inplace=True)
            self.data.drop("ID", axis=1, inplace=True)
            self.data.drop("PO Sent to Vendor Date", axis=1, inplace=True)
            self.data.drop("Item Description", axis=1, inplace=True)
            self.data.drop("Country", axis=1, inplace=True)
            return self.data
        except Exception as e:
            print("Error in {}".format(e))
            raise e

    def PQ_First_Sent_to_Client_Date_func(self, shipment_data_f):
        if shipment_data_f == "Pre-PQ Process":
            return pd.to_datetime("01/06/2009", format="%d/%m/%Y")
        elif shipment_data_f == "Date Not Captured":
            return " 2009-06-01"

        else:
            if len(shipment_data_f) < 9:
                shipment_data_f = pd.to_datetime(shipment_data_f, format="%m/%d/%y")
                return shipment_data_f
            else:
                shipment_data_f = shipment_data_f.replace("-", "/")
                shipment_data_f = pd.to_datetime(shipment_data_f, format="%d/%m/%Y")
                return shipment_data_f

    def PQ_First_Sent_to_Client_Date(self):
        try:
            self.data = self.Remove_Unwanted_data_Features()
            self.data["PQ First Sent to Client Date"] = self.data[
                "PQ First Sent to Client Date"
            ].apply(self.PQ_First_Sent_to_Client_Date_func)
            self.data["PQ First Sent to Client Date"] = pd.to_datetime(
                self.data["PQ First Sent to Client Date"]
            )
            self.data["PQ_Year"] = self.data["PQ First Sent to Client Date"].dt.year
            self.data["PQ_Month"] = self.data["PQ First Sent to Client Date"].dt.month
            self.data["PQ_Day"] = self.data["PQ First Sent to Client Date"].dt.day
            self.data.drop("PQ First Sent to Client Date", axis=1, inplace=True)
            self.data.drop(
                columns=["Delivered to Client Date", "Delivery Recorded Date"],
                inplace=True,
            )
            return self.data
        except Exception as e:
            print("Error in {}".format(e))
            raise e


def Process_post(data_path):
    """
    This function takes in a pandas dataframe as input and applies the PQ_First_Sent_to_Client_Date function to it.

    Parameters:
    data_path (pandas.DataFrame): The input dataframe

    Returns:
    pandas.DataFrame: The processed dataframe with the PQ_First_Sent_to_Client_Date column added
    """
    try:
        Feature_Engineering_Configure_Class_obj = Feature_Engineering_Configure_Class(
            data_feature=data_path
        )

        cleaned_data = (
            Feature_Engineering_Configure_Class_obj.PQ_First_Sent_to_Client_Date()
        )

        for col in cleaned_data.columns:
            if cleaned_data[col].dtype == "object":
                cleaned_data[col] = cleaned_data[col].astype("category")
            else:
                cleaned_data[col] = cleaned_data[col].astype("float64")

        return cleaned_data

    except Exception as e:
        raise e
