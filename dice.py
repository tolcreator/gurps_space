import random

def roll(numdice, sides):
    random.seed()
    total = 0
    for x in range(numdice):
        total += random.randint(1, sides)
    return total

def explode(numdice, sides):
    random.seed()
    total = 0
    for x in range(numdice):
        done = False
        while not done:
            roll = random.randint(1, sides)
            if not roll == sides:
                done = True
            total = total + roll
    return total

class Dice:
    def __init__(self):
        random.seed()

    def roll(self, numdice, sides):
        total = 0
        for x in range(numdice):
            total += random.randint(1, sides)
        return total

def test(sides, times):
    gauss = {}
    for x in range(times):
        r = explode(1, sides)
        if r in gauss.keys():
            gauss[r] = gauss[r] + 1
        else:
            gauss[r] = 1
    for key in sorted(gauss.keys()):
        print "%02d: %d" % (key, gauss[key])
