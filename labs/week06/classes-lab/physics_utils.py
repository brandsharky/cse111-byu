class PhysicsUtils:
    @staticmethod
    def density(mass, volume):
        return mass / volume


    @staticmethod
    def kinetic_energy(mass, velocity):
        return 0.5 * mass * velocity**2