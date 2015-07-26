import body
import dice
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

def GetWorldSubtype(mainType, blackBodyTemperature):
    if mainType == "Tiny":
        if blackBodyTemperature <= 140:
            return "Ice"        #May turn out to be Sulfur later
        return "Rock"
    if mainType == "Small":
        if blackBodyTemperature <= 80:
            return "Hadean"
        if blackBodyTemperature <= 140:
            return "Ice"
        return "Rock"
    if mainType == "Standard" or mainType == "Large":
        if blackBodyTemperature <= 80:
            return "Hadean"
        if blackBodyTemperature <= 150:
            return "Ice"    
        if blackBodyTemperature <= 230:
            return "Ammonia"    #May turn out to be Ice later
        if blackBodyTemperature <= 240:
            return "Ice"
        if blackBodyTemperature <= 320:
            return "Ocean"      #May turn out to be Garden later
        if blackBodyTemperature <= 500:
            return "Greenhouse"
        return "Chthonian"
    return "N/a"

def GenerateAtmosphericMass(mainType, subType):
    if mainType == "Small" and subType == "Ice":
        disqualified = False
    elif mainType == "Standard":
        if subType == "Hadean" or subType == "Chthonian":
            disqualified = True
        else:
            disqualified = False
    elif mainType == "Large":
        if subType == "Chthonian":
            disqualified = True
        else:
            disqualified = False
    else:
        disqualified = True
    if disqualified:
        return 0.0

    r = dice.roll(3, 6)
    mass = float(r) / 10
    r = dice.roll(1, 20) - 10
    var = float(r) / 200
    return mass + var    

def GenerateHydrosphere(mainType, subType):
    hydro = 0
    if mainType == "Small" and subType == "Ice":
        hydro = (dice.roll(1, 6) + 2) * 10
    if mainType == "Standard" or mainType == "Large":
        if subType == "Ammonia":
            hydro = (dice.roll(2, 6)) * 10
        if subType == "Ice":
            hydro = (dice.roll(2, 6) - 10) * 10
        if subType == "Ocean" or subType == "Garden":
            if mainType == "Standard":
                var = 4
            else:
                var = 6
            hydro = (dice.roll(1, 6) + var) * 10
        if subType == "Greenhouse":
            hydro = (dice.roll(2, 6) - 7) * 10
    if hydro > 0:
        r = dice.roll(1, 10) - 5
        hydro = hydro + r
        return min(hydro, 100)
    return 0

def GetBlackBodyCorrection(mainType, subType, hydrosphere, atmosphericMass):
    if mainType == "Belt" or mainType == "Moonlet":
        AF = 0.97
        GF = 0.0
    elif mainType == "Tiny":
        if subType == "Ice":
            AF = 0.86
            GF = 0.0
        elif subType == "Sulfur":
            AF = 0.77
            GF = 0.0
        else: #Rock
            AF = 0.97
            GF = 0.00
    elif mainType == "Small":
        if subType == "Hadean":
            AF = 0.67
            GF = 0.0
        elif subType == "Ice":
            AF = 0.93
            GF = 0.10
        else: #Rock
            AF = 0.96
            GF = 0.0
    elif mainType == "Standard" or mainType == "Large":
        if subType == "Ammonia":
            AF = 0.84
            GF = 0.20
        elif subType == "Ice":
            AF = 0.86
            GF = 0.20
        elif subType == "Ocean" or subType == "Garden":
            GF = 0.16
            if hydrosphere >= 20:
                AF = 0.95
            elif hydrosphere >= 50:
                AF = 0.92
            elif hydrosphere >= 90:
                AF = 0.88
            else:
                AF = 0.84
        elif subType == "Greenhouse":
            AF = 0.77
            GF = 2.0
        else: #Chthonian
            AF = 0.97
            GF = 0.0
    else:
        return 1.0
    return AF * (1 + (atmosphericMass * GF))

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

def GetInitialLargeIronCoreDensity(r):
    if r <= 6:
        return 0.8
    if r <= 10:
        return 0.9
    if r <= 14:
        return 1.0
    if r <= 17:
        return 1.1
    return 1.2

def GetInitialSmallIronCoreDensity(r):
    if r <= 6:
        return 0.6
    if r <= 10:
        return 0.7
    if r <= 14:
        return 0.8
    if r <= 17:
        return 0.9
    return 1.0

def GetInitialIcyCoreDensity(r):
    if r <= 6:
        return 0.3
    if r <= 10:
        return 0.4
    if r <= 14:
        return 0.5
    if r <= 17:
        return 0.6
    return 0.7

