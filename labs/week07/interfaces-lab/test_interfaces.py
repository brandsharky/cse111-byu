import math
import pytest
from byu_pytest_utils import with_import

# Q1: Basic Interface
@with_import("animal", "Dog")
def test_q1_dog_speak(Dog):
    dog = Dog()
    assert "Woof!" in dog.speak()

@with_import("animal", "Cat")
def test_q1_cat_speak(Cat):
    cat = Cat()
    assert "Meow!" in cat.speak()

# Q2: Abstract Base Class
@with_import("shape", "Circle")
def test_q2_circle_area(Circle):
    c = Circle(2)
    assert math.isclose(c.area(), math.pi * 4)

@with_import("shape", "Square")
def test_q2_square_area(Square):
    s = Square(3)
    assert s.area() == 9

# Q3: Interface Usage
@with_import("shape", "print_area")
@with_import("shape", "Square")
@with_import("shape", "Circle")
def test_q3_print_area(Circle, Square, print_area, capsys):
    c = Circle(1)
    s = Square(2)
    print_area(c)
    print_area(s)
    out = capsys.readouterr().out
    assert str(c.area()) in out
    assert str(s.area()) in out

# Q4: Multiple Interfaces
@with_import("flyable", "Bird")
def test_q4_bird_speak_and_fly(Bird):
    b = Bird()
    assert "Tweet!" in b.speak()
    assert "I am flying!" in b.fly()

# Q5: Interface Enforcement
@with_import("animal", "Animal")
def test_q5_animal_instantiation_error(Animal):
    with pytest.raises(TypeError):
        Animal()

# Q6: Polymorphism
@with_import("animal", "make_animals_speak")
@with_import("flyable", "Bird")
@with_import("animal", "Cat")
@with_import("animal", "Dog")
def test_q6_make_animals_speak(Dog, Cat, Bird, make_animals_speak, capsys):
    animals = [Dog(), Cat(), Bird()]
    make_animals_speak(animals)
    out = capsys.readouterr().out
    assert "Woof!" in out
    assert "Meow!" in out
    assert "Tweet!" in out

# Q7: Interface in Practice
@with_import("vehicle", "Car")
def test_q7_car_drive(Car):
    car = Car()
    assert "Driving a car!" in car.drive()

@with_import("vehicle", "Bicycle")
def test_q7_bicycle_drive(Bicycle):
    bike = Bicycle()
    assert "Riding a bicycle!" in bike.drive()
