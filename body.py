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
        self.orbiters.sort(key = lambda o: o.GetRadius())

    def GetOrbiters(self):
        return self.orbiters

    def Show(self):
        return self.GetType()

    def GetType(self):
        return "Unknown"

    def GetIndent(self):
        if self.orbit:
            indent = self.orbit.GetOrbitee().GetIndent()
            if indent:
                return "    " + indent
            else:
                return "   "
        return None

    def __str__(self):
        indent = self.GetIndent()
        if indent:
            ret = indent + self.Show()
        else:
            ret = self.Show()
        for o in self.orbiters:
            c = o.GetOrbiter()
            ret = ret + "\n"
            ret = ret + o.__str__()
            ret = ret + c.__str__()
        return ret
