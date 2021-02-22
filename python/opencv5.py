import cv2
import numpy as np

img = cv2.imread("makeup.jpg") # here change "makeup.jpg" to your image file name


height, width, _ = img.shape
for size in range(min(height, width), 4, -1):
    matrix_size = size
    blank = np.zeros((height, width, 3), dtype=np.uint8)
    blank.fill(255)

    for col in range(0, width, matrix_size):
        for row in range(0, height, matrix_size):

            img_matrix_blue = img[row:row+matrix_size, col:col+matrix_size, 0]
            b = np.average(img_matrix_blue)
            img_matrix_green = img[row:row+matrix_size, col:col+matrix_size, 1]
            g = np.average(img_matrix_green)
            img_matrix_red = img[row:row+matrix_size, col:col+matrix_size, 2]
            r = np.average(img_matrix_red)

            cv2.rectangle(blank, (col, row), (col+matrix_size,
                                              row+matrix_size), (b, g, r), 1)
            cv2.circle(blank, (col+matrix_size//2, row+matrix_size//2),
                       matrix_size//2, (b, g, r), -1)

    cv2.imshow("original", img)
    cv2.imshow("window1", blank)
    cv2.waitKey(1)
