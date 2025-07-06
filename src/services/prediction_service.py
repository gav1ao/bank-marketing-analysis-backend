from src.schemas import BankClientSchema
from src.services.machine_learning.pipeline import Pipeline
from src.services.machine_learning.pre_processor import PreProcessor

PIPELINE_PATH = "machine_learning/pipelines/modelo_bancario_pipeline.pkl"


class PredictionService:

    def __init__(self):
        self.__pre_processor = PreProcessor()
        self.__pipeline = Pipeline()

        self.__model = self.__pipeline.load_pipeline(PIPELINE_PATH)

    def predict(self, bank_client: BankClientSchema) -> bool:
        X_Input = self.__pre_processor.prepare_data(bank_client)

        outcome = self.__model.predict(X_Input)[0]

        return outcome == 1