import pandas as pd
import os
from Pipelines.data_pipeline import data_pipeline


data_path = r"/mnt/d/my projects/consignment_pricing_prediction_using_mlops_cicd/data/raw/Consignment_pricing_raw.csv"
df = data_pipeline(data_path=data_path)
