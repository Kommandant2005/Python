from tkinter import *
root = Tk()
root.title("Admission Form")
root.geometry("250x400")
Label(root,text="Your Name").grid(row=0,column=0)
Label(root,text="Father's Name").grid(row=1,column=0)
Label(root,text="Mother's Name").grid(row=2,column=0)
Label(root,text="Age").grid(row=3,column=0)
Label(root,text="Caste").grid(row=4,column=0)
Label(root,text="Religion").grid(row=9,column=0)
Label(root,text="Aadhar Card Number").grid(row=11,column=0)
Label(root,text="Stream Chosen").grid(row=13,column=0)
e1=Entry(root)
e1.grid(row=0,column=1)
e2=Entry(root)
e2.grid(row=1,column=1)
e3=Entry(root)
e3.grid(row=2,column=1)
e4=Entry(root)
e4.grid(row=3,column=1)
v=IntVar()
Radiobutton(root,text="General",variable=v,value=1).grid(row=4,column=1)
Radiobutton(root,text="OBC",variable=v,value=2).grid(row=5,column=1)
Radiobutton(root,text="ST",variable=v,value=3).grid(row=6,column=1)
Radiobutton(root,text="SC",variable=v,value=4).grid(row=7,column=1)
e5=Entry(root)
e5.grid(row=9,column=1)
e6=Entry(root)
e6.grid(row=11,column=1)
v1=IntVar()
Radiobutton(root,text="Maths",variable=v1,value=1).grid(row=13,column=1)
Radiobutton(root,text="Biology",variable=v1,value=2).grid(row=14,column=1)
Radiobutton(root,text="Commerce",variable=v1,value=3).grid(row=15,column=1)
Radiobutton(root,text="Humanities",variable=v1,value=4).grid(row=16,column=1)
Button(root,text="Submit",foreground="white",background="black").grid(row=18,sticky=NE)
root.mainloop()
