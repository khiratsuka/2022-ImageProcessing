import math

from pgm import PGMData

# ヘッダ部の記述内容
magic_number = 'P2'
comment = '#Created by Python'
width = 256
height = 256
bit = 255


def SinAmp30Row100HzCol50Hz(filename):
    sinamp30row100hzcol50hz_pgm = PGMData(magic_number, comment, width, height, bit)

    for i in range(height):
        for j in range(width):
            col_data = round(30*math.sin(math.radians(2*math.pi*100*i)))
            row_data = round(30*math.sin(math.radians(2*math.pi*50*j)))
            sinamp30row100hzcol50hz_pgm.colorOfPixel(j, i, row_data+col_data+100)

    sinamp30row100hzcol50hz_pgm.outputPGM(filename)
