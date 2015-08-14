import dice
import world
import math

smallGasGiantSizeTable = [
    { "Mass":10, "Density":0.42 },
    { "Mass":15, "Density":0.26 },
    { "Mass":20, "Density":0.22 },
    { "Mass":30, "Density":0.19 },
    { "Mass":40, "Density":0.17 },
    { "Mass":50, "Density":0.17 },
    { "Mass":60, "Density":0.17 },
    { "Mass":70, "Density":0.17 },
    { "Mass":80, "Density":0.17 }
]

mediumGasGiantSizeTable = [
    { "Mass":100, "Density":0.18 },
    { "Mass":150, "Density":0.19 },
    { "Mass":200, "Density":0.20 },
    { "Mass":250, "Density":0.22 },
    { "Mass":300, "Density":0.24 },
    { "Mass":350, "Density":0.25 },
    { "Mass":400, "Density":0.26 },
    { "Mass":450, "Density":0.27 },
    { "Mass":500, "Density":0.29 }
]

largeGasGiantSizeTable = [
    { "Mass":600,  "Density":0.31 },
    { "Mass":800,  "Density":0.35 },
    { "Mass":1000, "Density":0.4  },
    { "Mass":1500, "Density":0.6  },
    { "Mass":2000, "Density":0.8  },
    { "Mass":2500, "Density":1.0  },
    { "Mass":3000, "Density":1.2  },
    { "Mass":3500, "Density":1.4  },
    { "Mass":4000, "Density":1.6  }
]

def GenerateGasGiantSubtype(mod):
    r = dice.roll(3, 6) + mod
    if r <= 10:
        return "Small"
    if r <= 16:
        return "Medium"
    return "Large"

def GenerateGasGiantSizeEntry():
    r = dice.roll(3, 6)
    if r <= 8:
        return 0
    elif r <= 10:
        return 1
    elif r <= 11:
        return 2
    elif r <= 12:
        return 3
    elif r <= 13:
        return 4
    elif r <= 14:
        return 5
    elif r <= 15:
        return 6
    elif r <= 16:
        return 7
    else:
        return 8

def GenerateGasGiantMassAndDensity(subType):
    if subType == "Small":
        table = smallGasGiantSizeTable
    elif subType == "Medium":
        table = mediumGasGiantSizeTable
    else:
        table = largeGasGiantSizeTable
    entry = GenerateGasGiantSizeEntry()
    r = dice.roll(3, 6) - 10
    if entry == 0:
        r = max(r, 0)
    if entry == 8:
        r = min(r, 0)
    if r == 0:
        return table[entry]
    if r < 0:
        high = table[entry]
        low = table[entry - 1]
    elif r > 0:
        high = table[entry + 1]
        low = table[entry]
    diff = high["Mass"] - low["Mass"]
    massStep = diff / 10
    massStep *= float(r) 
    diff = high["Density"] - low["Density"]
    denStep = diff / 10
    denStep *= float(r)
    mass = table[entry]["Mass"] + massStep
    density = table[entry]["Density"] + denStep

    """ Vary Density a little """
    r = dice.roll(3, 6) - 10
    var = float(r) / 10
    var = 1 + var
    density = density * var
    return { "Mass":mass, "Density":density }

class GasGiant(world.World):
    def __init__(self, parentStar):
        world.World.__init__(self, "Gas Giant", parentStar)
        self.numSulfurWorlds = 0
        self.numInnerMoons = 0

    def ShowUWP(self):
        if self.subType == "Small":
            return "SGG"
        if self.subType == "Medium":
            return "MGG"
        return "LGG"

    def GenerateBasic(self):
        mod = 0
        solarRadius = self.GetOrbit().GetRadius()
        if self.parentStar.GetIsInsideSnowLine(solarRadius):
            mod = 4
        elif self.parentStar.GetIsFirstOrbitBeyondSnowLine(solarRadius):
            mod = 4
        self.subType = GenerateGasGiantSubtype(mod)
        massAndDensity = GenerateGasGiantMassAndDensity(self.subType)
        self.mass = massAndDensity["Mass"]
        self.density = massAndDensity["Density"]
        self.diameter = pow(self.mass/self.density, 1.0/3.0)
        self.gravity = self.diameter * self.density 

    def GenerateDynamics(self):
        self.orbitalPeriod = math.sqrt(pow(self.orbit.GetRadius(), 3) / self.parentStar.GetMass()) * 365.26
        tide = (0.47 * self.parentStar.GetMass() * self.diameter) / pow(self.orbit.GetRadius(), 3)
        tidalEffect = (tide * self.parentStar.GetAge()) / self.mass
        if tidalEffect > 50:
            parentLock = True
            self.rotationalPeriod = self.orbitalPeriod
        else:
            self.rotationalPeriod = world.GenerateRotationalPeriod(self.mainType, self.subType, tidalEffect)
        if self.rotationalPeriod > self.orbitalPeriod:
            parentLock = True
            self.rotationalPeriod = self.orbitalPeriod
        self.axialTilt = world.GenerateAxialTilt()
        
    def ShowBasic(self):
        return self.GetSymbol() + " " + self.subType + " " + self.mainType

    def ShowDetails(self):
        return "----       ----       ----       ----      %- 10.3f %- 10.3f %- 10.3f %- 10.3f  ----       %-10s %-10s %- 10d ----       ----       --  --  --" % \
            (self.diameter, self.mass, self.density, self.gravity, world.PrettyPeriod(self.orbitalPeriod), world.PrettyPeriod(self.rotationalPeriod), self.axialTilt)

    def GetNumSulfurWorlds(self):
        return self.numSulfurWorlds

    def IncNumSulfurWorlds(self):
        self.numSulfurWorlds = self.numSulfurWorlds + 1

    def SetNumInnerMoons(self, n):
        self.numInnerMoons = n

    def GetSymbol(self):
        return "O"

    def GetAffinity(self):
        return -10

    def GetResource(self):
        return -5
