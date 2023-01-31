from tkinter import *
import tkinter

def buttonclick(numbers):   #define the button(btn)click function
    global operator
    operator=operator + str(numbers)
    textinput.set(operator)

def buttonClearDisplay():   # define the clear function
    global operator
    operator=""
    textinput.set("")

def buttonEqualsInput():     #define the Equal to function
    global operator
    sumup=str(eval(operator))
    textinput.set(sumup)
    operators=""

calculator = Tk()
calculator.title("Pythontpoint")       # name the app, i choose a "calculator" because it's random
operator = ""
textinput = StringVar()

textdisplay = Entry(calculator,font=('Times New Roman', 25,'bold'), textvariable=textinput, bd=30, insertwidth=4,
                   bg="cyan", justify='right').grid(columnspan=4) 

buttonclear=Button(calculator,padx=16,pady=16,bd=8, fg="black",font=('Times New Roman', 25,'bold'),
            text="C",bg="cyan",command=buttonClearDisplay).grid(row=1,column="0")

ButtonM=Button(calculator,padx=16,pady=16,bd=8, fg="black",font=('Times New Roman', 25,'bold'),
            text="M",bg="cyan",).grid(row=1,column="1")

Buttonbraket1=Button(calculator,padx=16,pady=16,bd=8, fg="black",font=('Times New Roman', 25,'bold'),
            text="(",bg="cyan",command=lambda:buttonclick("(")).grid(row=1,column="2")

Buttonbracket2=Button(calculator,padx=16,pady=16,bd=8, fg="black",font=('Times New Roman', 25,'bold'),
            text=")",bg="cyan",command=lambda:buttonclick(")")).grid(row=1,column="3")
#=======================================================================================================================

button7=Button(calculator,padx=16,pady=16,bd=8, fg="black",font=('Times New Roman', 25,'bold'),
            text="7",bg="cyan",command=lambda:buttonclick(7)).grid(row=2,column="0")

button8=Button(calculator,padx=16,pady=16,bd=8, fg="black",font=('Times New Roman', 25,'bold'),
            text="8", bg="cyan",command=lambda:buttonclick(8)).grid(row=2,column="1")

button9=Button(calculator,padx=16,pady=16,bd=8, fg="black",font=('Times New Roman', 25,'bold'),
            text="9", bg="cyan",command=lambda:buttonclick(9)).grid(row=2,column="2")

Division=Button(calculator,padx=16,pady=16,bd=8, fg="black",font=('Times New Roman', 25,'bold'),
            text="/",bg="cyan",command=lambda:buttonclick("/")).grid(row=2,column="3")
#===========================================================================================================================

button6=Button(calculator,padx=16,pady=16,bd=8, fg="black",font=('Times New Roman', 25,'bold'),
            text="6",bg="cyan",command=lambda:buttonclick(6)).grid(row=3,column="0")

button5=Button(calculator,padx=16,pady=16,bd=8, fg="black",font=('Times New Roman', 25,'bold'),
            text="5",bg="cyan",command=lambda:buttonclick(5)).grid(row=3,column="1")

button4=Button(calculator,padx=16,pady=16,bd=8, fg="black",font=('Times New Roman', 25,'bold'),
            text="4",bg="cyan",command=lambda:buttonclick(4)).grid(row=3,column="2")

subtraction=Button(calculator,padx=16,pady=16,bd=8, fg="black",font=('Times New Roman', 25,'bold'),
            text="-",bg="cyan",command=lambda:buttonclick("-")).grid(row=3,column="3")
#===============================================================================================================================

button3=Button(calculator,padx=16,pady=16,bd=8, fg="black",font=('Times New Roman', 25,'bold'),
            text="3",bg="cyan",command=lambda:buttonclick(3)).grid(row=4,column="0")

button2=Button(calculator,padx=16,pady=16,bd=8, fg="black",font=('Times New Roman', 25,'bold'),
            text="2",bg="cyan",command=lambda:buttonclick(2)).grid(row=4,column="1")

button1=Button(calculator,padx=16,pady=16,bd=8, fg="black",font=('Times New Roman', 25,'bold'),
            text="1",bg="cyan",command=lambda:buttonclick(1)).grid(row=4,column="2")

Multiplication=Button(calculator,padx=16,pady=16,bd=8, fg="black",font=('Times New Roman', 25,'bold'),
            text="*",bg="cyan",command=lambda:buttonclick("*")).grid(row=4,column="3")
#==================================================================================================================================

Button0=Button(calculator,padx=16,pady=16,bd=8, fg="black",font=('Times New Roman', 25,'bold'),
            text="0",bg="cyan",command=lambda:buttonclick(0)).grid(row=5,column="0")

Dot=Button(calculator,padx=16,pady=16,bd=8, fg="black",font=('Times New Roman', 25,'bold'),
            text=".",bg="cyan",command=lambda:buttonclick(".")).grid(row=5,column="1")

Equal=Button(calculator,padx=16,pady=16,bd=8, fg="black",font=('Times New Roman', 25,'bold'),
            text="=",bg="cyan",command=buttonEqualsInput).grid(row=5,column="2")

Addition=Button(calculator,padx=16,pady=16,bd=8, fg="black",font=('Times New Roman', 25,'bold'),
            text="+",bg="cyan",command=lambda:buttonclick("+")).grid(row=5,column="3")



calculator.mainloop()
