from animal import Animal



class Flyable:
    def fly(self):
        raise NotImplementedError



class Bird(Animal, Flyable):
    def speak(self):
        return "Tweet!"


    def fly(self):
        return "I am flying!"