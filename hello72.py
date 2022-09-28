from tkinter import *
root = Tk()
T = Text(root, height=2, width=30)
T.pack()
T.insert(END,"Techokids Best Classes")
W = Spinbox(root,from_ = 0 ,to = 20)
W.pack()
root.mainloop()
