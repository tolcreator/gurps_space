import dice
import star
import orbit
import math

stellarMassTable = [
               [ 0, 0, 0, 2.00, 2.00, 2.00, 2.00, 2.00, 2.00, 2.00, 2.00, 1.90, 1.90, 1.90, 1.90, 1.90, 1.90, 1.90, 1.90 ],
               [ 0, 0, 0, 2.00, 2.00, 2.00, 2.00, 2.00, 2.00, 2.00, 2.00, 1.90, 1.90, 1.90, 1.90, 1.90, 1.90, 1.90, 1.90 ],
               [ 0, 0, 0, 2.00, 2.00, 2.00, 2.00, 2.00, 2.00, 2.00, 2.00, 1.90, 1.90, 1.90, 1.90, 1.90, 1.90, 1.90, 1.90 ],
               [ 0, 0, 0, 2.00, 2.00, 2.00, 2.00, 2.00, 2.00, 2.00, 2.00, 1.90, 1.90, 1.90, 1.90, 1.90, 1.90, 1.90, 1.90 ],
               [ 0, 0, 0, 1.80, 1.80, 1.80, 1.80, 1.80, 1.80, 1.70, 1.70, 1.70, 1.60, 1.60, 1.60, 1.60, 1.60, 1.60, 1.60 ],
               [ 0, 0, 0, 1.50, 1.50, 1.50, 1.50, 1.50, 1.45, 1.45, 1.45, 1.40, 1.40, 1.35, 1.35, 1.35, 1.35, 1.35, 1.35 ],
               [ 0, 0, 0, 1.30, 1.30, 1.30, 1.30, 1.30, 1.25, 1.25, 1.20, 1.15, 1.15, 1.10, 1.10, 1.10, 1.10, 1.10, 1.10 ],
               [ 0, 0, 0, 1.05, 1.05, 1.05, 1.05, 1.05, 1.00, 1.00, 0.95, 0.90, 0.90, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85 ], 
               [ 0, 0, 0, 0.80, 0.80, 0.80, 0.80, 0.80, 0.75, 0.75, 0.70, 0.65, 0.65, 0.60, 0.60, 0.60, 0.60, 0.60, 0.60 ],
               [ 0, 0, 0, 0.55, 0.55, 0.55, 0.55, 0.55, 0.55, 0.50, 0.50, 0.50, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45 ],
               [ 0, 0, 0, 0.40, 0.40, 0.40, 0.40, 0.40, 0.40, 0.35, 0.35, 0.35, 0.30, 0.30, 0.30, 0.30, 0.30, 0.30, 0.30 ],
               [ 0, 0, 0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25 ],
               [ 0, 0, 0, 0.20, 0.20, 0.20, 0.20, 0.20, 0.20, 0.20, 0.20, 0.20, 0.20, 0.20, 0.20, 0.20, 0.20, 0.20, 0.20 ],
               [ 0, 0, 0, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15 ],
               [ 0, 0, 0, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10 ],
               [ 0, 0, 0, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10 ],
               [ 0, 0, 0, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10 ],
               [ 0, 0, 0, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10 ],
               [ 0, 0, 0, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10 ]
]

stellarAgeTable = [
               { "population":"invalid",                     "base":0.0,  "stepa":0.0, "stepb":0.0  },
               { "population":"invalid",                     "base":0.0,  "stepa":0.0, "stepb":0.0  },
               { "population":"invalid",                     "base":0.0,  "stepa":0.0, "stepb":0.0  },
               { "population":"Extreme Population I",        "base":0.0,  "stepa":0.0, "stepb":0.0  },
               { "population":"Young Population I",          "base":0.1,  "stepa":0.3, "stepb":0.05 },
               { "population":"Young Population I",          "base":0.1,  "stepa":0.3, "stepb":0.05 },
               { "population":"Young Population I",          "base":0.1,  "stepa":0.3, "stepb":0.05 },
               { "population":"Intermediate Population I",   "base":2.0,  "stepa":0.6, "stepb":0.1  },
               { "population":"Intermediate Population I",   "base":2.0,  "stepa":0.6, "stepb":0.1  },
               { "population":"Intermediate Population I",   "base":2.0,  "stepa":0.6, "stepb":0.1  },
               { "population":"Intermediate Population I",   "base":2.0,  "stepa":0.6, "stepb":0.1  },
               { "population":"Old Population I",            "base":5.6,  "stepa":0.6, "stepb":0.1  },
               { "population":"Old Population I",            "base":5.6,  "stepa":0.6, "stepb":0.1  },
               { "population":"Old Population I",            "base":5.6,  "stepa":0.6, "stepb":0.1  },
               { "population":"Old Population I",            "base":5.6,  "stepa":0.6, "stepb":0.1  },
               { "population":"Intermediate Population II",  "base":8.0,  "stepa":0.6, "stepb":0.1  },
               { "population":"Intermediate Population II",  "base":8.0,  "stepa":0.6, "stepb":0.1  },
               { "population":"Extreme Population II",       "base":8.0,  "stepa":0.6, "stepb":0.1  },
               { "population":"Extreme Population II",       "base":10.0, "stepa":0.6, "stepb":0.1  }
]

