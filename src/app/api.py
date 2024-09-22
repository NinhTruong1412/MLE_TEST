from fastapi import APIRouter
from app import __version__
from app.helpers import path_root_service, sourcing_data
from app.schemas.health import Health
from app.config import settings
import app.config as config
from app.schemas.predict import SalePredictionOutput
from app.service.pre_processing import PreProcessInput
from app.service.sale_prediction import PredictSale
from app.service.post_processing import PostProcessOuput
import logging
logging.basicConfig(format="%(asctime)s %(levelname)s %(message)s", level=logging.INFO)

api_router = APIRouter()

data_folder = path_root_service / "app/data"
model_folder = path_root_service / "app/models"

@api_router.get("/health", response_model=Health, status_code=200)
def health() -> dict:
    """
    Root Get
    """
    health = Health(name=settings.PROJECT_NAME, api_version=__version__)

    return health.dict()

@api_router.post(
    "/predict/{shop_id}/{item_id}",
    response_model=SalePredictionOutput,
    status_code=200, 
)
async def booking_predict_async(
        shop_id: int,
        item_id: int,
    ) -> SalePredictionOutput:
    """
    Make sale prediction for next month
    """
    data_path = data_folder / config.DATA_FILE_NAME
    model_path = model_folder / config.MODEL_FILE_NAME

    dataframe = sourcing_data(data_path)
    # Preprocessing input
    logging.info(f"Preprocessing")
    df_input = PreProcessInput(
        shop_id = shop_id,
        item_id = item_id,
        df = dataframe
    ).run()

    # Predict sale
    logging.info(f"Predicting sales")
    prediction_output = PredictSale(
        model_path = model_path,
        df_input = df_input
    ).run()

    # Postprocessing output
    logging.info(f"Postprocessing")
    output = PostProcessOuput(
        prediction_output=prediction_output,
        shop_id=shop_id,
        item_id=item_id
    ).run()

    return output