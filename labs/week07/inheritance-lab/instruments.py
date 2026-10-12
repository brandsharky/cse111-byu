class Instrument:
    valid_families = ["woodwind", "brass", "strings", "percussion"]

    def __init__(self, number, name, subtype, family):
        if family not in self.valid_families:
            raise ValueError(f"{family} is not a valid family. The options are: {Instrument.valid_families}")
        self.number = number
        self.name = name
        self.subtype = subtype
        self.family = family

    def play_sound(self):
        print(f"{self.name} played a sound")



class Percussion(Instrument):
    valid_subtypes = ["drum", "timpani", "auxilary", "mallet percussion", "keyboard"]

    def __init__(self, number, name, subtype):
        if subtype not in self.valid_subtypes:
            raise ValueError(f"{subtype} is not a valid subtype. The options are: {Percussion.valid_subtypes}")
        super().__init__(number, name, subtype, "percussion")



class Xylophone(Percussion):
    def __init__(self, number):
        super().__init__(number, "xylophone", "mallet percussion")

    def play_sound(self):
        print(f"{self.name} played 'Clink!'")