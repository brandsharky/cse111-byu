class Drone:
    """Represents a drone that may or may not be inspected."""

    def __init__(self, name, drone_type):
        self.name = name
        self.drone_type = drone_type
        self.inspected = False

    def __str__(self):
        return f"{self.name} is a {self.drone_type} drone"

    def inspect(self):
        self.inspected = True



class SurveyDrone(Drone):
    def __init__(self, name):
        super().__init__(name, "survey")



class DeliveryDrone(Drone):
    def __init__(self, name):
        super().__init__(name, "delivery")



class RacingDrone(Drone):
    def __init__(self, name):
        super().__init__(name, "racing")