from django.shortcuts import get_object_or_404
from ninja import NinjaAPI
from ninja.pagination import paginate
from ninja.errors import ValidationError as NinjaValidationError
from django.core.exceptions import ValidationError

from api.models import Car
from api.schemas import CarIn, CarOut, CarPatch
from api.utils.throttling import throttle_view

api = NinjaAPI(version="1.0")


@api.post("/", response={201: CarOut})
@throttle_view
def create_car(request, payload: CarIn):
    car = Car.objects.create(**payload.dict())
    return car


@api.get("/", response=list[CarOut])
@paginate
@throttle_view
def get_cars(request):
    cars = Car.objects.all()
    return cars


@api.get("/{car_id}", response=CarOut)
@throttle_view
def get_car(request, car_id: int):
    car = get_object_or_404(Car, id=car_id)
    return car


@api.put("/{car_id}", response=CarOut)
@throttle_view
def update_car(request, car_id: int, payload: CarIn):
    car = get_object_or_404(Car, id=car_id)
    for attr, value in payload.dict().items():
        setattr(car, attr, value)
    car.save()
    return car


@api.patch("/{car_id}", response=CarOut)
@throttle_view
def patch_car(request, car_id: int, payload: CarPatch):
    car = get_object_or_404(Car, id=car_id)
    for attr, value in payload.dict(exclude_unset=True).items():
        setattr(car, attr, value)
    car.save()
    return car


@api.delete("/{car_id}")
@throttle_view
def delete_car(request, car_id: int):
    car = get_object_or_404(Car, id=car_id)
    car.delete()
    return {"success": True}
