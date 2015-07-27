import dice
import world
import orbit
import math

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

""" TODO make a terrestrial body class, and make planets and moons subclasses of this """

class Planet(world.World):
    def __init__(self, mainType, parentStar, parentWorld = None):
        world.World.__init__(self, mainType, parentStar)
        self.parentWorld = parentWorld

    def ShowBasic(self):
        return self.GetSymbol() + " " + self.mainType + " " + self.subType

    def ShowDetails(self):
        ret = "%-10s %-10d %-10s %-10d%- 10.3f %- 10.3f %- 10.3f %- 10.3f %- 10.3f  %-10s %-10s %- 10d %-10s %-10s %-3d %-3d %-3d " % \
            (self.atmosphericCategory, self.hydrosphere, self.climate, self.averageTemperature, \
             self.diameter, self.mass, self.density, self.gravity, self.atmosphericPressure, \
             world.PrettyPeriod(self.orbitalPeriod), world.PrettyPeriod(self.rotationalPeriod), self.axialTilt, \
             self.vulcanism, self.tectonics, self.habitability, self.resourceValue, self.affinity)
        return ret

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
        if not self.parentStar.GetType() == "L" and not self.parentStar.GetType() == "T" and not self.parentStar.GetType() == "Y":
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
        self.gravity = world.GetGravity(self.density, self.diameter)
        self.mass = world.GetMass(self.density, self.diameter)
         
        atmosphericMass = GenerateAtmosphericMass(self.mainType, self.subType)
        self.hydrosphere = GenerateHydrosphere(self.mainType, self.subType)
        blackBodyCorrection = GetBlackBodyCorrection(self.mainType, self.subType, self.hydrosphere, atmosphericMass)
        self.averageTemperature = blackBodyTemperature * blackBodyCorrection
        self.climate = world.GetClimate(self.averageTemperature)
        self.atmosphericPressure = GetAtmosphericPressure(self.mainType, self.subType, atmosphericMass, self.gravity)
        self.atmosphericCategory = GetAtmosphericCategory(self.atmosphericPressure)

    def GenerateDynamics(self):
        """ Orbital period in days """
        parentLock = False
        lunarLock = False
        possibleLunarLock = False
        possibleSolarLock = False
        potentialRotationalPeriod = 0
        if self.parentWorld:
            self.orbitalPeriod = math.sqrt(pow(self.orbit.GetRadius(), 3) / self.parentWorld.GetMass()) * 0.166
            tide = (2230000 * self.parentWorld.GetMass() * self.diameter) / pow(self.orbit.GetRadius(), 3)
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
                        potentialRotationalPeriod = math.sqrt(pow(o.GetRadius(), 3) / self.GetMass()) * 0.166
                    tide = tide + (2230000 * m.GetMass() * self.diameter) / pow(o.GetRadius(), 3)
        tidalEffect = (tide * self.parentStar.GetAge()) / self.mass
        if tidalEffect > 50:
            if possibleLunarLock:
                lunarLock = True
                self.rotationalPeriod = potentialRotationalPeriod
            else:
                parentLock = True
                self.rotationalPeriod = self.orbitalPeriod
                if not self.parentWorld:
                    possibleSolarLock = True
        else:
            self.rotationalPeriod = world.GenerateRotationalPeriod(self.mainType, None, tidalEffect)
        if possibleLunarLock and self.rotationalPeriod > potentialRotationalPeriod:
            lunarLock = True
            self.rotationalPeriod = self.orbitalPeriod
        elif self.rotationalPeriod > self.orbitalPeriod:
            parentLock = True
            self.rotationalPeriod = self.orbitalPeriod
            if not self.parentWorld:
                possibleSolarLock = True
        self.axialTilt = world.GenerateAxialTilt()

        if possibleSolarLock:
            if self.orbit.GetEccentricity() >= 0.1:
                r = dice.roll(3, 6)
                if r >= 12:
                    possibleSolarLock = False
                    self.rotationalPeriod = self.orbitalPeriod * (3.0/2.0)

        if possibleSolarLock:
            self.SolarLockCorrection()

    def SolarLockCorrection(self):
        DF = 1.0
        NF = 1.0
        p = self.atmosphericPressure
        if self.atmosphericCategory == "Vacuum" or self.atmosphericCategory == "Trace":
            self.atmosphericCategory = "Vacuum"
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
        self.dayFaceClimate = world.GetClimate(self.avTempDayFace)
        self.nightFaceClimate = world.GetClimate(self.avTempNightFace)            

    def GetNumMajorMoons(self):
        majorMoons = 0
        for o in self.orbiters:
            m = o.GetOrbiter()
            if not m.GetType() == "Moonlet":
                majorMoons = majorMoons + 1
        return majorMoons

    def GenerateVulcanism(self):
        if self.parentStar.GetAge() == 0:
            mod = 40
        else:
            mod = int((self.gravity / self.parentStar.GetAge()) * 40)
        majorMoons = self.GetNumMajorMoons()
        if majorMoons == 1:
            mod = mod + 5
        elif majorMoons > 1:
            mod = mod + 10
        if self.subType == "Sulfur":
            mod = mod + 60
        elif self.parentWorld:
            if self.parentWorld.GetType == "Gas Giant":
                mod = mod + 5 
        r = dice.roll(3, 6) + mod
        if r <= 16:
            self.vulcanism =  "None"
        elif r <= 20:
            self.vulcanism = "Light"
        elif r <= 26:
            self.vulcanism = "Moderate"
        elif r <= 70:
            self.vulcanism = "Heavy"
        else:
            self.vulcanism = "Extreme"
        """ TODO figure out if atmosphere is marginal """

    def GenerateTectonicActivity(self):
        if self.mainType == "Tiny" or self.mainType == "Small":
            self.tectonics = "None"
            return
        mod = 0
        if self.vulcanism == "None":
            mod = mod - 8
        elif self.vulcanism == "Light":
            mod = mod - 4
        elif self.vulcanism == "Heavy":
            mod = mod + 4
        elif self.vulcanism == "Extreme":
            mod = mod + 8
        if self.hydrosphere == 0:
            mod = mod - 4
        elif self.hydrosphere <= 50:
            mod = mod - 2
        majorMoons = self.GetNumMajorMoons()
        if majorMoons == 1:
            mod = mod + 2
        elif majorMoons > 1:
            mod = mod + 4
        r = dice.roll(3, 6) + mod
        if r <= 6:
            self.tectonics = "None"
        elif r <= 10:
            self.tectonics = "Light"
        elif r <= 14:
            self.tectonics = "Moderate"
        elif r <= 18:
            self.tectonics = "Heavy"
        else:
            self.tectonics = "Extreme"

    def GenerateMarginalComponents(self):
        self.atmosphericComposition.append("Marginal")
        r = dice.roll(3, 6)
        if r <= 3:
            self.atmosphericComposition.append("Flourine")
            self.atmosphericComposition.append("Highly Toxic")
            return
        if r <= 4:
            self.atmosphericComposition.append("Chlorine")
            self.atmosphericComposition.append("Highly Toxic")
            return
        if r <= 6:
            self.atmosphericComposition.append("Sulfur Compounds")
            self.atmosphericComposition.append("Mildly Toxic")
            return
        if r <= 7:
            self.atmosphericComposition.append("Nitrogen Compounds")
            self.atmosphericComposition.append("Mildly Toxic")
            return
        if r <= 9:
            self.atmosphericComposition.append("Organic Toxins")
            self.atmosphericComposition.append("Mildly Toxic")
            return
        if r <= 11:
            self.atmosphericComposition.append("Low Oxygen")
            return
        if r <= 13:
            self.atmosphericComposition.append("Pollutants")
            self.atmosphericComposition.append("Mildly Toxic")
            return
        if r <= 14:
            self.atmosphericComposition.append("High Carbon Dioxide")
            self.atmosphericComposition.append("Mildly Toxic")
            return
        if r <= 16:
            self.atmosphericComposition.append("High Oxygen")
            self.atmosphericComposition.append("Mildly Toxic")
            return
        self.atmosphericComposition.append("Inert Gasses")
        return

    def GenerateVolcanicPollutants(self):
        r = dice.roll(3, 6)
        target = 0
        if self.vulcanism == "Heavy":
            target = 8
        if self.vulcanism == "Extreme":
            target = 14
        if r <= target:
            self.atmosphericComposition.append("Marginal")
            r = dice.roll(1, 6)
            if r <= 3:
                self.atmosphericComposition.append("Pollutants")
                self.atmosphericComposition.append("Mildly Toxic")
            else:
                self.atmosphericComposition.append("Sulfur Compounds")
                self.atmosphericComposition.append("Mildly Toxic")

    def GenerateAtmosphericComposition(self):
        self.atmosphericComposition = []
        if self.atmosphericCategory == "Vacuum" or self.atmosphericCategory == "Trace":
            self.atmosphericComposition.append("None")
            return

        if self.mainType == "Small" and self.subType == "Ice":
            r = dice.roll(3, 6)
            if r <= 15:
                self.atmosphericComposition.append("Suffocating")
                self.atmosphericComposition.append("Mildly Toxic")
                return
            else:
                self.atmosphericComposition.append("Suffocating")
                self.atmosphericComposition.append("Highly Toxic")
                return
        if self.mainType == "Standard":
            if self.subType == "Ammonia" or self.subType == "Greenhouse":
                self.atmosphericComposition.append("Suffocating")
                self.atmosphericComposition.append("Lethally Toxic")
                self.atmosphericComposition.append("Corrosive")
                return
            if self.subType == "Ice" or self.subType == "Ocean":
                r = dice.roll(3, 6)
                if r <= 12:
                    self.atmosphericComposition.append("Suffocating")
                    return
                else:               
                    self.atmosphericComposition.append("Suffocating")
                    self.atmosphericComposition.append("Mildly Toxic")
                    return
            if self.subType == "Garden":
                r = dice.roll(3, 6)
                if r <= 11:
                    self.atmosphericComposition.append("Breatheable")
                    self.GenerateVolcanicPollutants()
                    return
                else:
                    self.atmosphericComposition.append("Breatheable")
                    self.GenerateMarginalComponents()
                    return
        if self.mainType == "Large":
            if self.subType == "Ammonia" or self.subType == "Greenhouse":        
                self.atmosphericComposition.append("Suffocating")
                self.atmosphericComposition.append("Lethallly Toxic")
                self.atmosphericComposition.append("Corrosive")
                return
            if self.subType == "Ice" or self.subType == "Ocean" or self.subType == "Hadean":
                self.atmosphericComposition.append("Suffocating")
                self.atmosphericComposition.append("Highly Toxic")
                return
            if self.subType == "Garden":
                r = dice.roll(3, 6)
                if r <= 11:
                    self.atmosphericComposition.append("Breatheable")
                    self.GenerateVolcanicPollutants()
                    return
                else:
                    self.atmosphericComposition.append("Breatheable")
                    self.GenerateMarginalComponents()
                    return
        print "Shouldn't get here %s %s %d" % (self.mainType, self.subType, self.averageTemperature)           

    def GenerateResourceValue(self):
        mod = 0
        if self.vulcanism == "None":
            mod = -2
        elif self.vulcanism == "Light":
            mod = -1
        elif self.vulcanism == "Heavy":
            mod = 1
        elif self.vulcanism == "Extreme":
            mod = 2
        r = dice.roll(3, 6) + mod
        if r <= 2:
            self.overallValue = "Scant"
            self.resourceValue = -3
        elif r <= 4:
            self.overallValue = "Very Poor"
            self.resourceValue = -2
        elif r <= 7:
            self.overallValue = "Poor"
            self.resourceValue = -1
        elif r <= 13:
            self.overallValue = "Average"
            self.resourceValue = 0
        elif r <= 16:
            self.overallValue = "Abundant"
            self.resourceValue = 1
        elif r <= 18:
            self.overallValue = "Very Abundant"
            self.resourceValue = 2
        else:
            self.overallValue = "Rich"
            self.resourceValue = 3

    def GetHabitabilityAndAffinity(self):
        self.habitability = 0
        """ Vulcanism and Tectonics """
        if self.vulcanism == "Heavy":
            self.habitability = self.habitability - 1
        elif self.vulcanism == "Extreme":
            self.habitability = self.habitability - 2
        if self.tectonics == "Heavy":
            self.habitability = self.habitability - 1
        elif self.tectonics == "Extreme":
            self.habitability = self.habitability - 2

        """ Atmosphere """
        if "Breatheable" in self.atmosphericComposition:
            if self.atmosphericCategory == "Very Thin":
                self.habitability = self.habitability + 1
            elif self.atmosphericCategory == "Thin":
                self.habitability = self.habitability + 2
            elif self.atmosphericCategory == "Standard" or self.atmosphericCategory == "Dense":
                self.habitability = self.habitability + 3
            elif self.atmosphericCategory == "Very Dense" or self.atmosphericCategory == "Superdense":
                self.habitability = self.habitability + 2
            if "Marginal" not in self.atmosphericComposition:
                self.habitability = self.habitability + 1
            if self.climate == "Cold" or self.climate == "Hot":
                 self.habitability = self.habitability + 1
            elif self.climate == "Chilly" or self.climate == "Cool" or self.climate == "Normal" or self.climate == "Warm" or self.climate == "Tropical":
                 self.habitability = self.habitability + 2
        elif not self.atmosphericCategory == "Vaccum" and not self.atmosphericCategory == "Trace":
            if "Corrosive" in self.atmosphericComposition:
                self.habitability = self.habitability - 2
            elif "Mildly Toxic" in self.atmosphericComposition or "Highly Toxic" in self.atmosphericComposition or "Lethally Toxic" in self.atmosphericComposition:
                self.habitability = self.habitability - 1

        """ Hydrosphere """
        if self.hydrosphere > 1:
            if self.hydrosphere <= 59:
                self.habitability = self.habitability + 1
            elif self.hydrosphere <= 90:
                self.habitability = self.habitability + 2
            elif self.hydrosphere <= 90:
                self.habitability = self.habitability + 1
        
        self.affinity = self.habitability + self.resourceValue        

    def GenerateDetails(self):
        self.GenerateVulcanism()
        self.GenerateTectonicActivity()
        self.GenerateAtmosphericComposition()
        self.GenerateResourceValue()
        self.GetHabitabilityAndAffinity()

    def GetSymbol(self):
        return "o"

    def GetAffinity(self):
        return self.affinity

    def GetIsAMoon(self):
        if self.parentWorld:
            return True
        return False

    def GetAtmosphericComposition(self):
        return self.atmosphericComposition
