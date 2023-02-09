import os

import cv2
import numpy as np

import assignmentPGM as ap


def fourierTransform():
    # 使うファイルがなければ生成する
    file_name = './result/sinamp30row100hzcol50hz.pgm'
    if not os.path.exists(file_name):
        ap.SinAmp30Row100HzCol50Hz(file_name)

    # グレイスケールで読み込み, imgはnumpy.ndarray
    img = cv2.imread(file_name, cv2.IMREAD_GRAYSCALE)

    # FFT実行、中央に値を寄せて周波数成分の大きさを確認
    fourier_img = np.fft.fft2(img)
    fourier_img_shift = np.fft.fftshift(fourier_img)
    fourier_freq_img = 20 * np.log(np.absolute(fourier_img_shift))

    cv2.imwrite('./result/2d_fourier_transform.jpg', fourier_freq_img)
    cv2.imshow('fourier img', fourier_freq_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def highPassPGM():
    # 使うファイルがなければ生成する
    file_name = './result/sinamp30row100hzcol50hz.pgm'
    if not os.path.exists(file_name):
        ap.SinAmp30Row100HzCol50Hz(file_name)

    # グレイスケールで読み込み, imgはnumpy.ndarray
    img = cv2.imread(file_name, cv2.IMREAD_GRAYSCALE)

    # FFT実行、中央に値を寄せて周波数成分の大きさを確認
    fourier_img = np.fft.fft2(img)
    fourier_img_shift = np.fft.fftshift(fourier_img)

    # ローパス・ハイパスフィルタの作成
    low_filter = np.full(img.shape, 0, dtype=np.float64)
    circle_center = (img.shape[0] // 2, img.shape[1] // 2)
    circle_r = 30
    cv2.circle(low_filter, circle_center, circle_r, color=255, thickness=-1)

    high_filter = np.full(img.shape, 255, dtype=np.float64)
    circle_center = (img.shape[0] // 2, img.shape[1] // 2)
    circle_r = 30
    cv2.circle(high_filter, circle_center, circle_r, color=0, thickness=-1)

    # フィルタをかけて画像を戻す
    fourier_low_filter_img_shift = np.copy(fourier_img_shift)
    fourier_high_filter_img_shift = np.copy(fourier_img_shift)
    for i in range(256):
        for j in range(256):
            if low_filter[i][j] == 0:
                fourier_low_filter_img_shift[i][j] *= 0
    for i in range(256):
        for j in range(256):
            if high_filter[i][j] == 0:
                fourier_high_filter_img_shift[i][j] *= 0

    fourier_low_filter_img = np.fft.fftshift(fourier_low_filter_img_shift)
    fourier_high_filter_img = np.fft.fftshift(fourier_high_filter_img_shift)
    filter_low_img = np.fft.ifft2(fourier_low_filter_img).real
    filter_high_img = np.fft.ifft2(fourier_high_filter_img).real

    cv2.imwrite('./result/low_filter_pgm.jpg', filter_low_img)
    cv2.imwrite('./result/high_filter_pgm.jpg', filter_high_img)
    cv2.destroyAllWindows()


def highPassLenna():
    # 使うファイルがなければ生成する
    file_name = './result/LENNA.bmp'

    # グレイスケールで読み込み, imgはnumpy.ndarray
    img = cv2.imread(file_name, cv2.IMREAD_GRAYSCALE)

    # FFT実行、中央に値を寄せて周波数成分の大きさを確認
    fourier_img = np.fft.fft2(img)
    fourier_img_shift = np.fft.fftshift(fourier_img)

    # ローパス・ハイパスフィルタの作成
    low_filter = np.full(img.shape, 0, dtype=np.float64)
    circle_center = (img.shape[0] // 2, img.shape[1] // 2)
    circle_r = 30
    cv2.circle(low_filter, circle_center, circle_r, color=255, thickness=-1)

    high_filter = np.full(img.shape, 255, dtype=np.float64)
    circle_center = (img.shape[0] // 2, img.shape[1] // 2)
    circle_r = 30
    cv2.circle(high_filter, circle_center, circle_r, color=0, thickness=-1)

    # フィルタをかけて画像を戻す
    fourier_low_filter_img_shift = np.copy(fourier_img_shift)
    fourier_high_filter_img_shift = np.copy(fourier_img_shift)
    for i in range(256):
        for j in range(256):
            if low_filter[i][j] == 0:
                fourier_low_filter_img_shift[i][j] *= 0
    for i in range(256):
        for j in range(256):
            if high_filter[i][j] == 0:
                fourier_high_filter_img_shift[i][j] *= 0

    fourier_low_filter_img = np.fft.fftshift(fourier_low_filter_img_shift)
    fourier_high_filter_img = np.fft.fftshift(fourier_high_filter_img_shift)
    filter_low_img = np.fft.ifft2(fourier_low_filter_img).real
    filter_high_img = np.fft.ifft2(fourier_high_filter_img).real

    cv2.imwrite('./result/high_pass_low_filter_lenna.jpg', filter_low_img)
    cv2.imwrite('./result/high_pass_high_filter_lenna.jpg', filter_high_img)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    fourierTransform()
    highPassPGM()
    highPassLenna()
