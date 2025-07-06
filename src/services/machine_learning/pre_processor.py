import pandas as pd
from pandas import DataFrame

from src.schemas import BankClientSchema

FIELD_ALIASES = {
    "p_days": "pdays",
    "p_outcome": "poutcome"
}


class PreProcessor:
    def prepare_data(self, bank_client: BankClientSchema) -> DataFrame:
        """ Prepara os dados recebidos pela API para serem usados no modelo. """

        data_dict = {
            k: (v.value if hasattr(v, "value") else v)
            for k, v in bank_client.model_dump().items()
        }

        data_converted = {
            FIELD_ALIASES.get(k, k): v
            for k, v in data_dict.items()
        }

        return pd.DataFrame([data_converted])
