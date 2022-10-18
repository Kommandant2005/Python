from tkinter import *
import random, string
import pyperclip

root = Tk()
root.geometry("400x400")
root.resizable(0,0)
root.title("DataFlair - Password Generator")

Label(root,text="Password Generator",font="arial 15 bold").pack()
Label(root,text="DataFlair",font="arial 15 bold").pack(side=BOTTOM)

pass_label = Label(root,text="Password Length",font="arial 10 bold").pack()
pass_len = IntVar()
length = Spinbox(root, from_ = 8, to_ = 32 , textvariable= pass_len, width=15).pack()

pass_str = StringVar()
def Generator():
    password=""

    for x in range(0,4):
        Password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.digits) + random.choice(string.punctuation)
    for y in range(pass_len.get()- 4):
        Password = Password + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    pass_str.set(Password)
Button(root,text="Generate Password" , command = Generator).pack(pady=5)
Entry(root, textvariable = pass_str).pack()

def Copy_Password():
    pyperclip.copy(pass_str.get())

Button(root,text="Copy To ClipBoard" , command = Copy_Password).pack(pady=5)

root.mainloop()
