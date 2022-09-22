from tkinter import *
a=Tk()
var=IntVar()
Radiobutton(a,text="Python",variable=var,value=1).pack(anchor=W)
Radiobutton(a,text="Thunkable",variable=var,value=2).pack(anchor=W)
Radiobutton(a,text="Java",variable=var,value=3).pack(anchor=W)
Radiobutton(a,text="Javasript",variable=var,value=4).pack(anchor=W)
Radiobutton(a,text="Html5",variable=var,value=5).pack(anchor=W)
Radiobutton(a,text="C++",variable=var,value=6).pack(anchor=W)
Radiobutton(a,text="C",variable=var,value=7).pack(anchor=W)
Radiobutton(a,text="CSS",variable=var,value=8).pack(anchor=W)
Radiobutton(a,text="MySQL",variable=var,value=9).pack(anchor=W)
mainloop()

