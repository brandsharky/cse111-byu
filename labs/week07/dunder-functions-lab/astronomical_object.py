class AstronomicalObject:
    def __init__(self, name, type, distance_from_earth):
        self.name = name
        self.type = type
        self.distance_from_earth = distance_from_earth


    def __str__(self):
        return f"{self.name} is a {self.type} located {self.distance_from_earth} light-years away from Earth."


    def __repr__(self):
        return f"AstronomicalObject({self.name!r}, {self.type!r}, {self.distance_from_earth})"


    def __eq__(self, other):
        if not isinstance(other, AstronomicalObject):
            return False
        return self.name == other.name and self.type == other.type



class Planet(AstronomicalObject):
    def __init__(self, name, distance_from_earth, in_solar_system):
        super().__init__(name, "planet", distance_from_earth)
        self.in_solar_system = in_solar_system


    def __str__(self):
        if self.in_solar_system:
            location = "It is in our solar system."
        else:
            location = "It is outside of our solar system."
        return (f"{self.name} is a planet located {self.distance_from_earth} light-years away from Earth. {location}")


    def __repr__(self):
        return (f"Planet({self.name!r}, {self.distance_from_earth}, {self.in_solar_system})")



class Star(AstronomicalObject):
    def __init__(self, name, distance_from_earth, surface_temperature):
        super().__init__(name, "star", distance_from_earth)
        self.surface_temperature = surface_temperature


    def __str__(self):
        return (f"{self.name} is a star located "
                f"{self.distance_from_earth} light-years away from Earth. "
                f"It has a surface temperature of {self.surface_temperature} K.")


    def __repr__(self):
        return (f"Star({self.name!r}, {self.distance_from_earth}, "
                f"{self.surface_temperature})")









