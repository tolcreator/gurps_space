import body
import dice
import math

def GetClimate(temp):
    if temp <= 244:
        return "Frozen"
    if temp <= 255:
        return "Very Cold"
    if temp <= 266:
        return "Cold"
    if temp <= 278:
        return "Chilly"
    if temp <= 289:
        return "Cool"
    if temp <= 300:
        return "Normal"
    if temp <= 311:
        return "Warm"
    if temp <= 322:
        return "Tropical"
    if temp <= 333:
        return "Hot"
    if temp <= 344:
        return "Very Hot"
    return "Infernal"

def GetGravity(density, diameter):
    return density * diameter

def ShowUWP(self):
    return "WTF"

def GetMass(density, diameter):
    return density * pow(diameter, 3)

def GenerateAxialTilt():
    r = dice.roll(3, 6)
    d = dice.roll(2, 6) - 2
    if r <= 6:
        return d
    if r <= 9:
        return 10 + d
    if r <= 12:
        return 20 + d
    if r <= 14:
        return 30 + d
    if r <= 16:
        return 40 + d
    r = dice.roll(1, 6)
    if r <= 2:
        return 50 + d
    if r <= 4:
        return 60 + d
    if r <= 5:
        return 70 + d
    return 80 + d

def GenerateSpecialRotationalPeriod(initial):
    r = dice.roll(3, 6)
    if r <= 6:
        return float(initial) / 24
    d = dice.roll(1, 6)
    if r <= 7:
        return d * 2
    if r <= 8:
        return d * 5
    if r <= 9:
        return d * 10
    if r <= 10:
        return d * 20
    if r <= 11:
        return d * 50
    return d * 100

def GenerateRotationalPeriod(mainType, subType, tidalEffect):
    mod = 0
    if mainType == "Gas Giant" and subType == "Small":
        mod = 6
    elif mainType == "Large":
        mod = 6
    elif mainType == "Standard":
        mod = 10
    elif mainType == "Small":
        mod = 14
    elif mainType == "Tiny":
        mod = 18
    mod = mod + int(tidalEffect)
    r = dice.roll(3, 6)
    if r >= 16:
        return GenerateSpecialRotationalPeriod(r + mod)
    if (r + mod) >= 36:
        return GenerateSpecialRotationalPeriod(r + mod)
    return float(r + mod) / 24

def Banner():
    return "   Orbit    Ecc  World Data                   %-10s %-10s %-10s %-10s %-10s %-10s %-10s %-10s %-10s %-10s %-10s %-10s %-10s %-10s %-10s %-3s %-3s %-3s Atmospheric Composition" % \
        ("UWP", "Atmosphere", "Hydro%", "Climate", "Avg Temp", \
         "Diameter", "Mass", "Density", "Gravity", "Pressure", \
         "Orbital", "Rotational", "Axial Tilt", \
         "Vulcanism", "Tectonics", "Hab", "Res", "Aff")

def PrettyPeriod(period):
    if period <= 2.0:
        return "%2.1f h" % (period * 24)
    if period <= 730.52:
        return "%2.1f d" % period
    return "%2.1f y" % (period / 365.26)

class World(body.Body):
    def __init__(self, mainType, parentStar):
        body.Body.__init__(self)
        self.mainType = mainType
        self.parentStar = parentStar
        self.diameter = 0
        self.mass = 0

    def GetParentStar(self):
        return self.parentStar

    def GetType(self):
        return self.mainType

    def GetDiameter(self):
        return self.diameter

    def GetMass(self):
        return self.mass

    def GenerateBasic(self):
        """ Do Nothing Yet """

    def GenerateDynamics(self):
        """ Do Nothing Yet """

    def GenerateDetails(self):
        """ Do Nothing Yet """
    
    def GetAffinity(self):
        return -10

    def GetResource(self):
        return -5

    def GetIsAMoon(self):
        return False

    def GetAtmosphericComposition(self):
        return ["None"]
