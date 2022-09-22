import tkinter
a = tkinter.Tk()
a.("blue")
a.title("hello62")
a.geometry("750x500")
button=tkinter.Button(a,text="Stop",width="50",command=a.destroy,foreground="red",background="yellow")
button.pack()
a.mainloop()
