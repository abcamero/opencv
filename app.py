import cv2
import tkinter
import imageops
from tkinter.filedialog import askopenfile
from tkmacosx import Button

from tkinter import *

# declare the window
window = Tk()
# set window title
window.geometry("1080x720")
window.configure(bg='white')
window.title("FireBlaze")
v1 = DoubleVar()
Button(window, text='Live Cam', height=5, width=10, command=lambda: imageops.LoadLive()).grid(column=0, row=1, sticky=W)
Button(window, text='Load Image', height=5, width=10, command=lambda: imageops.LoadImage(window)).grid(column=0, row=4,
                                                                                                       sticky=W)
Button(window, text='Color2Grey', height=5, width=10, command=lambda: imageops.Color2Grey(window)).grid(column=0, row=8,
                                                                                                       sticky=W)
Button(window, text='Negative', height=5, width=10, command=lambda: imageops.Negative(window)).grid(column=0, row=12, sticky=W)

Button(window, text='Blurr', height=5, width=10, command=lambda: imageops.Blurr(window)).grid(column=0, row=16, sticky=W)
Button(window, text='Reset', height=5, width=10, command=lambda: imageops.reset(window)).grid(column=0, row=20, sticky=W)

Button(window, text='Save Image', height=5, width=10, command=lambda: imageops.saveimage()).grid(column=0, row=24, sticky=W)

Button(window, text='Write On Image', height=5, width=10, command=lambda: imageops.writeonImage()).grid(column=0, row=28, sticky=W)


# set window width and heights
#window.configure(width=500, height=300)
# set window background color
window.mainloop()
