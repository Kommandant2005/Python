from tkinter import *
root = Tk()
Label(root,text="What is your name?").grid(row=0)
Label(root,text="Class?").grid(row=1)
e1=Entry(root)
e1.grid(row=0,column=1)
e2=Entry(root)
e2.grid(row=1,column=1)
root.mainloop()
                               
