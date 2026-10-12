from abc import ABC, abstractmethod



class Animal(ABC):
    @abstractmethod
    def speak(self):
        raise NotImplementedError



class Dog(Animal):
    def speak(self):
        return "Woof!"



class Cat(Animal):
    def speak(self):
        return "Meow!"



def make_animals_speak(animals):
    for animal in animals:
        print(animal.speak())