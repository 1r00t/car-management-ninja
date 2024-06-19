from typing import Optional
from ninja import Schema


class BaseCar(Schema):
    make: str
    model: str
    year: int
    color: str
    price: float


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
