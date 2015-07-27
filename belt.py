import dice
import world

class Belt(world.World):
    def __init__(self, parentStar):
        world.World.__init__(self, "Belt", parentStar)

    def GenerateDetails(self):
        r = dice.roll(3, 6)
        if r <= 3:
            self.overallValue = "Worthless"
            self.resourceValue = -5
        elif r <= 4:
            self.overallValue = "Very Scant"
            self.resourceValue = -4
        elif r <= 5:
            self.overallValue = "Scant"
            self.resourceValue = -3
        elif r <= 7:
            self.overallValue = "Very Poor"
            self.resourceValue = -2
        elif r <= 9:
            self.overallValue = "Poor"
            self.resourceValue = -1
        elif r <= 11:
            self.overallValue = "Average"
            self.resourceValue = 0
        elif r <= 13:
            self.overallValue = "Abundant"
            self.resourceValue = 1
        elif r <= 15:
            self.overallValue = "Very Abundant"
            self.resourceValue = 2
        elif r <= 16:
            self.overallValue = "Rich"
            self.resourceValue = 3
        elif r <= 17:
            self.overallValue = "Very Rich"
            self.resourceValue = 4
        else:
            self.overallValue = "Motherlode"
            self.resourceValue = 5

        self.habitability = 0
        self.affinity = self.resourceValue

    def GetAffinity(self):
        return self.affinity

    def ShowDetails(self):
        return "Vacuum     ----       ----       ----       ----       ----       ----       ----       ----       ----       ----       ----       ----       ----       %-3d %-3d %-3d" % \
             (self.habitability, self.resourceValue, self.affinity)
