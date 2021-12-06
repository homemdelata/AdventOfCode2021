import os
import sys
from Utils import ReadFromFile

def ConvertBase2StringArrayToIntArray(base2StringArray):
    intArray = [int(base2String, 2) for base2String in base2StringArray]

    return intArray

def CheckGammaRate(diagnostics):
    highestBitSize = max(diagnostics).bit_length()

    gammaRate = 0

    for n in range(highestBitSize):
        bitNumber = (2 ** n)
        arr = [diagnostic & bitNumber for diagnostic in diagnostics]

        if arr.count(bitNumber) < len(arr) / 2:
            bitNumber = 0

        gammaRate = gammaRate | bitNumber

    return gammaRate

def CheckEpsilonRate(diagnostics):
    highestBitSize = max(diagnostics).bit_length()

    epsilonRate = 0

    for n in range(highestBitSize):
        bitNumber = (2 ** n)
        arr = [diagnostic & bitNumber for diagnostic in diagnostics]

        if arr.count(bitNumber) > len(arr) / 2:
            bitNumber = 0

        epsilonRate = epsilonRate | bitNumber

    return epsilonRate

def CheckPowerConsumption(diagnostics):
    return CheckGammaRate(diagnostics) * CheckEpsilonRate(diagnostics)

test1Array = [
'00100',
'11110',
'10110',
'10111',
'10101',
'01111',
'00111',
'11100',
'10000',
'11001',
'00010',
'01010']

test1GammaRate = CheckGammaRate(ConvertBase2StringArrayToIntArray(test1Array))
print('Gamma Rate Test 1: ' + str(test1GammaRate))

test1EpsilonRate = CheckEpsilonRate(ConvertBase2StringArrayToIntArray(test1Array))
print('Epsilon Rate Test 1: ' + str(test1EpsilonRate))

test1PowerConsumption = CheckPowerConsumption(ConvertBase2StringArrayToIntArray(test1Array))
print('Power Consumption Test 1: ' + str(test1PowerConsumption))

challengeArray = ReadFromFile.ToStringArray(os.path.join(sys.path[0], 'input3.txt'))

challenge1PowerConsumption = CheckPowerConsumption(ConvertBase2StringArrayToIntArray(challengeArray))
print('Power Consumption Challenge 1: ' + str(challenge1PowerConsumption))