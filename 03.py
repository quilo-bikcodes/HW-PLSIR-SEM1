class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    def __init__(self,name, max_speed, mileage,model):
        super().__init__(name, max_speed, mileage)
        self.model= model

myBus = Bus("School",25,"30kmpl","volvo")
print(myBus.name,myBus.max_speed,myBus.model)