from tkinter import *
a = Tk()
v=IntVar()
Radiobutton(a, text="male",variable=v,value=1).pack(anchor=W)
Radiobutton(a, text="female",variable=v,value=2).pack(anchor=W)
v1=IntVar()
Checkbutton(a,text="maths",variable=v1).pack(anchor=W)
v2=IntVar()
Checkbutton(a,text="commerce",variable=v2).pack(anchor=W)
v3=IntVar()
Checkbutton(a,text="biology",variable=v3).pack(anchor=W)
v4=IntVar()
Checkbutton(a,text="humanities",variable=v4).pack(anchor=W)
Button(a,text="Exit",width="100",height="50",command=a.destroy).pack(anchor=W)
mainloop()
