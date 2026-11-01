class Car:
    def __init__ (self, color, engine_displacement, distance):
        self.color=color
        self.engine_displacement=engine_displacement
        self.distance= distance
    def reset_distance(self):
        self.distance=0
    def add_distance(self, km):
        self.distance+=km

car1= Car("red", 1.7, 50000)

car1.add_distance(100)
print(car1.distance)  # Output: 50100
car1.reset_distance()
print(car1.distance)  # Output: 0

car2= Car("blue", 2.0, 15000)
car2.add_distance(150)
print(car2.distance) 
car2.reset_distance()
print(car2.distance)  # Output: 0