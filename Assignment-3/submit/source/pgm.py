class PGMData():
    def __init__(self, magic_number, comment, width, height, color_bit):
        # ヘッダ部
        self.magic_number = magic_number
        self.comment = comment
        self.width = str(width)
        self.height = str(height)
        self.color_bit = str(color_bit)
        
        #データ部
        self.img = []
        for i in range(int(self.width)):
            self.img.append([])
        for i in range(int(self.width)):
            for j in range(int(self.height)):
                self.img[i].append(str(0))
    
    def colorOfPixel(self, width, height, data):
        data = str(data)
        self.img[height][width] = data

    def outputPGM(self, filename):
        #画像データを出力
        with open(filename, 'w') as f:
            # ヘッダ書き込み
            f.write(self.magic_number + '\n')  # マジックナンバー
            f.write(self.comment + '\n')       # コメント
            scale = [self.width, self.height]  # 画像の大きさを1行にする
            scale = ' '.join(scale)
            f.write(scale + '\n')              # 画像の大きさ
            f.write(self.color_bit + '\n')     # ビット

            #データ書き込み
            for i in range(int(self.height)):
                col_data = ' '.join(self.img[i])
                f.write(col_data + '\n')