import dice
import star
import world
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

def GenerateGasGiantArrangement(parentStar):
    """ Snow line requires *initial* luminosity """
    snowLine = parentStar.GetSnowLine()
    forbiddenZones = GetForbiddenZones(parentStar)
    """ Check if snow line within a forbidden zone """
    disqualified = False
    for zone in forbiddenZones:
        if snowLine > zone["in"] and snowLine < zone["out"]:
            disqualified = True
    if disqualified:
        return "None"

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

def GetForbiddenZones(parentStar):
    forbiddenZones = []
    if parentStar.GetOrbit():
        innerEdge = parentStar.GetOrbit().GetMinSeparation() / 3
        forbiddenZones.append( { "in":innerEdge, "out":10000 } )
    for orbiter in parentStar.GetOrbiters():
        innerEdge = orbiter.GetMinSeparation() / 3
        outerEdge = orbiter.GetMaxSeparation() * 3
        forbiddenZones.append( { "in":innerEdge, "out":outerEdge } )
    return forbiddenZones

""" Placements are rough orbits """
def GeneratePlacements(parentStar, arrangement):
    """ Determine Inner Limit """
    limit1 = 0.1 * parentStar.GetMass()
    limit2 = 0.01 * math.sqrt(parentStar.GetLuminosity())
    innerLimit = max(limit1, limit2)

    """ Outer limit """
    outerLimit = 40 * parentStar.GetMass()

    """ Snow line requires *initial* luminosity """
    snowLine = parentStar.GetSnowLine()
    forbiddenZones = GetForbiddenZones(parentStar)

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

def GetWorldEccentricity(mod):
    r = dice.roll(3, 6) + mod
    upvar = 0.025
    downvar = 0.025
    if r <= 3:
        rough = 0.0
    elif r <= 6:
        rough = 0.05
    elif r <= 9:
        rough = 0.1
    elif r <= 11:
        rough = 0.15
    elif r <= 12:
        rough = 0.2
        upvar = 0.05
    elif r >= 18:
        rough = 0.8
        upvar = 0.05
        downvar = 0.05
    else:
        rough = float(r - 10) / 10
        upvar = 0.05
        downvar = 0.05
    r = dice.roll(1, 2)
    if r == 1:
        r = dice.roll(1, 100)
        upvar = (upvar / 100) * float(r)
        ret = rough + upvar
    else:
        r = dice.roll(1, 100)
        downvar = (downvar / 100) * float(r)
        ret = rough - downvar
    return max(ret, 0)

def GenerateMoonType(parentType):
    r = dice.roll(3, 6)
    if r <= 11:
        return "Tiny"
    elif r <= 14:
        if parentType == "Gas Giant" or parentType == "Large":
            return "Small"
        else:
            return "Tiny"
    else:
        if parentType == "Gas Giant" or parentType == "Large":
            return "Standard"
        elif parentType == "Standard":
            return "Small"
        else:
            return "Tiny"

def GenerateTerrestrialMajorMoonOrbitRadius(moonType, planetType, existingOrbit):
    mod = 0
    if moonType == "Tiny":
        if planetType == "Small":
            mod = 4
        elif planetType == "Standard":
            mod = 2
    elif moonType == "Small":
        if planetType == "Standard":
            mod = 4
        elif planetType == "Large":
            mod = 2
    else:
        mod = 4
    r = existingOrbit
    while r == existingOrbit:
        r = dice.roll(2, 6) + mod
    return r

def GenerateTerrestrialMinorMoonOrbitRadius(existingOrbits):
    legal = False
    while not legal:
        r = float(dice.roll(1, 6) + 4) / 4
        legal = True
        for e in existingOrbits:
            if e == r:
                legal = False
    existingOrbits.append(r)
    return r

def GenerateGasGiantInnerMoonOrbitRadius():
    return float(dice.roll(1, 6) + 4) / 4

def GenerateGasGiantMajorMoonOrbitRadius(existingOrbits):
    legal = False
    while not legal:
        r = dice.roll(3, 6) + 3
        if r >= 15:
            r = r + dice.roll(2, 6)
        rad = float(r) / 2
        legal = True
        for e in existingOrbits:
            if e == rad:
                legal = False
    existingOrbits.append(rad)
    return rad

def GenerateGasGiantOuterMoonOrbitRadius(existingOrbits):
    legal = False
    while not legal:
        r = dice.roll(3, 6) + 3
        if r >= 15:
            r = r + dice.roll(2, 6)
        rad = float(r) * 3.34
        legal = True
        for e in existingOrbits:
            if e == rad:
                legal = False
    existingOrbits.append(rad)
    return rad


def GetGasGiantInnerMoonMod(r):
    mod = 0
    if r <= 0.1:
        mod = -10
    elif r <= 0.5:
        mod = -8
    elif r <= 0.75:
        mod = -6
    elif r <= 1.5:
        mod = -3
    return mod

def GetGasGiantMajorMoonMod(r):
    mod = 0
    if r <= 0.5:
        mod = -5
    elif r <= 0.75:
        mod = -4
    elif r <= 1.5:
        mod = -1
    return mod

def GetGasGiantOuterMoonMod(r):
    mod = 0
    if r <= 0.75:
        mod = -5
    elif r <= 1.5:
        mod = -4
    elif r <= 3.0:
        mod = -1
    return mod

