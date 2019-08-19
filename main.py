from methods import *
import os


def executeDrawingTool():
    # open input file with comands
    # draw comands
    # write result to output file

    os.remove('output.txt')
    with open('input.txt', 'r') as comands:
        canvas = ''  # init canvas
        resultCanvas = ''
        for line in comands:
            comand = line.split()
            if comand[0] == 'C':
                canvas = initEmptyCanvas(comand)
            else:
                if len(canvas) != 0:
                    canvas = executeComand(canvas, comand)

            # write canvas after some comand to the output file
            with open('output.txt', 'a') as outputFile:
                outputFile.writelines(matrixToString(canvas))


# execute draw comands
executeDrawingTool()