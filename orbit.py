import body

class Orbit:
    def __init__(self, orbitee, orbiter, radius, eccentricity, oType="Solar"):
        self.orbitee = orbitee
        self.orbiter = orbiter
        self.radius = radius
        self.eccentricity = eccentricity
        self.oType = oType

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
        if self.oType == "Solar":
            units = "AU"
        else:
            units = " D"
        return "% 8.3f %s ecc %0.2f" % (self.radius, units, self.eccentricity)
