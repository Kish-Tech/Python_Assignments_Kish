# Assignment 1: Design Your Own Class! 🏗️
# Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
# Add attributes and methods to bring the class to life!
# Use constructors to initialize each object with unique values.
# Add an inheritance layer to explore polymorphism or encapsulation.

# Base class (Superhero)
class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.__city = city  # Encapsulated attribute

    def use_power(self):
        print(f"{self.name} uses {self.power}!")

    def get_city(self):  # Encapsulated access method
        return self.__city

# Subclass (FlyingSuperhero inherits from Superhero)
class FlyingSuperhero(Superhero):
    def __init__(self, name, power, city, flight_speed):
        super().__init__(name, power, city)
        self.flight_speed = flight_speed

    def use_power(self):
        print(f"{self.name} flies at {self.flight_speed} km/h using {self.power}!")

# Create instances
hero1 = Superhero("ShadowStrike", "Invisibility", "Metroville")
hero2 = FlyingSuperhero("SkyBlaze", "Fire Wings", "SkyCity", 120)

# Use their methods
hero1.use_power()
print(f"{hero1.name} protects {hero1.get_city()}\n")

hero2.use_power()
print(f"{hero2.name} patrols {hero2.get_city()}")


# Activity 2: Polymorphism Challenge! 🎭

# Create a program that includes animals or vehicles with the same action (like move()). However, make each class define move() differently (for example, Car.move() prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️).

class Vehicle:
    def move(self):
        print("The vehicle moves...")

class Car(Vehicle):
    def move(self):
        print("🚗 The car drives on the road.")

class Plane(Vehicle):
    def move(self):
        print("✈️ The plane flies in the sky.")

class Boat(Vehicle):
    def move(self):
        print("🚤 The boat sails on water.")

# Test polymorphism
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()
