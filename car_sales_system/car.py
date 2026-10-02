from database import DatabaseConnection

class Car:
    def __init__(self,car_id,brand,model,price,available_quantity):
        self.car_id=car_id
        self.brand=brand
        self.model=model
        self.price=price
        self.available_quantity=available_quantity
car = Car(1, "Toyota", "Fortuner", 3500000, 5)
class CarSalesSystem:
    def __init__(self):
        self.db = DatabaseConnection()