from pydantic import BaseModel


class SalePredictionOutput(BaseModel):
    shop_id: int
    item_id: int
    total_month_sale: float