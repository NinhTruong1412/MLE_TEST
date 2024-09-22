import logging
from app.helpers import (
    Constant as Const
)

logging.basicConfig(format="%(asctime)s %(levelname)s %(message)s", level=logging.INFO)


class PostProcessOuput:
    def __init__(
        self,
        prediction_output: list,
        shop_id: int,
        item_id: int
    ):
        self.prediction_output = prediction_output
        self.shop_id = shop_id
        self.item_id = item_id

    def run(self):
        
        # if there is no predicted result return 0
        total_month_sale = 0 if len(self.prediction_output) == 0 else self.prediction_output[0]
        
        return {
            Const.SHOP_ID : self.shop_id,
            Const.ITEM_ID : self.item_id,
            Const.TOTAL_MONTH_SALE : total_month_sale
        }