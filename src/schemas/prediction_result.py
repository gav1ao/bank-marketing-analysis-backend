from pydantic import BaseModel


class PredictionResultSchema(BaseModel):
    will_accept_offer: bool