def GenerateDensity(mainType, subType):
    core = "Large"
    if mainType == "Tiny":
        if subType == "Ice" or subType == "Sulfur":
            core = "Icy"
        else:
            core = "Small"
    elif mainType == "Small":
        if subType == "Ice" or subType == "Hadean":
            core = "Icy"
        else:
            core = "Small"
    elif mainType == "Standard":
        if subType == "Hadean" or subType == "Ammonia":
            core = "Icy"
    elif mainType == "Large":
        if subType == "Ammonia":
            core == "Icy"

    r = dice.roll(3, 6)
    if core == "Large":
        initial = GetInitialLargeIronCoreDensity(r)
    elif core == "Small":
        initial = GetInitialSmallIronCoreDensity(r)
    else:
        initial = GetInitialIcyCoreDensity(r)
    r = dice.roll(1, 20) - 10
    var = float(r) / 200
    return initial + var   

def GenerateDiameter(mainType, blackBodyTemperature, density): 
    if mainType == "Large":
        minimum = 0.065
        maximum = 0.091
    elif mainType == "Standard":
        minimum = 0.030
        maximum = 0.065
    elif mainType == "Small":
        minimum = 0.024
        maximum = 0.030
    else:
        minimum = 0.004
        maximum = 0.024

    var = math.sqrt(blackBodyTemperature / density)
    myMin = minimum * var
    myMax = maximum * var
    step = (myMax - myMin) / 10

    r = dice.roll(2, 6) - 2
    step =  step * float(r)

    r = dice.roll(1, 20) - 10
    var = float(r) / 200
    step = step * (1.0 + var)

    return myMin + step

def GetGravity(density, diameter):
    return density * diameter

def GetWorldMass(density, diameter):
    return density * pow(diameter, 3)

def GetAtmosphericPressure(mainType, subType, atmosphericMass, gravity):
    """ No Atmosphere """
    if mainType == "Tiny":
        return 0.0
    if mainType == "Small" and subType == "Hadean":
        return 0.0
    """ Trace Atmosphere """
    """ Gurps gives no means to work this out. """
    """ Just says it's less than 0.01 """
    if mainType == "Small" and subType == "Rock":
        r = dice.roll(1, 100) - 1
        return float(r) / 10000
    if mainType == "Standard" and subType == "Chthonian":
        r = dice.roll(1, 100) - 1
        return float(r) / 10000
    if mainType == "Large" and subType == "Chthonian":
        r = dice.roll(1, 100) - 1
        return float(r) / 10000

    if mainType == "Small" and subType == "Ice":
        PF = 10
    if mainType == "Standard":
        if subType == "Greenhouse":
            PF = 100
        else:
            PF = 1
    if mainType == "Large":
        if subType == "Greenhouse":
            PF = 500
        else:
            PF = 5
    
    return PF * atmosphericMass * gravity

def GetAtmosphericCategory(pressure):
    if pressure == 0.0:
        return "Vacuum"
    if pressure <= 0.01:
        return "Trace"
    if pressure <= 0.5:
        return "Very Thin"
    if pressure <= 0.8:
        return "Thin"
    if pressure <= 1.2:
        return "Standard"
    if pressure <= 1.5:
        return "Dense"
    if pressure <= 10.0:
        return "Very Dense"
    return "Superdense"

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
    return "                                                  %-10s %-10s %-10s %-10s %-10s %-10s %-10s %-10s %-10s %-10s %-10s" % \
        ("Atmosphere", "Hydro%", "Climate", "Avg Temp", "Diameter", "Mass", "Density", "Gravity", "Pressure", "Orbital", "Rotational")

class World(body.Body):
    def __init__(self, mainType, parentStar):
        body.Body.__init__(self)
        self.mainType = mainType
        self.parentStar = parentStar
        self.diameter = 0
        self.mass = 0

    def GetType(self):
        return self.mainType

    def GetDiameter(self):
        return self.diameter

    def GetMass(self):
        return self.mass

def PrettyPeriod(period):
    if period <= 2.0:
        return "%2.1f h" % (period * 24)
    if period <= 730.52:
        return "%2.1f d" % period
    return "%2.1f y" % (period / 365.26)

