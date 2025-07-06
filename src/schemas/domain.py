from pydantic import BaseModel


class BankDomainSchema(BaseModel):
    job: list[dict[str, str]]
    marital: list[dict[str, str]]
    education: list[dict[str, str]]
    default: list[dict[str, str]]
    housing: list[dict[str, str]]
    loan: list[dict[str, str]]
    contact: list[dict[str, str]]
    month: list[dict[str, str]]
    p_outcome: list[dict[str, str]]
