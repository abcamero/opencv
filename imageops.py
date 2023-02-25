from tkinter.filedialog import askopenfile
from tkinter import *
import cv2
import tkinter


def LoadImage(frame):
    file_path = askopenfile(mode='r', filetypes=[('Image Files', '*jpeg')])
    print(file_path.name)
    img = cv2.imread(file_path.name)
    img = cv2.resize(img, (600,400))
    cv2.imshow("img",img)
    cv2.waitKey(0)
    if file_path is not None:
        pass
