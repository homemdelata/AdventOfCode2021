import os
import sys
from Utils import ReadFromFile

def CheckDepthIncreases(measurements):
    increases = -1
    currentMeaseurement = -1

    for measurement in measurements:
        if (measurement > currentMeaseurement):
            increases += 1
        
        currentMeaseurement = measurement
    
    return increases

testArray = [199
,200
,208
,210
,200
,207
,240
,269
,260
,263]

result = CheckDepthIncreases(testArray)

print(result)

challengeArray = ReadFromFile.ToIntArray(os.path.join(sys.path[0], 'input1.txt'))

challengeResult = CheckDepthIncreases(challengeArray)

print(challengeResult)