# Python program to demonstrate
# scale widget
import cv2
from tkinter import *

root = Tk()
root.geometry("400x300")

v1_alpha = DoubleVar()
v2_beta =  DoubleVar()

ig = cv2.imread("ball.jpeg")


def show1():
    sel = "Horizontal Scale Value = " + str(v1.get())
    l1.config(text=sel, font=("Courier", 14))


s1 = Scale(root, variable=v1_alpha,
           from_=1, to=100,
           orient=HORIZONTAL)

s2 = Scale(root, variable=v2_beta,
           from_=1, to=100,
           orient=HORIZONTAL)




l3 = Label(root, text="Horizontal Scaler")

b1 = Button(root, text="Display Horizontal",
            command=show1,
            bg="yellow")

l1 = Label(root)

s1.pack(anchor=CENTER)
l3.pack()
b1.pack(anchor=CENTER)
l1.pack()


cv2.convertScaleAbs(ig, v1_alpha, v2_beta)

cv2.imshow("Output",ig)

cv2.waitKey(0)

root.mainloop()