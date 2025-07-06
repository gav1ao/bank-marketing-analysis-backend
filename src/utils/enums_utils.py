from enum import StrEnum
from typing import Type


def enum_to_dict_list(enum_cls: Type[StrEnum]) -> list[dict[str, str]]:
    return [{"key": member.name, "value": member.value} for member in enum_cls]