class TerrestrialWorld(World):
    def __init__(self, mainType, parentStar, parentWorld = None):
        World.__init__(self, mainType, parentStar)
        self.parentWorld = parentWorld

    def ShowBasic(self):
        return self.GetSymbol() + " " + self.mainType + " " + self.subType

    def ShowDetails(self):
        return "%-10s %-10d %-10s %-10d%- 10.3f %- 10.3f %- 10.3f %- 10.3f %- 10.3f  %-10s %-10s" % \
            (self.atmosphericCategory, self.hydrosphere, self.climate, self.averageTemperature, \
             self.diameter, self.mass, self.density, self.gravity, self.atmosphericPressure, \
             PrettyPeriod(self.orbitalPeriod), PrettyPeriod(self.rotationalPeriod))

    def GenerateBasic(self):
        if self.parentWorld:
            solarRadius = self.parentWorld.GetOrbit().GetRadius()
        else:
            solarRadius = self.GetOrbit().GetRadius()
        blackBodyTemperature = 278 * ( pow(self.parentStar.GetLuminosity(), 0.25) / pow(solarRadius, 0.5) )
        self.subType = GetWorldSubtype(self.mainType, blackBodyTemperature)

        """ Corrections """
        """ Fix Ammonia worlds now """
        if self.subType == "Ammonia" and self.parentStar.GetMass() > 0.65:
            self.subType = "Ice"
        """ Find Sulfur World now """
        if self.mainType == "Tiny" and self.subType == "Ice" and self.parentWorld and self.parentWorld.GetType() == "Gas Giant" and self.parentWorld.GetNumSulfurWorlds() == 0:
            r = dice.roll(1, 6)
            if r <= 3:
                self.subType = "Sulfur"
                self.parentWorld.IncNumSulfurWorlds()

        """ Find Garden World Now """
        """ TODO: Use First In method """
        if self.mainType == "Standard" and self.subType == "Ocean":
            r = dice.roll(3, 6)
            mod = int(self.parentStar.GetAge() / 0.5)
            mod = max(mod, 10)
            r = r + mod
            if r > 18:
                self.subType = "Garden"
        if self.mainType == "Large" and self.subType == "Ocean":
            r = dice.roll(3, 6)
            mod = int(self.parentStar.GetAge() / 0.5)
            mod = max(mod, 5)
            r = r + mod
            if r > 18:
                self.subType = "Garden"
     
        self.density = GenerateDensity(self.mainType, self.subType)
        if blackBodyTemperature < 3.0:
            """ Damn White Dwarves """
            """ TODO: Maybe use the III temperature instead """
            originalBlackBodyTemperature = 278 * ( pow(self.parentStar.GetInitialLuminosity(), 0.25) / pow(solarRadius, 0.5) )
            self.diameter = GenerateDiameter(self.mainType, originalBlackBodyTemperature, self.density)
        else:     
            self.diameter = GenerateDiameter(self.mainType, blackBodyTemperature, self.density)
        self.gravity = GetGravity(self.density, self.diameter)
        self.mass = GetWorldMass(self.density, self.diameter)
         
        atmosphericMass = GenerateAtmosphericMass(self.mainType, self.subType)
        self.hydrosphere = GenerateHydrosphere(self.mainType, self.subType)
        blackBodyCorrection = GetBlackBodyCorrection(self.mainType, self.subType, self.hydrosphere, atmosphericMass)
        self.averageTemperature = blackBodyTemperature * blackBodyCorrection
        self.climate = GetClimate(self.averageTemperature)
        self.atmosphericPressure = GetAtmosphericPressure(self.mainType, self.subType, atmosphericMass, self.gravity)
        self.atmosphericCategory = GetAtmosphericCategory(self.atmosphericPressure)

    def GenerateDynamics(self):
        """ Orbital period in days """
        parentLock = False
        lunarLock = False
        possibleLunarLock = False
        potentialRotationalPeriod = 0
        if self.parentWorld:
            self.orbitalPeriod = math.sqrt(pow(self.orbit.GetRadius(), 3) / self.parentWorld.GetMass()) * 0.0588
            tide = (17800000 * self.parentWorld.GetMass() * self.diameter) / pow(self.orbit.GetRadius(), 3)
            if tide > 50:
                parentLock = True
        else:
            self.orbitalPeriod = math.sqrt(pow(self.orbit.GetRadius(), 3) / self.parentStar.GetMass()) * 365.26
            tide = (0.47 * self.parentStar.GetMass() * self.diameter) / pow(self.orbit.GetRadius(), 3)
            for o in self.orbiters:
                m = o.GetOrbiter()
                if not m.GetType() == "Moonlet":
                    if not possibleLunarLock:            
                        possibleLunarLock = True
                        potentialRotationalPeriod = math.sqrt(pow(o.GetRadius(), 3) / self.GetMass()) * 0.0588
                    tide = tide + (17800000 * m.GetMass() * self.diameter) / pow(o.GetRadius(), 3)
        tidalEffect = (tide * self.parentStar.GetAge()) / self.mass
        if tidalEffect > 50:
            if possibleLunarLock:
                lunarLock = True
                self.rotationalPeriod = potentialRotationalPeriod
            else:
                parentLock = True
                self.rotationalPeriod = self.orbitalPeriod
                if not self.parentWorld:
                    self.SolarLockCorrection()
        else:
            self.rotationalPeriod = GenerateRotationalPeriod(self.mainType, None, tidalEffect)
        if possibleLunarLock and self.rotationalPeriod > potentialRotationalPeriod:
            lunarLock = True
            self.rotationalPeriod = self.orbitalPeriod
        elif self.rotationalPeriod > self.orbitalPeriod:
            parentLock = True
            self.rotationalPeriod = self.orbitalPeriod
            if not self.parentWorld:
                self.SolarLockCorrection()

    def SolarLockCorrection(self):
        DF = 1.0
        NF = 1.0
        p = self.atmosphericPressure
        if self.atmosphericCategory == "None" or self.atmosphericCategory == "Trace":
            self.atmosphericCategory = "None"
            self.hydrosphere = 0
            DF = 1.2
            NF = 0.1
            self.atmosphericPressure = 0.0
        elif self.atmosphericCategory == "Very Thin":
            self.atmosphericCategory = "Trace"
            self.hydrosphere = 0
            DF = 1.2
            NF = 0.1
            p = p - 0.01
            p = p / 49
            self.atmosphericPressure = p
            if self.subType == "Ocean" or self.subType == "Garden":
                self.subType = "Chthonian"
        elif self.atmosphericCategory == "Thin":
            self.atmosphericCategory = "Very Thin"
            self.hydrosphere = max(self.hydrosphere - 50, 0)
            DF = 1.16
            NF = 0.67
            p = p - 0.5
            p = p * (49/30)
            p = p + 0.01
            self.atmosphericPressure = p
        elif self.atmosphericCategory == "Standard":
            self.atmosphericCategory = "Thin"
            self.hydrosphere = max(self.hydrosphere - 25, 0)
            DF = 1.12
            NF = 0.8
            p = p - 0.8
            p = p * 0.75
            p = p + 0.5
            self.atmosphericPressure = p
        elif self.atmosphericCategory == "Dense":
            self.hydrosphere = max(self.hydrosphere - 10, 0)
            DF = 1.09
            NF = 0.88
        elif self.atmosphericCategory == "Very Dense":
            DF = 1.05
            NF = 0.95
        self.avTempDayFace = self.averageTemperature * DF
        self.avTempNightFace = self.averageTemperature * NF
        self.dayFaceClimate = GetClimate(self.avTempDayFace)
        self.nightFaceClimate = GetClimate(self.avTempNightFace)            

    def GetSymbol(self):
        return "o"
       
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

