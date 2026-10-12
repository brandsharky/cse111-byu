"""Create the Sky Lab Hangar scenario described in the lab writeup."""

# Import your classes and complete the launch-day script here.
from hangar import Hangar
from drone import *



hangar = Hangar("Sky Lab Hangar")

for name in ["Maple", "Atlas", "Scout", "Vantage"]:
    hangar.add_drone(SurveyDrone(name))

for name in ["Parcel-1", "Parcel-2"]:
    hangar.add_drone(DeliveryDrone(name))

for name in ["Comet", "Blaze", "Nitro", "Apex", "Drift"]:
    hangar.add_drone(RacingDrone(name))

for drone in hangar.drones:
    if drone.name in ["Maple", "Atlas", "Comet"]:
        drone.inspect()

print(hangar.need_to_inspect())