def GetTerrestrialMajorMoonMod(r, t):
    mod = 0
    if r <= 0.75:
        mod = -3
    elif r <= 1.5:
        mod = -1
    if t == "Tiny":
        mod = mod - 2
    elif t == "Small":
        mod = mod - 1
    elif t == "Large":
        mod = mod + 1
    return mod

def GenerateWorlds(parentStar, worlds):
    arrangement = GenerateGasGiantArrangement(parentStar)
    placements = GeneratePlacements(parentStar, arrangement)
    for placement in placements:
        if placement["Type"] == "Tiny" or placement["Type"] == "Small" or placement["Type"] == "Standard" or placement["Type"] == "Large":
            w = world.TerrestrialWorld(placement["Type"], parentStar)
            mod = 0
            if arrangement == "Conventional":
                mod = -6 
            eccentricity = GetWorldEccentricity(mod)
            o = orbit.Orbit(parentStar, w, placement["Radius"], eccentricity)
            parentStar.AddOrbiter(o)
            w.SetOrbit(o)
            w.GenerateBasic()
            """ Moons """
            majorMoons = 0
            minorMoons = 0
            if placement["Radius"] <= 0.5:
                majorMoons = 0
                minorMoons = 0
            else:
                mod = GetTerrestrialMajorMoonMod(placement["Radius"], placement["Type"])
                majorMoons = max(dice.roll(1, 6) + mod - 4, 0)
                if majorMoons == 0:
                    minorMoons = max(dice.roll(1, 6) + mod - 2, 0)
            existingOrbit = 0
            for i in range(0, majorMoons):
                t = GenerateMoonType(placement["Type"])    
                m = world.TerrestrialWorld(t, parentStar, parentWorld = w)
                r = GenerateTerrestrialMajorMoonOrbitRadius(t, placement["Type"], existingOrbit)
                existingOrbit = r
                radius = r * w.GetDiameter()
                o = orbit.Orbit(w, m, radius, 0, oType = "Lunar")
                m.SetOrbit(o)
                w.AddOrbiter(o)
                m.GenerateBasic()
            existingOrbits = []
            for i in range(0, minorMoons):
                m = world.Moonlet(parentStar, parentWorld = w)
                r = GenerateTerrestrialMinorMoonOrbitRadius(existingOrbits)
                radius = r * w.GetDiameter()
                o = orbit.Orbit(w, m, radius, 0, oType = "Lunar")
                m.SetOrbit(o)
                w.AddOrbiter(o)
                m.Generate()
                 
        elif placement["Type"] == "Gas Giant":
            w = world.GasGiant(parentStar)
            mod = 0
            eccentricity = GetWorldEccentricity(mod)
            o = orbit.Orbit(parentStar, w, placement["Radius"], eccentricity)
            w.SetOrbit(o)
            parentStar.AddOrbiter(o)
            w.GenerateBasic()            
            """ Inner Moons """
            innerMoons = max(dice.roll(2, 6) + GetGasGiantInnerMoonMod(placement["Radius"]), 0)
            w.SetNumInnerMoons(innerMoons)
            for i in range(0, innerMoons):
                m = world.Moonlet(parentStar, parentWorld = w)
                r = GenerateGasGiantInnerMoonOrbitRadius()
                radius = r * w.GetDiameter()
                o = orbit.Orbit(w, m, radius, 0, oType = "Lunar")
                m.SetOrbit(o)
                w.AddOrbiter(o)
                m.Generate()
            """ Major Moons """
            if placement["Radius"] <= 0.1:
                majorMoons = 0
            else:
                majorMoons = max(dice.roll(1, 6) + GetGasGiantMajorMoonMod(placement["Radius"]),  0)
            existingOrbits = []
            for i in range(0, majorMoons):
                t = GenerateMoonType("Gas Giant")    
                m = world.TerrestrialWorld(t, parentStar, parentWorld = w)
                r = GenerateGasGiantMajorMoonOrbitRadius(existingOrbits)
                radius = r * w.GetDiameter()
                o = orbit.Orbit(w, m, radius, 0, oType = "Lunar")
                m.SetOrbit(o)
                w.AddOrbiter(o)
                m.GenerateBasic()
            """ Outer Moons """
            if placement["Radius"] < 0.5:
                outerMoons = 0
            else:
                outerMoons = max(dice.roll(1, 6) + GetGasGiantOuterMoonMod(placement["Radius"]), 0)
            existingOrbits = []
            for i in range(0, innerMoons):
                m = world.Moonlet(parentStar, parentWorld = w)
                r = GenerateGasGiantOuterMoonOrbitRadius(existingOrbits)
                radius = r * w.GetDiameter()
                o = orbit.Orbit(w, m, radius, 0, oType = "Lunar")
                m.SetOrbit(o)
                w.AddOrbiter(o)
                m.Generate()

        elif placement["Type"] == "Belt":
            w = world.Belt(parentStar)
            mod = 0
            eccentricity = GetWorldEccentricity(mod)
            o = orbit.Orbit(parentStar, w, placement["Radius"], eccentricity)
            w.SetOrbit(o)
            parentStar.AddOrbiter(o)
            w.Generate()            

class System:
    def __init__(self):
        self.stars = []
        self.worlds = []
        self.age = 0.0

    def Generate(self):
        self.age = GenerateAge()
        GenerateStars(self.age, self.stars)
        for s in self.stars:
            GenerateWorlds(s, self.worlds)
              
    def __str__(self):
        primary = self.stars[0]
        return world.Banner() + "\n                     " + primary.__str__()
