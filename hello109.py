from tkinter import *
import random

root=Tk()
root.geometry("300x200")

def start():
    def ask():
        answers = [
            "The answer lies in your heart",
            "l do not know",
            "Almost certainly",
            "well. well",
            "Outlook good.",
            "Why do you need to ask?" ,
            "Go away."
            "Time will only tell",
            "Cannot predict now.",
            "Reply hazy, try again.",
            "most probably",
            "hmmm-..i am thinking"
        ]

        l2=Label(newWindow)
        l2.config(text=str(random.choice(answers)))
        l2.place(x=160,y=80)

    newWindow = Toplevel(root)
    newWindow.title("MagicBa118")
    newWindow.geometry("350x250")

    ql = Label(newWindow,text="Ask your question")
    ql.place(x=40,y=50)

    ql_entry = Entry(newWindow)
    ql_entry.place(x=160,y=50)

    another = Button(newWindow, text="Another Question",command=start)
    another.place(x=40,y=140)

    cancel = Button(newWindow, text="Cancel",command=quit)
    cancel.place(x=150,y=140)

    ask = Button(newWindow,text="Ask",command=ask)
    ask.place(x=300,y=50)

    
title_label = Label(root,text="MAGICBALL8",font=("Cabin",12,"bold"),fg="blue")
title_label.place(x=100,y=100)

name_label = Label(root,text="Your Name")
name_label.place(x=50,y=50)

entry_name = Entry(root)
entry_name.place(x=140,y=50)

readyLabel = Label(root,text="Are You Ready?")
readyLabel.place(x=50,y=80)

yes_label = Label(root,text="Yes")
yes_label.place(x=140,y=80)

no_label = Label(root,text="No")
no_label.place(x=190,y=80)

yes = Checkbutton(root)
yes.place(x=160,y=80)

no = Checkbutton(root,command=quit)
no.place(x=220,y=80)

cancel_btn = Button(root,text="Cancel",command=quit)
cancel_btn.place(x=140,y=150)

submit = Button(root,text="Let's Start", command=start)
submit.place(x=200,y=150)

root.mainloop()










                      
    
