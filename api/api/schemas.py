from typing import Optional
from ninja import Schema
from pydantic import field_validator
from ninja.errors import ValidationError


class BaseCar(Schema):
    make: str
    model: str
    year: int
    color: str
    price: float

    @field_validator("year", mode="before")
    def year_must_be_greater_than_1886(cls, value):
        if int(value) < 1886:
            raise ValidationError("Cars were not invented yet!")
        return value


class CarIn(BaseCar):
    pass


class CarOut(BaseCar):
    id: int


class CarPatch(Schema):
    make: Optional[str] = None
    model: Optional[str] = None
    year: Optional[int] = None
    color: Optional[str] = None
    price: Optional[float] = None
