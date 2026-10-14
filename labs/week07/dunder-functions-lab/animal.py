class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species


    def __str__(self):
        return f"{self.name} is a {self.species}"


    def __repr__(self):
        return f"Animal({self.name!r}, {self.species!r})"


    def __eq__(self, other):
        if not isinstance(other, Animal):
            return False
        return self.name == other.name and self.species == other.species


    def make_sound(self):
        pass



class Lion(Animal):
    def __init__(self, name):
        super().__init__(name, "lion")


    def __str__(self):
        return f"{self.name} is a lion"


    def __repr__(self):
        return f"Lion({self.name!r})"


    def __eq__(self, other):
        if not isinstance(other, Lion):
            return False
        return self.name == other.name


    def make_sound(self):
        return "Roar"