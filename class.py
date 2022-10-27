#day- 5:
#object oriented programming:

from car import Car

car_1 = Car("Chevy","Corvetter","2022","blue")
car_2 = Car("Ford","Mustang","2021","red")

Car.wheels = 2
print(car_1.wheels)
print(car_2.wheels)

print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.color)
print("\n")
"""
#inheritance
class Animal:
    alive = True

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")

class Rabbit(Animal):
    def run(self):
        print("This rabbit is running")


class Fish(Animal):
    def swim(self):
        print("This fish is swimming")

class Hawk(Animal):
    def fly(self):
        print("This hawk is flying")


rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)
fish.swim()
hawk.fly()
rabbit.run()
print("\n")
"""
#mutli-level inheritance
#when a derived (child) class inherits another derived class

class Organsim:
    alive = True

class Animal(Organsim):
    def eat(self):
        print("This animal is eating")

class Dog(Animal):
    def bark(self):
        print("This dog is barking")
dog = Dog()
print(dog.alive)
dog.eat()
dog.bark()
print("\n")

#multiple inhertance
# when a child class is derived from more than one parent class

class Prey:
    def flee(self):
        print("This animal flees")

class Predator:
    def hunt(self):
        print("This animal is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey,Predator):
    pass

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()
print("\n")

#method overriding
class Animal:
    def eat(self):
        print("this animal is eating")
class Rabbit(Animal):
    def eat(self):
        print("This bunny is eating a carrot")

bunny = Rabbit()
bunny.eat()
print("\n")

# method chaining:
# calling multiple methods sequentially
# each call performs an actions on the same objects and return self.

class Car:

    def turn_on(self):
        print("you start the engine")
        return self

    def drive(self):
        print("you drive the car")
        return self

    def brake(self):
        print("you step on the brakes")
        return self

    def turn_off(self):
        print("you turn off the engine")
        return self

car = Car()
#car.turn_on()
#car.drive()

#car.turn_on().drive()
#for method chaining
car.turn_on().drive().brake().turn_off()
print("\n")

# super()
# Function used to give access to the method of a parent class
# returns a temporary object of the parent class when used
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width


class Square(Rectangle):
    def __init__(self,length,width):
        super().__init__(length,width)

    def area(self):
        return self.length * self.width

class Cube(Rectangle):
    def __init__(self,length,width,height):
        super().__init__(length,width)
        self.height = height

    def volume(self):
        return self.length * self.width * self.height


square = Square(3,3)
cube = Cube(3,3,3)

print(square.area())
print(cube.volume())
print("\n")

#abstract class:
"""
# prevents a user from creating an object of that class
# compels a user to override abstract method in a child class
# abstract class- a class which contains one or more abstract methods
# abstract method - a method that has a declaration but does not have an implementation
"""

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def go(self):
        print("You drive the car")

    def stop(self):
        print("This car is stopped")

class Motorcycle(Vehicle):
    def go(self):
        print("You ride the motorcycle")
    def stop(self):
        print("This motocycle is stopped")

#vehicle = Vehicle()
car = Car()
motor = Motorcycle()
car.go()
motor.go()

car.stop()
motor.stop()