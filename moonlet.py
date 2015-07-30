import world

class Moonlet(world.World):
    def __init__(self, parentStar, parentWorld):
        world.World.__init__(self, "Moonlet", parentStar)
        self.parentWorld = parentWorld

    def GetIsAMoon(self):
        return True

    def ShowDetails(self):
        return "Vacuum     ----       ----       ----       ----       ----       ----       ----       ----       ----       ----       ----       ----       ----       ----       ----       ----"
