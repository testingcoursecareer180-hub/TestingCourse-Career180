
class Car:
    wheels = 4 #class variable
    def __init__(self, make, model, year,doors,engine):
        self.engine = engine
        self.make = make
        self.model = model
        self.year = year
        self.windows = 4 #instance variable
        self.transmission = 1 #instance variable
        self.fuel = 1 #instance variable
        self.brakes = 1 #instance variable
        self.steering = 1 #instance variable
        self.lights = 1 #instance variable
        self.horn = 1 #instance variable
        self.radio = 1 #instance variable

    def drive(self):
        print(f"Driving {self.make} {self.model} {self.year}")


#Creating objects
car_Toyota = Car("Toyota", "Corolla", 2020, 4 ,1)
car_Ford = Car("Ford", "Mustang", 2021, 2 ,0)
car_Nissan = Car("Nissan", "Altima", 2022, 4 ,2)

print(car_Toyota.engine)
print(car_Ford.engine)
print(car_Nissan.engine)
