import os
import sys
import array

def PrepareBingoFromFile(path):
    coordinates = []

    with open(path) as f:
        line = f.readline()
        while line:
            splittedLine = line.split()
            x1 = int(splittedLine[0].split(',')[0])
            y1 = int(splittedLine[0].split(',')[1])
            x2 = int(splittedLine[2].split(',')[0])
            y2 = int(splittedLine[2].split(',')[1])
            coordinates.append(((x1,y1),(x2,y2)))
            line = f.readline()


    return coordinates

def IsCoordinateHorizontal(coordinate):
    return coordinate[0][0] == coordinate[1][0]

def IsCoordinateVertical(coordinate):
    return coordinate[0][1] == coordinate[1][1]

def IsCoordinateDiagonal(coordinate):
    return abs(coordinate[0][0] - coordinate[1][0]) == abs(coordinate[0][1] - coordinate[1][1])

def GetHorizontalAndVerticalLines(coordinates: array):
    return [coordinate for coordinate in coordinates if IsCoordinateHorizontal(coordinate) or IsCoordinateVertical(coordinate)]

def GetHorizontalAndVerticalAndDiagonalLines(coordinates: array):
    return [coordinate for coordinate in coordinates if IsCoordinateHorizontal(coordinate) or IsCoordinateVertical(coordinate) or IsCoordinateDiagonal(coordinate)]


def CreateHydrothermalVentsDiagram(hydrothermalVentsCoordinates: array):
    x1list = [input[0][0] for input in hydrothermalVentsCoordinates]
    y1list = [input[0][1] for input in hydrothermalVentsCoordinates]
    x2list = [input[1][0] for input in hydrothermalVentsCoordinates]
    y2list = [input[1][1] for input in hydrothermalVentsCoordinates]
    horizontalSize = max(x1list + x2list) + 1
    verticalSize = max(y1list + y2list) + 1

    hydrothermalVentsDiagram = [[0 for x in range(horizontalSize)] for y in range(verticalSize)] 

    for coordinate in hydrothermalVentsCoordinates:
        if IsCoordinateHorizontal(coordinate):
            x = coordinate[0][0]
            y1 = coordinate[0][1]
            y2 = coordinate[1][1]
            for y in range(min(y1,y2), max(y1,y2) + 1):
                hydrothermalVentsDiagram[y][x] += 1

        if IsCoordinateVertical(coordinate):
            x1 = coordinate[0][0]
            x2 = coordinate[1][0]
            y = coordinate[0][1]
            for x in range(min(x1,x2), max(x1,x2) + 1):
                hydrothermalVentsDiagram[y][x] += 1
        
        if IsCoordinateDiagonal(coordinate):
            x1 = coordinate[0][0]
            x2 = coordinate[1][0]
            y1 = coordinate[0][1]
            y2 = coordinate[1][1]
            xSpan = []
            if x1 <= x2:
                xSpan = [*range(x1, x2 + 1)]
            else:
                xSpan = [*range(x1, x2 -1, -1)]
            ySpan = []
            if y1 <= y2:
                ySpan = [*range(y1, y2 + 1)]
            else:
                ySpan = [*range(y1, y2 -1, -1)]

            for n in range(len(xSpan)):
                hydrothermalVentsDiagram[ySpan[n]][xSpan[n]] += 1

    return hydrothermalVentsDiagram

def GetNumberOfOverlaps(diagram):
    overlaps = 0
    for line in diagram:
        for point in line:
            if point > 1:
                overlaps += 1

    return overlaps


test1Setup = PrepareBingoFromFile(os.path.join(sys.path[0], 'inputTest.txt'))
test1HVLines = GetHorizontalAndVerticalLines(test1Setup)
test1Diagram = CreateHydrothermalVentsDiagram(test1HVLines)
test1Overlaps = GetNumberOfOverlaps(test1Diagram)

print(test1Overlaps)

challenge1Setup = PrepareBingoFromFile(os.path.join(sys.path[0], 'input5.txt'))
challenge1HVLines = GetHorizontalAndVerticalLines(challenge1Setup)
challenge1Diagram = CreateHydrothermalVentsDiagram(challenge1HVLines)
challenge1Overlaps = GetNumberOfOverlaps(challenge1Diagram)

print(challenge1Overlaps)

test2HVDLines = GetHorizontalAndVerticalAndDiagonalLines(test1Setup)
test2Diagram = CreateHydrothermalVentsDiagram(test2HVDLines)
test2Overlaps = GetNumberOfOverlaps(test2Diagram)

print(test2Overlaps)

challenge2HVDLines = GetHorizontalAndVerticalAndDiagonalLines(challenge1Setup)
challenge2Diagram = CreateHydrothermalVentsDiagram(challenge2HVDLines)
challenge2Overlaps = GetNumberOfOverlaps(challenge2Diagram)

print(challenge2Overlaps)
