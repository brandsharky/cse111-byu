class Mascot:
    max_events = 6



    def __init__(self, name, energy):
        self.name = name
        self.energy = energy
        self.cash = 0
        self.events = []


    def do_backflip(self):
        if self.energy >= 3:
            self.cash += 10
            self.energy -= 1
            print("Great backflip!")
        else:
            print("Too tired :(")


    def go_to_event(self, event_name):
        if len(self.events) < self.max_events:
            self.events.append(event_name)
            print(f"Went to: {event_name}")
        else:
            print("Been at too many events")


    def eat(self):
        self.energy += 10
        print("Gained 10 energy")