class GasGiant(World):
    def __init__(self, parentStar):
        World.__init__(self, "Gas Giant", parentStar)
        self.numSulfurWorlds = 0
        self.numInnerMoons = 0

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
            self.rotationalPeriod = GenerateRotationalPeriod(self.mainType, self.subType, tidalEffect)
        if self.rotationalPeriod > self.orbitalPeriod:
            parentLock = True
            self.rotationalPeriod = self.orbitalPeriod
        
    def ShowBasic(self):
        return self.GetSymbol() + " " + self.subType + " " + self.mainType

    def ShowDetails(self):
        return "----       ----       ----       ----      %- 10.3f %- 10.3f %- 10.3f %- 10.3f  ----       %-10s %-10s" % \
            (self.diameter, self.mass, self.density, self.gravity, PrettyPeriod(self.orbitalPeriod), PrettyPeriod(self.rotationalPeriod))

    def GetNumSulfurWorlds(self):
        return self.numSulfurWorlds

    def IncNumSulfurWorlds(self):
        self.numSulfurWorlds = self.numSulfurWorlds + 1

    def SetNumInnerMoons(self, n):
        self.numInnerMoons = n

    def GetSymbol(self):
        return "O"

class Belt(World):
    def __init__(self, parentStar):
        World.__init__(self, "Belt", parentStar)

    def GenerateBasic(self):
        """ Do Nothing Yet """

    def GenerateDynamics(self):
        """ Do Nothing Yet """

class Moonlet(World):
    def __init__(self, parentStar, parentWorld):
        World.__init__(self, "Moonlet", parentStar)
        self.parentWorld = parentWorld

    def GenerateBasic(self):
        """ Do Nothing Yet """

    def GenerateDynamics(self):
        """ Do Nothing Yet """
