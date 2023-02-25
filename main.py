import cv2
import numpy as np

img = cv2.imread("traffic.jpeg")
print(img.shape)
# We haveto write a transformation function call

cv2.imshow("INPUT-IMAGE1", img)
cv2.waitKey(0)  # waitkey -> to hold image on screen


# dif -> API call & Function call

def ImageOperation(img):
    img = cv2.resize(img, (250, 500))
    img = cv2.convertScaleAbs(img, alpha=1.7, beta=15)  # alpha (contrast control) Beta (Brightness control)
    img = cv2.blur(img, (50, 50))
    img = cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE) # rotate via codec
    t_lower2 = 50
    t_upper2 = 100
    edge2 = cv2.Canny(img,t_lower2,t_upper2)
    kernal1 = np.array([[1,1,1],[1,9,1],[1,1,1]])
    img = cv2.filter2D(img,-1,kernal1)
    factor = img.max()
    negative = factor - img

    #return img,edge,edge2
    return img,negative


#retimg,edge,edge2 = ImageOperation(img)
retimg,negative = ImageOperation(img)
cv2.imshow("OUTPUT-IMAGE1", retimg)
cv2.imshow("Negative Image",negative)
#cv2.imshow("Edge inage with new threshold",edge)
#cv2.imshow("Edge inage ",edge2)
cv2.waitKey(0)
