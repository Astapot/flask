import pydantic
from typing import Optional, Type

from errors import HttpError


class CreateAdv(pydantic.BaseModel):
    header: str
    description: str
    owner: str

    @pydantic.field_validator('header')
    @classmethod
    def header_length(cls, text: str) -> str:
        if len(text) > 100:
            raise ValueError('нельзя больше 100 символов')
        return text


class UpdateAdv(pydantic.BaseModel):
    header: Optional[str] = None
    description: Optional[str] = None
    owner: Optional[str] = None

    @pydantic.field_validator('header')
    @classmethod
    def header_length(cls, text: str) -> str:
        if len(text) > 100:
            raise ValueError('нельзя больше 100 символов')
        return text


VALIDATOR_CLASS = Type[CreateAdv | UpdateAdv]
VALIDATOR = CreateAdv | UpdateAdv


def validate(validation_clas: VALIDATOR_CLASS, json_data: dict | list):
    try:
        return validation_clas(**json_data).model_dump(exclude_unset=True) # если ввести функцию dict, ide ее зачеркивает и говорит, что она устарела
    except pydantic.ValidationError as er:
        error = er.errors()[0]
        error.pop('ctx', None)
        raise HttpError(400, error)


