from enum import StrEnum


class JobEnum(StrEnum):
    ADMIN = "admin"
    UNKNOWN = "unknown"
    UNEMPLOYED = "unemployed"
    MANAGEMENT = "management"
    HOUSEMAID = "housemaid"
    ENTREPRENEUR = "entrepreneur"
    STUDENT = "student"
    BLUE_COLLAR = "blue-collar"
    SELF_EMPLOYED = "self-employed"
    RETIRED = "retired"
    TECHNICIAN = "technician"
    SERVICES = "services"


class MaritalEnum(StrEnum):
    MARRIED = "married"
    DIVORCED = "divorced"
    SINGLE = "single"


class EducationEnum(StrEnum):
    UNKNOWN = "unknown"
    SECONDARY = "secondary"
    PRIMARY = "primary"
    TERTIARY = "tertiary"


class YesNoEnum(StrEnum):
    YES = "yes"
    NO = "no"


class ContactEnum(StrEnum):
    UNKNOWN = "unknown"
    TELEPHONE = "telephone"
    CELLULAR = "cellular"


class MonthEnum(StrEnum):
    JAN = "jan"
    FEB = "feb"
    MAR = "mar"
    APR = "apr"
    MAY = "may"
    JUN = "jun"
    JUL = "jul"
    AUG = "aug"
    SEP = "sep"
    OCT = "oct"
    NOV = "nov"
    DEC = "dec"


class PreviousOutcomeEnum(StrEnum):
    UNKNOWN = "unknown"
    OTHER = "other"
    FAILURE = "failure"
    SUCCESS = "success"
