from tkinter import *

root = Tk()
frame = Frame(root)
frame.pack()
bottomframe = Frame(root)
bottomframe.pack( side= BOTTOM)
redbutton = Button(frame, text ="Red" ,fg="Red")
redbutton.pack( side= LEFT)
greenbutton = Button(frame, text ="Green" ,fg="Green")
greenbutton.pack( side= BOTTOM)
bluebutton = Button(frame, text ="Blue" ,fg="Blue")
bluebutton.pack( side= LEFT)
blackbutton = Button(frame, text ="Black" ,fg="Black")
blackbutton.pack( side= BOTTOM)
root.mainloop()