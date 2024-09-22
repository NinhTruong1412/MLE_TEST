import pandas as pd
import logging
from app.helpers import (
    Constant as Const
)
from fastapi import HTTPException, status
logging.basicConfig(format="%(asctime)s %(levelname)s %(message)s", level=logging.INFO)


class PreProcessInput:
    def __init__(
        self,
        shop_id: int,
        item_id: int,
        df: pd.DataFrame
    ):
        self.shop_id = shop_id
        self.item_id = item_id
        self.df = df

    def convert_dtypes(self, columns):
        
        logging.info(f"Convert dtypes for list of columns: {columns}")
        self.df[columns] = self.df[columns].astype(Const.CATEGORY)

    def run(self):
        
        # convert dtypes
        logging.info(f"Convert dtypes")
        columns = [Const.SHOP_ID, Const.ITEM_ID, Const.MONTH, Const.ITEM_CATEGORY_ID]
        self.convert_dtypes(columns)

        # Get input
        logging.info(f"Get data by shop_id and item_id")
        df_input = self.df[(self.df[Const.SHOP_ID] == self.shop_id)&(self.df[Const.ITEM_ID] == self.item_id)]

        return df_input


