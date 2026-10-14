class Dragon:
    """
    Tracks the name, species, age, and whether the dragon has been fed today.
    User is able to feed the dragon, celebrate its birthday (which increases its age by 1), and print out a string representation of the dragon.
    >>> d1 = Dragon("Smaug", "Fire Dragon", 100)
    >>> d1.name
    'Smaug'
    >>> d1.species
    'Fire Dragon'
    >>> print(d1)
    Smaug is a 100-year-old Fire Dragon. They still need to be fed today.
    >>> d2 = Dragon("Smaug", "Fire Dragon", 100)
    >>> d1 == d2
    True
    >>> d1.feed()
    >>> d1 == d2
    False
    >>> d1.birthday()
    >>> print(d1)
    Smaug is a 101-year-old Fire Dragon. They have already been fed today.
    >>> repr(d1)
    "Dragon('Smaug', 'Fire Dragon', 101)"
    """
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
        self.fed_today = False


    def feed(self):
        self.fed_today = True


    def birthday(self):
        self.age += 1


    def __str__(self):
        feed_str = ''
        if self.fed_today:
            feed_str = "They have already been fed today."
        else:
            feed_str = "They still need to be fed today."
        return f'{self.name} is a {self.age}-year-old {self.species}. {feed_str}'


    def __repr__(self):
        return f"Dragon('{self.name}', '{self.species}', {self.age})"


    def __eq__(self, other):
        if not isinstance(other, Dragon):
            return False
        return self.name == other.name and self.species == other.species and self.age == other.age and self.fed_today == other.fed_today



class Zoo:
    """
    A Zoo optionally takes in an arbitrary amount of dragons and map of enclosures to list of dragons.
    The Zoo has methods to add and remove dragons, move dragons between enclosures, and feed all dragons.
    No duplicate enclosures should be added to the zoo.
    A dragon should not be added to more than one enclosure at a time.
    >>> toothless = Dragon("Toothless", "Night Fury", 22)
    >>> stormfly = Dragon("Stormfly", "Deadly Nadder", 7)
    >>> zoo = Zoo([toothless, stormfly], {"Enclosure 1": [toothless], "Enclosure 2": [stormfly]})
    >>> print(zoo)
    Zoo: {'Enclosure 1': [Dragon('Toothless', 'Night Fury', 22)], 'Enclosure 2': [Dragon('Stormfly', 'Deadly Nadder', 7)]}
    >>> zoo.add_enclosure("Enclosure 1")
    >>> print(zoo)
    Zoo: {'Enclosure 1': [Dragon('Toothless', 'Night Fury', 22)], 'Enclosure 2': [Dragon('Stormfly', 'Deadly Nadder', 7)]}
    >>> smaug = Dragon("Smaug", "Fire Dragon", 100)
    >>> zoo.add_dragon(smaug)
    >>> zoo.move_dragon(smaug, "Enclosure 1")
    >>> print(zoo)
    Zoo: {'Enclosure 1': [Dragon('Toothless', 'Night Fury', 22), Dragon('Smaug', 'Fire Dragon', 100)], 'Enclosure 2': [Dragon('Stormfly', 'Deadly Nadder', 7)]}
    >>> zoo.move_dragon(stormfly, "Enclosure 1")
    >>> print(zoo)
    Zoo: {'Enclosure 1': [Dragon('Toothless', 'Night Fury', 22), Dragon('Smaug', 'Fire Dragon', 100), Dragon('Stormfly', 'Deadly Nadder', 7)], 'Enclosure 2': []}
    >>> zoo.remove_dragon(toothless)
    >>> print(zoo)
    Zoo: {'Enclosure 1': [Dragon('Smaug', 'Fire Dragon', 100), Dragon('Stormfly', 'Deadly Nadder', 7)], 'Enclosure 2': []}
    """
    def __init__(self, dragons=None, enclosures=None):
        if dragons is None:
            self.dragons = []
        else:
            self.dragons = dragons

        # Enclosures should be formatted as enclosure_name: dragons_list
        if enclosures is None:
            self.enclosures = {}
        else:
            self.enclosures = enclosures


    def add_enclosure(self, name):
        if name not in self.enclosures.keys():
            self.enclosures[name] = []


    def add_dragon(self, dragon):
        self.dragons.append(dragon)


    def remove_dragon(self, dragon):
        for enclosure in self.enclosures:
            if dragon in self.enclosures[enclosure]:
                self.enclosures[enclosure].remove(dragon)
                break

        if dragon in self.dragons:
            self.dragons.remove(dragon)


    def move_dragon(self, dragon, new_enclosure):
        for enclosure in self.enclosures:
            if dragon in self.enclosures[enclosure]:
                self.enclosures[enclosure].remove(dragon)
                break
        self.enclosures[new_enclosure].append(dragon)


    def feed_all_dragons(self):
        for dragon in self.dragons:
            dragon.feed()


    def __str__(self):
        return f"Zoo: {self.enclosures}"