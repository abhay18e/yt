import cv2
import numpy as np

img = cv2.imread("leaf.jpg") # change "leaf.jpg" with your image file name here
cv2.imshow("original", img)

def img_func(img,step):
    
    if step ==0:
        return img
    
    strip_count = 2**step -1
    strip_thickness = 8
    img_height, img_width, _ = img.shape
    height = img_height+strip_thickness*strip_count
    width = img_width+strip_thickness*strip_count

    blank = np.zeros((height, width, 3), dtype=np.uint8)

    img_top_left = img[0:img_height//2, 0:img_width//2]
    img_top_right = img[0:img_height//2, img_width//2:]
    img_bottom_left = img[img_height//2:, 0:img_width//2]
    img_bottom_right = img[img_height//2:, img_width//2:]

    blank[0:height//2-strip_thickness//2, 0:width //
        2-strip_thickness//2] = img_func(img_top_left,step-1)
    blank[0:height//2-strip_thickness//2, width //
        2+strip_thickness//2:] = img_func(img_top_right,step-1)
    blank[height//2+strip_thickness//2:, 0:width //
        2-strip_thickness//2] = img_func(img_bottom_left,step-1)
    blank[height//2+strip_thickness//2:, width //
        2+strip_thickness//2:] = img_func(img_bottom_right,step-1)
    
    return blank
    

out = img_func(img,4)


cv2.imshow("window1", out)


cv2.waitKey(0)
