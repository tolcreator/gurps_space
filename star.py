import dice
import math
import body
import orbit

stellarEvolutionTable = [
    { "mass":0.10, "type":"M7", "temperature":3100, "lmin":0.0012, "lmax":0,    "mspan":0,   "sspan":0,   "gspan":0   },
    { "mass":0.15, "type":"M6", "temperature":3200, "lmin":0.0036, "lmax":0,    "mspan":0,   "sspan":0,   "gspan":0   },
    { "mass":0.20, "type":"M5", "temperature":3200, "lmin":0.0079, "lmax":0,    "mspan":0,   "sspan":0,   "gspan":0   },
    { "mass":0.25, "type":"M4", "temperature":3300, "lmin":0.015,  "lmax":0,    "mspan":0,   "sspan":0,   "gspan":0   },
    { "mass":0.30, "type":"M4", "temperature":3300, "lmin":0.024,  "lmax":0,    "mspan":0,   "sspan":0,   "gspan":0   },
    { "mass":0.35, "type":"M3", "temperature":3400, "lmin":0.037,  "lmax":0,    "mspan":0,   "sspan":0,   "gspan":0   },
    { "mass":0.40, "type":"M2", "temperature":3500, "lmin":0.054,  "lmax":0,    "mspan":0,   "sspan":0,   "gspan":0   },
    { "mass":0.45, "type":"M1", "temperature":3600, "lmin":0.07,   "lmax":0.08, "mspan":70,  "sspan":0,   "gspan":0   },
    { "mass":0.50, "type":"M0", "temperature":3800, "lmin":0.09,   "lmax":0.11, "mspan":59,  "sspan":0,   "gspan":0   },
    { "mass":0.55, "type":"K8", "temperature":4000, "lmin":0.11,   "lmax":0.15, "mspan":50,  "sspan":0,   "gspan":0   },
    { "mass":0.60, "type":"K6", "temperature":4200, "lmin":0.13,   "lmax":0.20, "mspan":42,  "sspan":0,   "gspan":0   },
    { "mass":0.65, "type":"K5", "temperature":4400, "lmin":0.15,   "lmax":0.25, "mspan":37,  "sspan":0,   "gspan":0   },
    { "mass":0.70, "type":"K4", "temperature":4600, "lmin":0.19,   "lmax":0.35, "mspan":30,  "sspan":0,   "gspan":0   },
    { "mass":0.75, "type":"K2", "temperature":4900, "lmin":0.23,   "lmax":0.48, "mspan":24,  "sspan":0,   "gspan":0   },
    { "mass":0.80, "type":"K0", "temperature":5200, "lmin":0.28,   "lmax":0.65, "mspan":20,  "sspan":0,   "gspan":0   },
    { "mass":0.85, "type":"G8", "temperature":5400, "lmin":0.36,   "lmax":0.84, "mspan":17,  "sspan":0,   "gspan":0   },
    { "mass":0.90, "type":"G6", "temperature":5500, "lmin":0.45,   "lmax":1.0,  "mspan":14,  "sspan":0,   "gspan":0   },
    { "mass":0.95, "type":"G4", "temperature":5700, "lmin":0.56,   "lmax":1.3,  "mspan":12,  "sspan":1.8, "gspan":1.1 },
    { "mass":1.00, "type":"G2", "temperature":5800, "lmin":0.68,   "lmax":1.6,  "mspan":10,  "sspan":1.6, "gspan":1.0 },
    { "mass":1.05, "type":"G1", "temperature":5900, "lmin":0.87,   "lmax":1.9,  "mspan":8.8, "sspan":1.4, "gspan":0.8 },
    { "mass":1.10, "type":"G0", "temperature":6000, "lmin":1.1,    "lmax":2.2,  "mspan":7.7, "sspan":1.2, "gspan":0.7 },
    { "mass":1.15, "type":"F9", "temperature":6100, "lmin":1.4,    "lmax":2.6,  "mspan":6.7, "sspan":1.0, "gspan":0.6 },
    { "mass":1.20, "type":"F8", "temperature":6300, "lmin":1.7,    "lmax":3.0,  "mspan":5.9, "sspan":0.9, "gspan":0.6 },
    { "mass":1.25, "type":"F7", "temperature":6400, "lmin":2.1,    "lmax":3.5,  "mspan":5.2, "sspan":0.8, "gspan":0.5 },
    { "mass":1.30, "type":"F6", "temperature":6500, "lmin":2.5,    "lmax":3.9,  "mspan":4.6, "sspan":0.7, "gspan":0.4 },
    { "mass":1.35, "type":"F5", "temperature":6600, "lmin":3.1,    "lmax":4.5,  "mspan":4.1, "sspan":0.6, "gspan":0.4 },
    { "mass":1.40, "type":"F4", "temperature":6700, "lmin":3.7,    "lmax":5.1,  "mspan":3.7, "sspan":0.6, "gspan":0.4 },
    { "mass":1.45, "type":"F3", "temperature":6900, "lmin":4.3,    "lmax":5.7,  "mspan":3.3, "sspan":0.5, "gspan":0.3 },
    { "mass":1.50, "type":"F2", "temperature":7000, "lmin":5.1,    "lmax":6.5,  "mspan":3.0, "sspan":0.5, "gspan":0.3 },
    { "mass":1.60, "type":"F0", "temperature":7300, "lmin":6.7,    "lmax":8.2,  "mspan":2.5, "sspan":0.4, "gspan":0.2 },
    { "mass":1.70, "type":"A9", "temperature":7500, "lmin":8.6,    "lmax":10,   "mspan":2.1, "sspan":0.3, "gspan":0.2 },
    { "mass":1.80, "type":"A7", "temperature":7800, "lmin":11,     "lmax":13,   "mspan":1.8, "sspan":0.3, "gspan":0.2 },
    { "mass":1.90, "type":"A6", "temperature":8000, "lmin":13,     "lmax":16,   "mspan":1.5, "sspan":0.2, "gspan":0.1 },
    { "mass":2.00, "type":"A5", "temperature":8200, "lmin":16,     "lmax":20,   "mspan":1.3, "sspan":0.2, "gspan":0.1 }
]

