import os
import sys
import array
from Utils import ReadFromFile

def GetInitialAgesFromFile(fileName: str):
    return [int(n) for n in ReadFromFile.ToStringArray(os.path.join(sys.path[0], fileName))[0].split(',')]


def CalculateLanternFishCount(numberOfDays: int, initialAges: array):
    lanternFishes = initialAges

    for day in range(numberOfDays):
        nextDay = [n-1 for n in lanternFishes]
        numberOfNew = nextDay.count(-1)
        nextDay.extend([8 for n in range(numberOfNew)])
        lanternFishes = [lanternFish if lanternFish >= 0 else 6 for lanternFish in nextDay]


    return len(lanternFishes)


testInitialAges = GetInitialAgesFromFile('inputTest.txt')
test18Days = CalculateLanternFishCount(18, testInitialAges)
test80Days = CalculateLanternFishCount(80, testInitialAges)

print(test18Days)
print(test80Days)

challengeInitialAges = GetInitialAgesFromFile('input6.txt')
challenge80Days = CalculateLanternFishCount(80, challengeInitialAges)

print(challenge80Days)