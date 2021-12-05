import os
import sys
from Utils import ReadFromFile

def CheckDepthIncreases(measurements):
    increases = 0
    currentMeaseurement = measurements[0]

    for measurement in measurements[1:]:
        if (measurement > currentMeaseurement):
            increases += 1
        
        currentMeaseurement = measurement
    
    return increases

def CheckSlidingWindowIncreases(measurements):
    increases = 0
    currentWindowMeasurement = measurements[0] + measurements[1] + measurements[2]

    for i in range(len(measurements[1:-2])):
        windowMeasurement = measurements[i+1] + measurements[i+2] + measurements[i+3]
        if (windowMeasurement > currentWindowMeasurement):
            increases += 1
        
        currentWindowMeasurement = windowMeasurement
    
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

test1Result = CheckDepthIncreases(testArray)

print(test1Result)

challengeArray = ReadFromFile.ToIntArray(os.path.join(sys.path[0], 'input1.txt'))

challenge1Result = CheckDepthIncreases(challengeArray)

print(challenge1Result)

test2Result = CheckSlidingWindowIncreases(testArray)
print(test2Result)

challenge2Result = CheckSlidingWindowIncreases(challengeArray)

print(challenge2Result)