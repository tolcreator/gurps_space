import body

class Orbit:
    def __init__(self, orbitee, orbiter, radius, eccentricity):
        self.orbitee = orbitee
        self.orbiter = orbiter
        self.radius = radius
        self.eccentricity = eccentricity

    def GetRadius(self):
        return self.radius

    def GetEccentricity(self):
        return self.eccentricity

    def GetOrbitee(self):
        return self.orbitee

    def GetOrbiter(self):
        return self.orbiter

    def GetMinSeparation(self):
        return (1 - self.eccentricity) * self.radius

    def GetMaxSeparation(self):
        return (1 + self.eccentricity) * self.radius

    def __str__(self):
        return "%0.2f AU ecc %0.2f" % (self.radius, self.eccentricity)
