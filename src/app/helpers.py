from pathlib import Path
from jinja2 import Template
import pandas as pd

__all__ = ["path_root_service", "Constant", "generate_query"]

path_root_service = Path(__file__).parent.parent

class Constant:
    SHOP_ID = "shop_id"
    ITEM_ID = "item_id"
    TOTAL_MONTH_SALE = "total_month_sale"
    MONTH = "month"
    ITEM_CATEGORY_ID = "item_category_id"
    CATEGORY = "category"

def sourcing_data(input_file: Path) -> pd.DataFrame:
    """
    Read input file and replace placeholder using Jinja.

    Args:
        input_file (Path): input file to read
    Returns:
        DataFrame
    """
    return pd.read_parquet(input_file)