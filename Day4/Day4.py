import os
import sys
import array
from types import ClassMethodDescriptorType
from BingoBoard import BingoBoard
from BingoSetup import BingoSetup
from Utils import ReadFromFile

def PrepareBingoFromFile(path):
    bingoSetup = BingoSetup()
    
    with open(path) as f:
        bingoSetup.drawnNumbers = [int(n) for n in f.readline().split(',')]

        line = f.readline()
        bingoBoard = None

        while line:
            if line.strip() == '':
                if bingoBoard:
                    bingoSetup.AddBoard(bingoBoard)
                bingoBoard = BingoBoard()
            else:
                bingoBoard.AddLine([int(number) for number in line.split()])

            line = f.readline()

        bingoSetup.AddBoard(bingoBoard)

    return bingoSetup

def RunBingo(bingoSetup: BingoSetup):
    for n in range(5, len(bingoSetup.drawnNumbers)):
        for board in bingoSetup.boards:
            rowResult = CheckRows(bingoSetup.drawnNumbers[:n], board)
            colResult = CheckColumns(bingoSetup.drawnNumbers[:n], board)
            if len(rowResult) == 5 or len(colResult) == 5:
                return (board, bingoSetup.drawnNumbers[:n])
    return None

def RunBingoForLast(bingoSetup: BingoSetup):
    boards = bingoSetup.boards.copy()
    lastWon = None
    for n in range(5, len(bingoSetup.drawnNumbers)):
        for board in boards:
            rowResult = CheckRows(bingoSetup.drawnNumbers[:n], board)
            colResult = CheckColumns(bingoSetup.drawnNumbers[:n], board)
            if len(rowResult) == 5 or len(colResult) == 5:
                lastWon = (board, bingoSetup.drawnNumbers[:n])
                boards.remove(board)
    return lastWon

def CheckRows(drawnNumbers: array, board: BingoBoard):
    resultLine = []
    for row in board.lines:
        resultLine = [k for k in row if k in drawnNumbers]
        if len(resultLine) == 5:
            break
    
    return resultLine

def CheckColumns(drawnNumbers: array, board: BingoBoard):
    resultColumn = []
    for n in range(5):
        column = [col[n] for col in board.lines]
        resultColumn = [k for k in column if k in drawnNumbers]
        if len(resultColumn) == 5:
            break
    
    return resultColumn

def CalculateBingoScore(board: BingoBoard, drawnNumbers: array):
    unmarkedNumbers = []
    for row in board.lines:
        resultLine = [k for k in row if k not in drawnNumbers]
        unmarkedNumbers = unmarkedNumbers + resultLine
    
    sumOfUnmarkedNumbers = sum(unmarkedNumbers)
    lastDrawnNumber = drawnNumbers[-1]

    return sumOfUnmarkedNumbers * lastDrawnNumber


test1BingoSetup = PrepareBingoFromFile(os.path.join(sys.path[0], 'inputTest.txt'))
test1BingoResult = RunBingo(test1BingoSetup)
test1BingoScore = CalculateBingoScore(test1BingoResult[0], test1BingoResult[1])

print(test1BingoScore)


challenge1BingoSetup = PrepareBingoFromFile(os.path.join(sys.path[0], 'input4.txt'))
challenge1BingoResult = RunBingo(challenge1BingoSetup)
challenge1BingoScore = CalculateBingoScore(challenge1BingoResult[0], challenge1BingoResult[1])

print(challenge1BingoScore)


test2BingoSetup = PrepareBingoFromFile(os.path.join(sys.path[0], 'inputTest.txt'))
test2BingoResult = RunBingoForLast(test2BingoSetup)
test2BingoScore = CalculateBingoScore(test2BingoResult[0], test2BingoResult[1])

print(test2BingoScore)

challenge2BingoSetup = PrepareBingoFromFile(os.path.join(sys.path[0], 'input4.txt'))
challenge2BingoResult = RunBingoForLast(challenge2BingoSetup)
challenge2BingoScore = CalculateBingoScore(challenge2BingoResult[0], challenge2BingoResult[1])

print(challenge2BingoScore)