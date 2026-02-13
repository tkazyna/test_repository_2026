#1
"""
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"

class Dog(Animal):
    def speak(self):  # override
        return f"{self.name} barks"
s=input("Enter name of dog: ")
my_dog = Dog(s)
my_dog2=Animal("s")
print(my_dog2.speak())
print(my_dog.speak())
"""
#2
"""
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_salary(self):
        return self.salary

    def display_info(self):
        return f"Employee: {self.name}, Salary: {self.salary} tg"
class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def get_salary(self):
        total = super().get_salary() + self.bonus
        return total

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Bonus: {self.bonus}, Total Salary: {self.get_salary()} tg"
print("Enter data for a regular employee:")
emp_name = input("Name: ")
emp_salary = int(input("Salary: "))
emp = Employee(emp_name, emp_salary)

print("\nEnter data for a manager:")
mgr_name = input("Name: ")
mgr_salary = int(input("Salary: "))
mgr_bonus = int(input("Bonus: "))

mgr = Manager(mgr_name, mgr_salary, mgr_bonus)


print("\nEmployee Info:")
print(emp.display_info())

print("\nManager Info:")
print(mgr.display_info())

Enter data for a regular employee:
Name: Alice
Salary: 50000

Enter data for a manager:
Name: Bob
Salary: 70000
Bonus: 15000

"""
#3
"""
class Flyer:
    def fly(self):
        return "I can fly"

class Swimmer:
    def swim(self):
        return "I can swim"

class Duck(Flyer, Swimmer): 
    pass

# Test
donald = Duck()
print(donald.fly())
print(donald.swim())
"""
#4
"""
class Vehicle:
    def __init__(self, brand, model, speed):
        self.brand = brand
        self.model = model
        self.speed = speed

    def display_info(self):
        return f"Vehicle: {self.brand} {self.model}, Max speed: {self.speed} km/h"

class ElectricVehicle(Vehicle):
    def __init__(self, brand, model, speed, battery_capacity):
        super().__init__(brand, model, speed)
        self.battery_capacity = battery_capacity

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Battery: {self.battery_capacity} kWh"

# --- User input ---
print("Enter data for a regular vehicle:")
v_brand = input("Brand: ")
v_model = input("Model: ")
v_speed = int(input("Max speed (km/h): "))
vehicle = Vehicle(v_brand, v_model, v_speed)

print("\nEnter data for an electric vehicle:")
ev_brand = input("Brand: ")
ev_model = input("Model: ")
ev_speed = int(input("Max speed (km/h): "))
ev_battery = int(input("Battery capacity (kWh): "))
electric_vehicle = ElectricVehicle(ev_brand, ev_model, ev_speed, ev_battery)

# --- Display ---
print("\n--- Vehicle Info ---")
print(vehicle.display_info())

print("\n--- Electric Vehicle Info ---")
print(electric_vehicle.display_info())
"""



