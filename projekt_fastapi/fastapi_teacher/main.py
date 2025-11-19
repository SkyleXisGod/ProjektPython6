from fastapi import FastAPI
from pydantic import BaseModel

class Car(BaseModel):
    brand: str
    model: str
    year: int

app = FastAPI()

cars = [
    {"id": 1, "brand": "Toyota", "model": "Corolla", "year": 2012},
    {"id": 2, "brand": "Ford", "model": "Focus", "year": 2018},
    {"id": 3, "brand": "Tesla", "model": "Model 3", "year": 2021},
    {"id": 4, "brand": "Volkswagen", "model": "Golf", "year": 2015},
    {"id": 5, "brand": "BMW", "model": "320i", "year": 2019}
]

@app.get("/")
def get_cars():
    return cars

@app.get("/cars/{car_id}")
def get_car(car_id: int):
    for car in cars:
        if car["id"] == car_id:
            return car

@app.post("/cars")
def create_car(car: Car):
    new_id = max([c["id"] for c in cars]) + 1 if cars else 1
    car_data = car.dict()
    car_data["id"] = new_id
    cars.append(car_data)
    return car_data

@app.put("/cars/{car_id}")
def update_car(car_id: int, car: Car):
    for index, existing_car in enumerate(cars):
        if existing_car["id"] == car_id:
          updated_car = car.dict()
          updated_car["id"] = car_id
          cars[index] = updated_car
          return updated_car

@app.delete("/cars/{car_id}")
def delete_car(car_id: int):
    for index, car in enumerate(cars):
        if car["id"] == car_id:
            removed_car = cars.pop(index)
            return removed_car