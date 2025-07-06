from src.schemas import BankDomainSchema, JobEnum, MaritalEnum, EducationEnum, YesNoEnum, ContactEnum, MonthEnum, \
    PreviousOutcomeEnum
from src.utils.enums_utils import enum_to_dict_list


class BankDomainService:

    def get_domain(self) -> BankDomainSchema:
        return BankDomainSchema(
            job=enum_to_dict_list(JobEnum),
            marital=enum_to_dict_list(MaritalEnum),
            education=enum_to_dict_list(EducationEnum),
            default=enum_to_dict_list(YesNoEnum),
            housing=enum_to_dict_list(YesNoEnum),
            loan=enum_to_dict_list(YesNoEnum),
            contact=enum_to_dict_list(ContactEnum),
            month=enum_to_dict_list(MonthEnum),
            p_outcome=enum_to_dict_list(PreviousOutcomeEnum)
        )