def GenerateNumStars():
    d = dice.roll(3, 6)
    if d <= 10:
        return 1
    if d <= 15:
        return 2
    return 3

def GenerateAge():
    p = dice.roll(3, 6)
    entry = stellarAgeTable[p]
    a = dice.roll(1, 6) - 1
    b = dice.roll(1, 6) - 1
    return entry["base"] + (entry["stepa"] * a) + (entry["stepb"] * b)

def GeneratePrimaryMass():
    f = dice.roll(3, 6)
    s = dice.roll(3, 6)
    return stellarMassTable[f][s]

def GenerateCompanionMass(primaryMass):
    m = dice.roll(1, 6)
    if m == 1:
        companionMass = primaryMass
    else:
        c = dice.roll(m-1, 6)
        companionMass = primaryMass - (float(c) * 0.05)
        if companionMass < 0.10:
            companionMass = 0.10
        if companionMass == 1.55:
            companionMass = 1.50
        if companionMass == 1.65:
            companionMass = 1.60
        if companionMass == 1.75:
            companionMass = 1.70
        if companionMass == 1.85:
            companionMass = 1.80
        if companionMass == 1.95:
            companionMass = 1.90
        if companionMass > 2.00:
            companionMass = 2.00
    return companionMass

def GenerateCompanionOrbit(primary, separationMod, minRadius, maxRadius):
    """ Separation """
    r = dice.roll(3, 6)
    r = r + separationMod
    if r <= 6:
        separation = "VeryClose"
        rm = 0.05
        em = -6
    elif r <= 9:
        separation = "Close"    
        rm = 0.5
        em = -4
    elif r <= 11:
        separation = "Moderate"
        rm = 2.0
        em = -2
    elif r <= 14:
        separation = "Wide"
        rm = 10.0
        em = 0
    else:
        separation = "Distant"
        rm = 50.0
        em = 0

    """ Radius """
    r = dice.roll(1, 6)
    if r == 1:
        mod = 50 + dice.roll(1, 50)
    elif r == 2:
        mod = 80 + dice.roll(1, 20)
    elif r == 3:
        mod = 94 + dice.roll(1, 6)
    elif r == 4:
        mod = 100 + dice.roll(1, 6)
    elif r == 5:
        mod = 100 + dice.roll(1, 20)
    elif r == 6:
        mod = 100 + dice.roll(1, 50)
    rm = (rm * mod) / 100
    r = dice.roll(2, 6)
    radius = r * rm
    if maxRadius != 0 and radius > maxRadius:
        radius = maxRadius
    if minRadius != 0 and radius < minRadius:
        radius = minRadius

    """ Eccentricity """
    r = dice.roll(3, 6)
    r = r + em
    if r <= 3:
        eccentricity = 0
    elif r == 4:
        eccentricity = 0.1
    elif r == 5:
        eccentricity = 0.2
    elif r == 6:
        eccentricity = 0.3
    elif r <= 8:
        eccentricity = 0.4
    elif r <= 11:
        eccentricity = 0.5
    elif r <= 13:
        eccentricity = 0.6
    elif r <= 15:
        eccentricity = 0.7
    elif r == 16:
        eccentricity = 0.8
    elif r == 17:
        eccentricity = 0.9
    else:
        eccentricity = 0.95
    return { "separation":separation, "radius":radius, "eccentricity":eccentricity }

def GenerateStars(age, stars):
    numStars = GenerateNumStars()
    """ Primary Star """
    primaryMass = GeneratePrimaryMass()
    primary = star.Star(primaryMass, age)
    primary.Generate()
    stars.append(primary)

    """ Companions? """
    minRadius = 0
    mod = 0
    for x in range(1, numStars):
        """ The mass of the primary may have changed during generation """
        companionMass = GenerateCompanionMass(primary.GetMass())
        companion = star.Star(companionMass, age)
        companion.Generate()
        stars.append(companion)
        details = GenerateCompanionOrbit(primary, mod, minRadius, 0)
        myOrbit = orbit.Orbit(primary, companion, details["radius"], details["eccentricity"])
        minRadius = myOrbit.GetMaxSeparation() * 3
        primary.AddOrbiter(myOrbit)
        companion.SetOrbit(myOrbit)
        mod = 6
        """ Check for distant companion """
        r = dice.roll(3, 6)
        if details["separation"] == "Distant" and r >= 11:
            """ The companion has a companion """
            distantMass = GenerateCompanionMass(companionMass)
            distant = star.Star(distantMass, age)
            distant.Generate()
            stars.append(distant)
            maxRadius = myOrbit.GetMinSeparation() / 3
            details = GenerateCompanionOrbit(distant, 0, 0, maxRadius)
            myOrbit = orbit.Orbit(companion, distant, details["radius"], details["eccentricity"])
            companion.AddOrbiter(myOrbit)
            distant.SetOrbit(myOrbit)

