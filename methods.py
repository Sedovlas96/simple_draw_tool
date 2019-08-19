import numpy as np


def generateMatrix(row, col, val=' '):
    # generate a matrix of dimension (row x col) with value val
    return np.array([[val] * col for i in range(row)])


def matrixToString(matrix):
    # convert matrix to text

    resultString = ''
    for row in matrix:
        resultString += ''.join(row) + '\n'
    return resultString


def getSortedCoordinates(coordinates):
    # sort coordinates from min to max by x and y

    x1, x2 = sorted([coordinates[0], coordinates[2]])
    y1, y2 = sorted([coordinates[1], coordinates[3]])
    return [x1, y1, x2, y2]


def drawLine(canvas, coordinates, drawChar='x', isCanvas=False):
    # draw line from (x1, y1) to (x2, y2)
    # draw ONLY vertical and horizontal line

    x1, y1, x2, y2 = getSortedCoordinates(coordinates)
    # watching that coordinates aren't draw on canvas
    if isCanvas == False:
        x1, x2 = max(x1, 1), min(x2, len(canvas[0]) - 1)
        y1, y2 = max(y1, 1), min(y2, len(canvas) - 1)
    canvas[y1:y2 + 1, x1:x2 + 1] = drawChar
    return canvas


def drawRectangle(canvas, coordinates, drawChar='x'):
    # draw rectangle from point (x1, y1) to (x2, y2)

    x1, y1, x2, y2 = coordinates
    drawLine(canvas, [x1, y1, x2, y1], drawChar)   # up
    drawLine(canvas, [x2, y1, x2, y2], drawChar)   # right
    drawLine(canvas, [x2, y2, x1, y2], drawChar)   # down
    drawLine(canvas, [x1, y2, x1, y1], drawChar)   # left
    return canvas


def floodFillingArea(canvas, x, y, oldColor, newColor):
    # fill the entire area connected to (x,y) with "color" c

    if canvas[y, x] != oldColor:
        # print(matrixToString(canvas))
        return canvas
    canvas[y, x] = newColor
    floodFillingArea(canvas, x + 1, y, oldColor, newColor)  # up
    floodFillingArea(canvas, x - 1, y, oldColor, newColor)  # down
    floodFillingArea(canvas, x, y + 1, oldColor, newColor)  # right
    floodFillingArea(canvas, x, y - 1, oldColor, newColor)  # left


def bucketFill(canvas, x, y, color):
    # select color of the point (x, y) and call procedure that floodfill area

    oldColor = canvas[y, x]
    if oldColor != '-' and oldColor != '|':
        floodFillingArea(canvas, x, y, oldColor, color)
    return canvas


def initEmptyCanvas(comand):
    # initialize empty matrix by some comand

    width, height = int(comand[1]) + 2, int(comand[2]) + 2
    canvas = generateMatrix(height, width)
    drawLine(canvas, [0, 0, width - 1, 0], '-', True)                      # up
    drawLine(canvas, [0, height - 1, width - 1, height - 1], '-', True)    # down
    drawLine(canvas, [0, 1, 0, height - 2], '|', True)                     # left
    drawLine(canvas, [width - 1, 1, width - 1, height - 2], '|', True)     # right
    return canvas


def executeComand(canvas, comand):
    # select type of comand and draw figure by comand

    comandType = comand[0]
    if comandType == 'L':
        coordinates = np.array(comand[1:]).astype(int)
        drawLine(canvas, coordinates)
    elif comandType == 'R':
        coordinates = np.array(comand[1:]).astype(int)
        drawRectangle(canvas, coordinates)
    elif comandType == 'B':
        x, y, color = int(comand[1]), int(comand[2]), comand[3]
        bucketFill(canvas, x, y, color)

    return canvas
