import orbit

class Body:
    def __init__(self):
        self.orbiters = []
        self.orbit = None

    def SetOrbit(self, orbit):
        """ should probably check that orbit.orbiter = self """
        self.orbit = orbit

    def GetOrbit(self):
        return self.orbit

    def AddOrbiter(self, orbit):
        """ should probably check that orbit.orbitee = self """
        self.orbiters.append(orbit)

    def GetOrbiters(self):
        return self.orbiters
