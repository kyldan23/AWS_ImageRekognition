import cv2
import numpy as np
from takeImage import takeSingleImage


#raw_img = takeSingleImage()


"""
#Blue Color 
low_blue = np.array([94, 80, 2])
high_blue = np.array([126, 255, 255])
blue_mask = cv2.inRange(hsv_image, low_blue, high_blue)
blue = cv2.bitwise_and(raw_image, raw_image, mask=blue_mask)

"""
# Red color
def onlyRedPart(raw_img):
    hsv_image = cv2.cvtColor(raw_img, cv2.COLOR_BGR2HSV)
    """low_red = np.array([161, 155, 84])
    high_red = np.array([179, 255, 255])
    red_mask = cv2.inRange(hsv_image, low_red, high_red)
    red = cv2.bitwise_and(raw_img, raw_img, mask=red_mask)"""
    # lower boundary RED color range values; Hue (0 - 10)
    lower1 = np.array([0, 100, 20])
    upper1 = np.array([10, 255, 255])
    
    # upper boundary RED color range values; Hue (160 - 180)
    lower2 = np.array([160,100,20])
    upper2 = np.array([179,255,255])
    
    lower_mask = cv2.inRange(hsv_image, lower1, upper1)
    upper_mask = cv2.inRange(hsv_image, lower2, upper2)
    """ Testing if you can cannyedge the mask itself
    cv2.imshow("lower_mask", lower_mask)
    cannyEdge = cv2.Canny(lower_mask, 0, 200)
    cv2.imshow('cannyedge', cannyEdge)
    """
    full_mask = lower_mask + upper_mask
    
    result = cv2.bitwise_and(raw_img, raw_img, mask=full_mask)

    return full_mask, result

""" Testing only red color
red = onlyRedPart(raw_img)[1]
cv2.imshow("Original", raw_img)
cv2.imshow("Red Filter", red)
cv2.waitKey(10000)
cv2.destroyAllWindows()
"""
"""PseudoCode
-Take an image 
-Convert image to hsv format 
-Initialize array with the names of 3 sodas (Coke, Fanta, and Sprite)
-Initialize empty dictionary
-Fill dictionary with key value pairs (Key = name of soda, Value = Total area with all color filters combined) 
-Return brand name after finding the max value from the dictionary 
"""