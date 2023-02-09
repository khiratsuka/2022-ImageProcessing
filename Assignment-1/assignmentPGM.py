import math
from scipy import signal
from pgm import PGMData


# ヘッダ部の記述内容
magic_number = 'P2'
comment = '#Created by Python'
width = 256
height = 256
bit = 255


def All100(filename):
    all100_pgm = PGMData(magic_number, comment, width, height, bit)
    
    for i in range(height):
        for j in range(width):
            all100_pgm.colorOfPixel(j, i, 100)
    
    all100_pgm.outputPGM(filename)


def Left0toRight255(filename):
    left0toright255_pgm = PGMData(magic_number, comment, width, height, bit)

    for i in range(height):
        for j in range(width):
            left0toright255_pgm.colorOfPixel(j, i, j)
    
    left0toright255_pgm.outputPGM(filename)


def Sin8HzAmp80Col(filename):
    sin8hzamp80col_pgm = PGMData(magic_number, comment, width, height, bit)

    for i in range(height):
        for j in range(width):
            data = round(80*math.sin(math.radians(2*math.pi*8*j))+100)
            sin8hzamp80col_pgm.colorOfPixel(j, i, data)
    
    sin8hzamp80col_pgm.outputPGM(filename)


def Cos32HzAmp70Row(filename):
    cos32hzamp70row_pgm = PGMData(magic_number, comment, width, height, bit)

    for i in range(height):
        for j in range(width):
            data = round(70*math.cos(math.radians(2*math.pi*32*i))+100)
            cos32hzamp70row_pgm.colorOfPixel(j, i, data)
    
    cos32hzamp70row_pgm.outputPGM(filename)


def Square8HzAmp30RowCol(filename):
    square8hzamp30rowcol_pgm = PGMData(magic_number, comment, width, height, bit)
    
    for i in range(height):
        for j in range(width):
            row_data = round(30*signal.square(math.radians(2*math.pi*8*i)))
            col_data = round(30*signal.square(math.radians(2*math.pi*8*j)))
            square8hzamp30rowcol_pgm.colorOfPixel(j, i, row_data+col_data+100)

    square8hzamp30rowcol_pgm.outputPGM(filename)