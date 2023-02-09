import os
import cv2


def main():
    result_folder = './result'
    img_file = 'lena.bmp'
    img_path = os.path.join(result_folder, img_file)

    img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)
    
    #輝度の最大値・最小値を求める
    img_max = int(img.max())
    img_min = int(img.min())

    #コントラストの計算
    img_contrast = (img_max - img_min) / (img_max + img_min)

    print('{} contrast is {:.3}'.format(img_file, img_contrast))

if __name__ == '__main__' :
    main()