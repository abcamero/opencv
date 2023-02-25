import cv2
import tkinter
import imageops
from tkinter.filedialog import askopenfile

from tkinter import *

# declare the window
window = Tk()
# set window title
window.geometry("1080x720")
window.title("FireBlaze")

frame = Frame(window, width=600, height=400)
frame.pack()
frame.place(anchor='e', relx=0.5, rely=0.5)

btn1 = Button(window, text='Live Cam', height=5, width=10)
btn1.pack()

btn2 = Button(window, text='Load Image', height=5, width=10, command=lambda: imageops.LoadImage(frame))
btn2.pack()



# set window width and height
# window.configure(width=500, height=300)
# set window background color
window.configure(bg='lightgray')
window.mainloop()
