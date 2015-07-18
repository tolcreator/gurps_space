import dice
import star
import orbit

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

class System:
    def __init__(self):
        self.stars = []
        self.orbits = []

    def Generate(self):
        self.age = self.GenerateAge()
        numStars = self.GenerateNumStars()
        """ Primary Star """
        primaryMass = self.GeneratePrimaryMass()
        primary = star.Star(primaryMass, self.age)
        primary.Generate()
        self.stars.append(primary)

        """ Companions? """
        minRadius = 0
        mod = 0
        for x in range(1, numStars):
            """ The mass of the primary may have changed during generation """
            companionMass = self.GenerateCompanionMass(primary.GetMass())
            companion = star.Star(companionMass, self.age)
            companion.Generate()
            self.stars.append(companion)
            details = self.GenerateCompanionOrbit(primary, mod, minRadius, 0)
            myOrbit = orbit.Orbit(primary, companion, details["radius"], details["eccentricity"])
            minRadius = myOrbit.GetMaxSeparation() * 3
            self.orbits.append(myOrbit)
            primary.AddOrbiter(myOrbit)
            companion.SetOrbit(myOrbit)
            mod = 6
            """ Check for distant companion """
            r = dice.roll(3, 6)
            if details["separation"] == "Distant" and r >= 11:
                """ The companion has a companion """
                distantMass = self.GenerateCompanionMass(companionMass)
                distant = star.Star(distantMass, self.age)
                distant.Generate()
                self.stars.append(distant)
                maxRadius = myOrbit.GetMinSeparation() / 3
                details = self.GenerateCompanionOrbit(distant, 0, 0, maxRadius)
                myOrbit = orbit.Orbit(companion, distant, details["radius"], details["eccentricity"])
                self.orbits.append(myOrbit)
                companion.AddOrbiter(myOrbit)
                distant.SetOrbit(myOrbit)

    def GenerateCompanionOrbit(self, primary, separationMod, minRadius, maxRadius):
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

    def GeneratePrimaryMass(self):
        f = dice.roll(3, 6)
        s = dice.roll(3, 6)
        return stellarMassTable[f][s]

    def GenerateCompanionMass(self, primaryMass):
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

    def GenerateNumStars(self):
        d = dice.roll(3, 6)
        if d <= 10:
            return 1
        if d <= 15:
            return 2
        return 3

    def GenerateAge(self):
        p = dice.roll(3, 6)
        entry = stellarAgeTable[p]
        a = dice.roll(1, 6) - 1
        b = dice.roll(1, 6) - 1
        return entry["base"] + (entry["stepa"] * a) + (entry["stepb"] * b)
            