def GenerateGasGiantArrangement():
    r = dice.roll(3, 6)
    if r <= 10:
        return "None"
    if r <= 12:
        return "Conventional"
    if r <= 14:
        return "Eccentric"
    return "Epistellar"

def GenerateSpacing():
    r = dice.roll(3, 6)
    if r <= 4:
        ret = 1.4
    elif r <= 6:
        ret = 1.5
    elif r <= 8:
        ret = 1.6
    elif r <= 12:
        ret = 1.7
    elif r <= 14:
        ret = 1.8
    elif r <= 16:
        ret = 1.9
    else:
        ret = 2.0
    r = dice.roll(1, 10)
    ret = ret + (float(r) / 100) - 0.05
    return ret

def GenerateGasGiantPresence(arrangement, beyondSnowLine, mod):
    if arrangement == "None":
        return False
    r = dice.roll(3, 6) + mod
    if arrangement == "Conventional":
        if beyondSnowLine and r <= 15:
            return True
        else:
            return False
    elif arrangement == "Eccentric":
        if not beyondSnowLine and r <= 8:
            return True
        elif beyondSnowLine and r <= 14:
            return True
        else:
            return False
    else:
        if not beyondSnowLine and r <= 6:
            return True
        elif beyondSnowLine and r <= 14:
            return True
        else:
            return False

def GeneratePlacementType(mod):
        r = dice.roll(3, 6) - mod
        if r <= 3:
            return "Empty"
        if r <= 6:
            return "Belt"
        if r <= 8:
            return "Tiny"
        if r <= 11:
            return "Small"
        if r <= 15:
            return "Standard"
        return "Large"

