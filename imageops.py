from tkinter.filedialog import askopenfile
from tkinter import *
import cv2
import tkinter
from PIL import ImageTk, Image


class Image:
    global img
    global original_img


def LoadImage(window):
    file_path = askopenfile(mode='r', filetypes=[('Image Files', '*jpeg')])
    # Position image
    if file_path is not None:
        pass
    Image.img = cv2.imread(file_path.name)
    Image.original_img = Image.img
    cv2.imshow("Display-Image", Image.img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        return
    return

def LoadLive():

    vid = cv2.VideoCapture(0)
    while (True):
        ret, frame = vid.read()
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    vid.release()
    cv2.destroyAllWindows()

def Color2Grey(window):
    Image.img = cv2.cvtColor(Image.img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Display-Image", Image.img)
    return

def Negative(window):
    Image.img = 255 - Image.img
    # Show the image
    cv2.imshow("Display-Image", Image.img)

def Blurr(window):
    Image.img = cv2.blur(Image.img, (10, 10))
    cv2.imshow("Display-Image", Image.img)

#def Grey2RGB(window):
#    Image.img = cv2.cvtColor(Image.img,cv2.COLOR_GRAY2RGB)
#    cv2.imshow("Display-Image", Image.img)

def saveimage():
    cv2.imwrite("ResultImage.jpeg",Image.img)



def writeonImage():

    txt = input("Please enter the txt you wish to display on image")
    font = cv2.FONT_HERSHEY_SIMPLEX
    org = (50, 50)
    fontScale = 1
    color = (255, 0, 0)
    thickness = 2
    Image.img = cv2.putText(Image.img, txt , org, font,
                        fontScale, color, thickness, cv2.LINE_AA)
    cv2.imshow("Display-Image", Image.img)

def reset(window):
    Image.img = Image.original_img
    cv2.imshow("Display-Image", Image.img)