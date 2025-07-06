from pydantic import Field, BaseModel

from src.schemas import JobEnum, MaritalEnum, EducationEnum, YesNoEnum, ContactEnum, MonthEnum, PreviousOutcomeEnum


class BankClientSchema(BaseModel):
    age: int = Field(...)
    job: JobEnum
    marital: MaritalEnum
    education: EducationEnum
    default: YesNoEnum
    balance: float
    housing: YesNoEnum
    loan: YesNoEnum
    contact: ContactEnum
    day: int = Field(..., ge=1, le=31)
    month: MonthEnum
    duration: int = Field(..., ge=0)
    campaign: int = Field(..., ge=0)
    p_days: int
    previous: int = Field(..., ge=0)
    p_outcome: PreviousOutcomeEnum
