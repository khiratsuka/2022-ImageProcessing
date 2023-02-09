import os
import cv2
import numpy as np


def mean(img, output_file):
    kernel = np.array([[1/25, 1/25, 1/25, 1/25, 1/25],
                       [1/25, 1/25, 1/25, 1/25, 1/25],
                       [1/25, 1/25, 1/25, 1/25, 1/25],
                       [1/25, 1/25, 1/25, 1/25, 1/25],
                       [1/25, 1/25, 1/25, 1/25, 1/25]])
    mean_img = cv2.filter2D(img, -1, kernel)
    cv2.imwrite(output_file, mean_img)


def gaussian(img, output_file):
    kernel = np.array([[1/256, 4/256, 6/256, 4/256, 1/256],
                       [4/256, 16/256, 24/256, 16/256, 4/256],
                       [6/256, 24/256, 36/256, 24/256, 6/256],
                       [4/256, 16/256, 24/256, 16/256, 4/256],
                       [1/256, 4/256, 6/256, 4/256, 1/256]])
    gaussian_img = cv2.filter2D(img, -1, kernel)
    cv2.imwrite(output_file, gaussian_img)


def direction(img, output_file):
    kernel = np.eye(5) / 5
    direction_img = cv2.filter2D(img, -1, kernel)
    cv2.imwrite(output_file, direction_img)


def median(img, output_file):
    median_img = cv2.medianBlur(img, ksize=3)
    cv2.imwrite(output_file, median_img)


if __name__ == '__main__' :
    result_folder = './result'
    if not os.path.exists(result_folder):
        os.makedirs(result_folder)

    img_file = './lena.bmp'
    img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)
    
    mean_output_file = 'lena_mean.bmp'
    mean_output_path = os.path.join(result_folder, mean_output_file)
    mean(img, mean_output_path)

    gaussian_output_file = 'lena_gaussian.bmp'
    gaussian_output_path = os.path.join(result_folder, gaussian_output_file)
    gaussian(img, gaussian_output_path)

    direction_output_file = 'lena_direction.bmp'
    direction_output_path = os.path.join(result_folder, direction_output_file)
    direction(img, direction_output_path)

    median_output_file = 'lena_median.bmp'
    median_output_path = os.path.join(result_folder, median_output_file)
    direction(img, median_output_path)