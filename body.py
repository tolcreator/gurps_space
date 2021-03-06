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

    def ShowBasic(self):
        return self.GetSymbol() + " " + self.GetType()

    def ShowDetails(self):
        return ""

    def GetSymbol(self):
        return "."

    def GetType(self):
        return "Unknown"

    def GetIndent(self):
        if self.orbit:
            indent = self.orbit.GetOrbitee().GetIndent()
            if indent:
                return " |" + indent
            else:
                return " |"
        return ""

    def ShowUWP(self):
        return ""

    def __str__(self):
        indent = self.GetIndent()
        basic = indent + "_" + self.ShowBasic()
        ret = "%-28s " % basic
        ret = ret + "%-10s " % self.ShowUWP()
        ret = ret + self.ShowDetails()
        moonlets = 0
        for o in self.orbiters:
            c = o.GetOrbiter()
            if not c.GetType() == "Moonlet":
                ret = ret + "\n"
                ret = ret + o.__str__()
                ret = ret + " "
                ret = ret + c.__str__()
            else:
                moonlets = moonlets + 1
        if moonlets:
            basic = indent + " |" + "_. %d Moonlets" % moonlets
            ret = ret + "\n                 %-28s" % basic + \
            " Vacuum     ----       ----       ----       ----       ----       ----       ----       ----       ----       ----       ----       ----       ----       --  --  --"
        return ret
