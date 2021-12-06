import os
import sys
from Utils import ReadFromFile

def CalculateHorizontalPosition(rawCommands):
    horizontalCommands = [int(command.split(' ')[1]) for command in rawCommands if 'forward' in command]

    return sum(horizontalCommands)

def CalculateVerticalPosition(rawCommands):
    depthIncreasesCommands = [int(command.split(' ')[1]) for command in rawCommands if 'down' in command]
    depthDecreasesCommands = [int(command.split(' ')[1]) for command in rawCommands if 'up' in command]

    return sum(depthIncreasesCommands) - sum(depthDecreasesCommands)

def CalculatePositionResult(rawCommands):
    return CalculateHorizontalPosition(rawCommands) * CalculateVerticalPosition(rawCommands)

test1CommandArray = [
'forward 5',
'down 5',
'forward 8',
'up 3',
'down 8',
'forward 2']

horizontalPositionTest = CalculateHorizontalPosition(test1CommandArray)
verticalPositionTest = CalculateVerticalPosition(test1CommandArray)
positionResultTest = CalculatePositionResult(test1CommandArray)

print('horizontal: ' + str(horizontalPositionTest))
print('vertical: ' + str(verticalPositionTest))
print('vertical: ' + str(positionResultTest))


challengeArray = ReadFromFile.ToStringArray(os.path.join(sys.path[0], 'input2.txt'))

challenge1Result = CalculatePositionResult(challengeArray)

print('challengeResult: ' + str(challenge1Result))
