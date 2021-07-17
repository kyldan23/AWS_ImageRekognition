import cv2
from colorFilter import onlyRedPart

#img = takeSingleImage()
cv2.namedWindow('canny edge photo')
cv2.createTrackbar('lower', 'canny edge photo', 0, 255, lambda x: None)
cv2.createTrackbar('upper', 'canny edge photo', 0, 255, lambda x: None)

raw_img = cv2.imread('referenceImages/coke.jpg')

blur_img = cv2.blur(raw_img, (5,5))
#Filter out red color only
red_mask, red_img, lower_mask = onlyRedPart(blur_img)
#Convert to grayscale 
gray = cv2.cvtColor(red_img, cv2.COLOR_BGR2GRAY)

while True:
    canny_lowerBound = cv2.getTrackbarPos('lower', 'canny edge photo')
    canny_upperBound = cv2.getTrackbarPos('upper', 'canny edge photo')
    cannyEdge = cv2.Canny(lower_mask, canny_lowerBound, canny_upperBound)

    cv2.imshow('original photo', raw_img)
    cv2.imshow('Blurred Image', blur_img)
    cv2.imshow('red_mask', red_mask)
    cv2.imshow('red image', red_img)
    cv2.imshow('grayscale photo', gray)
    cv2.imshow('canny edge photo', cannyEdge)
    if cv2.waitKey(1) == 27: 
        cv2.destroyAllWindows()
        break