""" Placements are rough orbits """
def GeneratePlacements(parentStar):
    """ Determine Inner Limit """
    limit1 = 0.1 * parentStar.GetMass()
    limit2 = 0.01 * math.sqrt(parentStar.GetLuminosity())
    innerLimit = max(limit1, limit2)

    """ Outer limit """
    outerLimit = 40 * parentStar.GetMass()

    """ Snow line requires *initial* luminosity """
    snowLine = 4.85 * math.sqrt(parentStar.GetInitialLuminosity())

    """ Forbidden Zones """
    forbiddenZones = []
    if parentStar.GetOrbit():
        innerEdge = parentStar.GetOrbit().GetMinSeparation() / 3
        forbiddenZones.append( { "in":innerEdge, "out":0.0 } )
    for orbiter in parentStar.GetOrbiters():
        innerEdge = orbiter.GetMinSeparation() / 3
        outerEdge = orbiter.GetMaxSeparation() * 3
        forbiddenZones.append( { "in":innerEdge, "out":outerEdge } )

    """ See if we have Gas Giants """
    """ Check if snow line within a forbidden zone """
    disqualified = False
    for zone in forbiddenZones:
        if snowLine > zone["in"] and snowLine < zone["out"]:
            disqualified = True
    if disqualified:
        arrangement = "None"
    else:
        arrangement = GenerateGasGiantArrangement()
    firstGasGiantRadius = 0
    if arrangement == "Conventional":
        r = dice.roll(2, 6) - 2
        firstGasGiantRadius = ((float(r) * 0.05) + 1) * snowLine
    elif arrangement == "Eccentric":
        r = dice.roll(1, 6)
        firstGasGiantRadius = float(r) * 0.125 * snowLine
    elif arrangement == "Epistellar":
        r = dice.roll(3, 6)
        firstGasGiantRadius = float(r) * 0.1 * innerLimit

    """ check if orbit in forbidden zone """
    disqualified = False
    for zone in forbiddenZones:
        if firstGasGiantRadius > zone["in"] and firstGasGiantRadius < zone["out"]:
            disqualified = True
    if disqualified:
        """ There is a tiny chance that even in the forbidden zone,
        the gas giant can exist. Probably less than 1:100, but we'll
        go with that barring a hard and fast rule """
        r = dice.roll(1, 100)
        if r != 1:
            firstGasGiantRadius = 0
    
    """ Now we place all other orbits """
    """ Placements needs to include radius, object type, and modifier """
    placements = []
    if firstGasGiantRadius:
        cursor = firstGasGiantRadius
        placements.append( { "Radius":cursor, "Type":"Gas Giant", "Mod":0 } )
    else:
        cursor = outerLimit
        mod = 3
        for zone in forbiddenZones:
            if outerLimit > zone["in"] and outerLimit < zone["out"]:
                """ we may move start several times: choose the lowest """
                cursor = min(zone["in"], cursor)
                mod = 6
        r = dice.roll(1, 6)
        cursor = cursor / ((float(r) * 0.05) + 1)
        if cursor > innerLimit:
            placements.append( { "Radius":cursor, "Type":"Unassigned", "Mod":mod } )

    """ Work in from gas giant or outer limit """
    previous = None
    while cursor >= innerLimit:
        placement = None
        spacing = GenerateSpacing() 
        cursor = cursor / spacing
        place = True
        for zone in forbiddenZones:
            if cursor > zone["in"] and cursor < zone["out"]:
                place = False
                if previous:
                    previous["Mod"] = previous["Mod"] + 6
        if cursor < innerLimit:
            if previous:
                previous["Mod"] = previous["Mod"] + 3
            place = False
        if place:
            placement = { "Radius":cursor, "Type":"Unassigned", "Mod":0 }
            placements.append(placement)
            previous = placement
        else:
            previous = None

    """ Work out from gas giant """
    if firstGasGiantRadius:
        cursor = firstGasGiantRadius
        while cursor <= outerLimit:
            spacing = GenerateSpacing()
            cursor = cursor * spacing
            place = True
            if cursor > outerLimit:
                place = False
            for zone in forbiddenZones:
                if cursor > zone["in"] and cursor < zone["out"]:
                    place = False
            if place:
                placements.append( { "Radius":cursor, "Type":"Unassigned", "Mod":0 } )
    placements.sort(key = lambda p: p["Radius"])
    
    """ Now work out what goes where """
    """ Gas Giants """
    beyondSnowLine = False
    previous = None
    nextMod = 0
    for placement in placements:
        placement["Mod"] = placement["Mod"] + nextMod
        if placement["Type"] == "Unassigned":
            mod = 0
            if placement["Radius"] <= snowLine:
                mod = 4
            elif not beyondSnowLine:
                beyondSnowLine = True
                mod = 4
            if GenerateGasGiantPresence(arrangement, beyondSnowLine, mod):
                placement["Type"] = "Gas Giant"
                nextMod = 3
                if previous:
                    previous["Mod"] = previous["Mod"] + 3
            else:
                nextMod = 0
        previous = placement
    
    """ Fill remaining orbits """
    for placement in placements:
        if placement["Type"] == "Unassigned":
            placement["Type"] = GeneratePlacementType(placement["Mod"])      

    """ And we're done """ 
    return placements

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

""" Including Moons """
def GenerateWorld(parentStar, placement):
    oRadius = placement["Radius"]
    blackBodyTemperature = 278 * ( pow(parentStar.GetLuminosity(), 0.25) / pow(oRadius, 0.5) )
    subType = GetWorldSubtype(placement["Type"], blackBodyTemperature)
    """ Fix Ammonia worlds now """
    if subType == "Ammonia" and parentStar.GetMass() > 0.65:
        subType = "Ice"
    print "    %06.3f: %s %s" % (placement["Radius"], placement["Type"], subType)

def GenerateWorlds(parentStar, age, worlds):
    placements = GeneratePlacements(parentStar)
    print parentStar
    for placement in placements:
        if not placement["Type"] == "Empty":
            world = GenerateWorld(parentStar, placement)

class System:
    def __init__(self):
        self.stars = []
        self.worlds = []
        self.age = 0.0

    def Generate(self):
        self.age = GenerateAge()
        GenerateStars(self.age, self.stars)
        for s in self.stars:
            GenerateWorlds(s, self.age, self.worlds)
              
    def __str__(self):
        primary = self.stars[0]
        ret = primary.__str__()
        for orbit in primary.GetOrbiters():
            companion = orbit.GetOrbiter()
            ret = ret + "\n    "
            ret = ret + orbit.__str__()
            ret = ret + " "
            ret = ret + companion.__str__()
            for orbit in companion.GetOrbiters():
                companion = orbit.GetOrbiter()
                ret = ret + "\n        "
                ret = ret + orbit.__str__()
                ret = ret + " "
                ret = ret + companion.__str__()
        return ret           
