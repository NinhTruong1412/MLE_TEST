import pandas as pd
import logging
from fastapi import HTTPException, status
import joblib
logging.basicConfig(format="%(asctime)s %(levelname)s %(message)s", level=logging.INFO)

class PredictSale:
    def __init__(
        self,
        model_path: str,
        df_input: pd.DataFrame
    ):
        self.model_path = model_path
        self.df_input = df_input

    def run(self):
        
        # Load model
        logging.info("Loading sale prediction model")
        sale_prediction_model = joblib.load(self.model_path)

        # Predict
        logging.info("Predict monthly sales each shop")
        sale_prediction_output = sale_prediction_model.predict(self.df_input).clip(0, 20)

        return sale_prediction_output