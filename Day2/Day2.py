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

def CalculatePositionWithAim(rawCommands):
    aim = 0
    depth = 0
    horizontal = 0
    commands = [[command.split(' ')[0],int(command.split(' ')[1])] for command in rawCommands]

    for command in commands:
        if command[0] == 'forward':
            horizontal += command[1]
            depth += aim * command[1]
        elif command[0] == 'down':
            aim += command[1]
        elif command[0] == 'up':
            aim -= command[1]
    
    return horizontal * depth


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
print('position 1: ' + str(positionResultTest))


challengeArray = ReadFromFile.ToStringArray(os.path.join(sys.path[0], 'input2.txt'))

challenge1Result = CalculatePositionResult(challengeArray)

print('challengeResult 1: ' + str(challenge1Result))

test2Result = CalculatePositionWithAim(test1CommandArray)
print('position 2: ' + str(test2Result))

challenge2Result = CalculatePositionWithAim(challengeArray)
print('challengeResult 2: ' + str(challenge2Result))

