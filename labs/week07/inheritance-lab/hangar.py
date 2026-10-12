class Hangar:
    """Tracks drones that are stored at a hangar."""

    def __init__(self, name, drones=None):
        self.name = name
        if drones is None:
            self.drones = []
        else:
            self.drones = drones



    def __str__(self):
        return f"{self.name} has {len(self.drones)} drones"



    def add_drone(self, drone):
        self.drones.append(drone)



    def need_to_inspect(self):
        return [str(drone) for drone in self.drones if not drone.inspected]