class Star(body.Body):
    """ Mass is in stellar masses. 1.0 = mass of the Sun """
    """ Age is in Billions of years """
    def __init__(self, mass, age):
        body.Body.__init__(self)
        self.age = age
        self.mass = mass

    def Generate(self):
        self.setEntry = self.GetStellarEvolutionTableEntry()
        self.luminosityClass = self.DetermineLuminosityClass()
        self.luminosity = self.DetermineLuminosity() 
        self.temperature = self.DetermineTemperature()
        self.spectralType = self.DetermineSpectralType()
        self.radius = self.DetermineRadius()

    def GetType(self):
        return "%s %s" % (
                self.spectralType,
                self.luminosityClass)

    def GetAge(self):
        return self.age

    def GetMass(self):
        return self.mass

    def GetLuminosity(self):
        return self.luminosity

    def GetInitialLuminosity(self):
        return self.setEntry["lmin"]

    def GetSnowLine(self):
        return 4.85 * math.sqrt(self.GetInitialLuminosity())

    def GetIsInsideSnowLine(self, r):
        if r <= self.GetSnowLine():
            return True
        return False

    def GetIsFirstOrbitBeyondSnowLine(self, r):
        for o in self.orbiters:
            if r == o.GetRadius():
                if r > self.GetSnowLine():
                    return True
            else:
                 if o.GetRadius() > self.GetSnowLine():
                     return False
        return False

    def GetStellarEvolutionTableEntry(self):
        for entry in stellarEvolutionTable:
            if self.mass <= entry["mass"]:
                return entry
        """ Eh? Ran off the table? What about them big stars? """
        return entry            

    def DetermineLuminosityClass(self):
        if self.setEntry["mspan"] == 0:
            return "V"
        elif self.setEntry["mspan"] >= self.age:
            return "V"
        elif self.setEntry["sspan"] == 0:
            return "IV"
        elif (self.setEntry["mspan"] + self.setEntry["sspan"]) >= self.age:
            return "IV"
        elif self.setEntry["gspan"] == 0:
            return "III"
        elif (self.setEntry["mspan"] + self.setEntry["sspan"] + self.setEntry["gspan"]) >= self.age:
            return "III"
        self.mass = (dice.roll(2, 6) * 0.05) + 0.9
        return "D"

    def DetermineLuminosity(self):
        if self.luminosityClass == "V":
            luminosity = self.DetermineMainSequenceLuminosity()
        elif self.luminosityClass == "IV":
            luminosity = self.DetermineSubgiantLuminosity()
        elif self.luminosityClass == "III":
            luminosity = self.DetermineGiantLuminosity()
        else:
            return self.DetermineDwarfLuminosity()
        roll = dice.roll(1, 6)
        if roll <= 1:
            mod = 90 + dice.roll(1, 10)
        if roll == 2:
            mod = 94 + dice.roll(1, 6)
        if roll == 3:
            mod = 96 + dice.roll(1, 4)
        if roll == 4:
            mod = 100 + dice.roll(1, 4)
        if roll == 5:
            mod = 100 + dice.roll(1, 6)
        if roll >= 6:
            mod = 100 + dice.roll(1, 10)
        m = float(mod) / 100
        return luminosity * m

    def DetermineMainSequenceLuminosity(self):
        lmin = self.setEntry["lmin"]
        if self.setEntry["lmax"] == 0:
            lmax = lmin
        else:
            lmax = self.setEntry["lmax"]
        if self.setEntry["mspan"] == 0:
            return lmin
        s = float(self.setEntry["mspan"])
        a = float(self.age)
        l = lmin + ((a/s) * (lmax - lmin))
        return l

    def DetermineSubgiantLuminosity(self):
        if self.setEntry["lmax"] == 0:
            return self.setEntry["lmin"]
        return self.setEntry["lmax"]

    def DetermineGiantLuminosity(self):
        if self.setEntry["lmax"] == 0:
            return self.setEntry["lmin"] * 25
        return self.setEntry["lmax"] * 25

    def DetermineDwarfLuminosity(self):
        return 0

    def DetermineTemperature(self):
        if self.luminosityClass == "V":
            temperature = self.DetermineMainSequenceTemperature()
        elif self.luminosityClass == "IV":
            temperature = self.DetermineSubgiantTemperature()
        elif self.luminosityClass == "III":
            temperature = self.DetermineGiantTemperature()
        else:
            return self.DetermineDwarfTemperature()
        roll = dice.roll(1, 6)
        if roll == 1:
            temperature = temperature - dice.roll(1, 100)
        if roll == 2:
            temperature = temperature - dice.roll(1, 60)
        if roll == 3:
            temperature = temperature - dice.roll(1, 40)
        if roll == 4:
            temperature = temperature + dice.roll(1, 40)
        if roll == 5:
            temperature = temperature + dice.roll(1, 60)
        if roll == 6:
            temperature = temperature + dice.roll(1, 100)
        return temperature

    def DetermineMainSequenceTemperature(self):
        return self.setEntry["temperature"]

    def DetermineSubgiantTemperature(self):
        m = self.setEntry["temperature"]
        a = float(self.age)
        a = a - self.setEntry["mspan"]
        s = float(self.setEntry["sspan"])
        if s == 0:
            return m
        t = m - ((a/s) * (m - 4800))
        return t

    def DetermineGiantTemperature(self):
        roll = dice.roll(2, 6)
        return (roll * 200) + 3000

    def DetermineDwarfTemperature(self):
        return 0

    def DetermineSpectralType(self):
        if self.luminosityClass == "V":
            return self.setEntry["type"]
        if self.luminosityClass == "IV":
            return self.GetSpectralTypeFromTemperature()
        if self.luminosityClass == "III":
            return self.GetSpectralTypeFromTemperature()
        return "D"

    def GetSpectralTypeFromTemperature(self):
        t = self.temperature / 100
        t = t * 100
        for entry in stellarEvolutionTable:
            if t <= entry["temperature"]:
                return entry["type"]
        """ Fell off the end? What about super hot stars? """
        return "A5"
    
    def DetermineRadius(self):
        """ in AU """
        """ Hope this keeps some precision... """
        if self.temperature == 0:
            return 0
        return (155000 * math.sqrt(self.luminosity)) / (math.pow(self.temperature, 2))
    
    def GetSymbol(self):
        return "*"


class BrownDwarf(Star):
    def __init__(self, mass, age):
        Star.__init__(self, mass, age)
