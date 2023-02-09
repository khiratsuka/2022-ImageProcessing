import os

import cv2
import numpy as np


def differential_height(img, output_file):
    kernel = np.array([[0, -1, 0],
                       [0, 0, 0],
                       [0, 1, 0]])
    dif_h_img = cv2.filter2D(img, -1, kernel)
    cv2.imwrite(output_file, dif_h_img)


def differential_width(img, output_file):
    kernel = np.array([[0, 0, 0],
                       [-1, 0, 1],
                       [0, 0, 0]])
    dif_w_img = cv2.filter2D(img, -1, kernel)
    cv2.imwrite(output_file, dif_w_img)


def laplacian(img, output_file):
    kernel = np.array([[1, 1, 1],
                       [1, -8, 1],
                       [1, 1, 1]])
    laplacian_img = cv2.filter2D(img, cv2.CV_64F, kernel)
    cv2.imwrite(output_file, laplacian_img)


def sharpening(img, output_file):
    kernel = np.array([[-1, -1, -1],
                       [-1, 9, -1],
                       [-1, -1, -1]])
    sharpening_img = cv2.filter2D(img, cv2.CV_64F, kernel)
    cv2.imwrite(output_file, sharpening_img)


if __name__ == '__main__':
    result_folder = './result'
    if not os.path.exists(result_folder):
        os.makedirs(result_folder)

    img_file = './lena.bmp'
    img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)

    dif_h_output_file = 'lena_dif_h.bmp'
    dif_h_output_path = os.path.join(result_folder, dif_h_output_file)
    differential_height(img, dif_h_output_path)

    dif_w_output_file = 'lena_dif_w.bmp'
    dif_w_output_path = os.path.join(result_folder, dif_w_output_file)
    differential_width(img, dif_w_output_path)

    laplacian_output_file = 'lena_laplacian.bmp'
    laplacian_output_path = os.path.join(result_folder, laplacian_output_file)
    laplacian(img, laplacian_output_path)

    sharpening_output_file = 'lena_sharpening.bmp'
    sharpening_output_path = os.path.join(result_folder, sharpening_output_file)
    sharpening(img, sharpening_output_path)
