from ninja import Schema
from ninja.errors import ValidationError
from pydantic import field_validator
from typing import Optional


# Base schema for Car with common attributes
class BaseCar(Schema):
    make: str
    model: str
    year: int
    color: str
    price: float

    @field_validator("year", mode="before")
    def year_must_be_greater_than_1886(cls, value):
        """
        Validator to ensure the car's year is not before 1886.
        """
        if int(value) < 1886:
            raise ValidationError("Cars were not invented yet!")
        return value


# Schema for creating a car, inherits from BaseCar
class CarIn(BaseCar):
    pass


# Schema for retrieving a car, includes an id attribute
class CarOut(BaseCar):
    id: int


# Schema for patching a car, all attributes are optional
class CarPatch(Schema):
    make: Optional[str] = None
    model: Optional[str] = None
    year: Optional[int] = None
    color: Optional[str] = None
    price: Optional[float] = None
