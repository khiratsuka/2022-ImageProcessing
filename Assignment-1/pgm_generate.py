import assignmentPGM as ap

def main():
    ap.All100('./result/all100.pgm')
    ap.Left0toRight255('./result/left0toright255.pgm')
    ap.Sin8HzAmp80Col('./result/sin8hzamp80col.pgm')
    ap.Cos32HzAmp70Row('./result/cos32hzamp70raw.pgm')
    ap.Square8HzAmp30RowCol('./result/square8hzamp30rowcol.pgm')
    

        
if __name__ == '__main__':
    main()