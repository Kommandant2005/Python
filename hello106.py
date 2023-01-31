from tkinter import*
import tkinter
import random 
import time


wd = Tk()
wd.geometry("1600x700+0+0")
wd.title("Restaurant Management System by Pythontpoint")
photo = PhotoImage(file = "rms.png")
Tops = Frame(wd,bg="white",width = 1600,height=50,relief=SUNKEN)
Tops.pack(side=TOP)

frame1 = Frame(wd,width = 900,height=700,relief=SUNKEN)
frame1.pack(side=LEFT)

frame2 = Frame(wd ,width = 400,height=700,relief=SUNKEN)
frame2.pack(side=RIGHT)
#------------------TIME--------------
localtime=time.asctime(time.localtime(time.time()))
#-----------------information TOP------------
labelinformation = Label(Tops, font=( 'aria' ,30, 'bold' ),text="Restaurant Management System",fg="steel blue",bd=10,anchor='w')
labelinformation.grid(row=0,column=0)
labelinformation = Label(Tops, font=( 'aria' ,20, ),text=localtime,fg="steel blue",anchor=W)
labelinformation.grid(row=1,column=0)

#---------------Calculator------------------
text_Input=StringVar()
operator =""

textdisplay = Entry(frame2,font=('ariel' ,20,'bold'), textvariable=text_Input , bd=5 ,insertwidth=7 ,bg="white",justify='right')
textdisplay.grid(columnspan=4)

def  buttonclick(numbers):
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)

def clrdisplay():
    global operator
    operator=""
    text_Input.set("")

def eqals():
    global operator
    sumup=str(eval(operator))

    text_Input.set(sumup)
    operator = ""

def Ref():
    x=random.randint(12980, 50876)
    randomRef = str(x)
    rand.set(randomRef)

    cof =float(Fries.get())
    colfries= float(Largefries.get())
    cob= float(hamburger.get())
    cofi= float(Filet.get())
    cochee= float(Cheese_hamburger.get())
    codr= float(Drinks.get())

    costoffries = cof*25
    costoflargefries = colfries*40
    costofhamburger = cob*35
    costoffilet = cofi*50
    costofcheesehamburger = cochee*50
    costofdrinks = codr*35

    costofmeal = "Rs.",str('%.2f'% (costoffries +  costoflargefries + costofhamburger + costoffilet + costofcheesehamburger + costofdrinks))
    PayTax=((costoffries +  costoflargefries + costofhamburger + costoffilet +  costofcheesehamburger + costofdrinks)*0.33)
    Totalcost=(costoffries +  costoflargefries + costofhamburger + costoffilet  + costofcheesehamburger + costofdrinks)
    Ser_Charge=((costoffries +  costoflargefries + costofhamburger + costoffilet + costofcheesehamburger + costofdrinks)/99)
    Service="Rs.",str('%.2f'% Ser_Charge)
    OverAllCost="Rs.",str( PayTax + Totalcost + Ser_Charge)
    PaidTax="Rs.",str('%.2f'% PayTax)

    Service_Charge.set(Service)
    cost.set(costofmeal)
    Tax.set(PaidTax)
    hamburgertotal.set(costofmeal)
    Total.set(OverAllCost)


def qexit():
    wd.destroy()

def reset():
    rand.set("")
    Fries.set("")
    Largefries.set("")
    hamburger.set("")
    Filet.set("")
    hamburgertotal.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    cost.set("")
    Cheese_hamburger.set("")


button7=Button(frame2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="7",bg="black", command=lambda: buttonclick(7) )
button7.grid(row=2,column=0)

button8=Button(frame2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="8",bg="black", command=lambda: buttonclick(8) )
button8.grid(row=2,column=1)

button9=Button(frame2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="9",bg="black", command=lambda: buttonclick(9) )
button9.grid(row=2,column=2)

Addition=Button(frame2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="+",bg="black", command=lambda: buttonclick("+") )
Addition.grid(row=2,column=3)
#---------------------------------------------------------------------------------------------
button4=Button(frame2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="4",bg="black", command=lambda: buttonclick(4) )
button4.grid(row=3,column=0)

button5=Button(frame2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="5",bg="black", command=lambda: buttonclick(5) )
button5.grid(row=3,column=1)

button6=Button(frame2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="6",bg="black", command=lambda: buttonclick(6) )
button6.grid(row=3,column=2)

hamburgerstraction=Button(frame2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="-",bg="black", command=lambda: buttonclick("-") )
hamburgerstraction.grid(row=3,column=3)
#-----------------------------------------------------------------------------------------------
button1=Button(frame2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="1",bg="black", command=lambda: buttonclick(1) )
button1.grid(row=4,column=0)

button2=Button(frame2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="2",bg="black", command=lambda: buttonclick(2) )
button2.grid(row=4,column=1)

button3=Button(frame2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="3",bg="black", command=lambda: buttonclick(3) )
button3.grid(row=4,column=2)

multiply=Button(frame2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="*",bg="black", command=lambda: buttonclick("*") )
multiply.grid(row=4,column=3)
#------------------------------------------------------------------------------------------------
button0=Button(frame2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="0",bg="black", command=lambda: buttonclick(0) )
button0.grid(row=5,column=0)

buttonc=Button(frame2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="c",bg="black", command=clrdisplay)
buttonc.grid(row=5,column=1)

buttonequal=Button(frame2,padx=16,pady=16,bd=4,width = 16, fg="white", font=('ariel', 20 ,'bold'),text="=",bg="black",command=eqals)
buttonequal.grid(columnspan=4)

Decimal=Button(frame2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text=".",bg="black", command=lambda: buttonclick(".") )
Decimal.grid(row=5,column=2)

Division=Button(frame2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="/",bg="black", command=lambda: buttonclick("/") )
Division.grid(row=5,column=3)
status = Label(frame2,font=('aria', 15, 'bold'),width = 16, text="-By Pythontpoint",bd=2,relief=SUNKEN)
status.grid(row=7,columnspan=3)

#---------------------------------------------------------------------------------------
rand = StringVar()
Fries = StringVar()
Largefries = StringVar()
hamburger = StringVar()
Filet = StringVar()
hamburgertotal = StringVar()
Total = StringVar()
Service_Charge = StringVar()
Drinks = StringVar()
Tax = StringVar()
cost = StringVar()
Cheese_hamburger = StringVar()


labelref = Label(frame1, font=( 'aria' ,16, 'bold' ),text="Order No.",fg="black",bd=10,anchor='w')
labelref.grid(row=0,column=0)
textref = Entry(frame1,font=('ariel' ,16,'bold'), textvariable=rand , bd=6,insertwidth=4,bg="light blue" ,justify='right')
textref.grid(row=0,column=1)

labelfries = Label(frame1, font=( 'aria' ,16, 'bold' ),text="Fries Meal",fg="black",bd=10,anchor='w')
labelfries.grid(row=1,column=0)
textfries = Entry(frame1,font=('ariel' ,16,'bold'), textvariable=Fries , bd=6,insertwidth=4,bg="light blue" ,justify='right')
textfries.grid(row=1,column=1)

labelLargefries = Label(frame1, font=( 'aria' ,16, 'bold' ),text="Lunch Meal",fg="black",bd=10,anchor='w')
labelLargefries.grid(row=2,column=0)
textLargefries = Entry(frame1,font=('ariel' ,16,'bold'), textvariable=Largefries , bd=6,insertwidth=4,bg="light blue" ,justify='right')
textLargefries.grid(row=2,column=1)


labelhamburger = Label(frame1, font=( 'aria' ,16, 'bold' ),text="hamburger Meal",fg="black",bd=10,anchor='w')
labelhamburger.grid(row=3,column=0)
texthamburger = Entry(frame1,font=('ariel' ,16,'bold'), textvariable=hamburger , bd=6,insertwidth=4,bg="light blue" ,justify='right')
texthamburger.grid(row=3,column=1)

labelFilet = Label(frame1, font=( 'aria' ,16, 'bold' ),text="Pizza Meal",fg="black",bd=10,anchor='w')
labelFilet.grid(row=4,column=0)
textFilet = Entry(frame1,font=('ariel' ,16,'bold'), textvariable=Filet , bd=6,insertwidth=4,bg="light blue" ,justify='right')
textFilet.grid(row=4,column=1)

labelCheese_hamburger = Label(frame1, font=( 'aria' ,16, 'bold' ),text="Cheese hamburger",fg="black",bd=10,anchor='w')
labelCheese_hamburger.grid(row=5,column=0)
textCheese_hamburger = Entry(frame1,font=('ariel' ,16,'bold'), textvariable=Cheese_hamburger , bd=6,insertwidth=4,bg="light blue" ,justify='right')
textCheese_hamburger.grid(row=5,column=1)

#--------------------------------------------------------------------------------------
labelDrinks = Label(frame1, font=( 'aria' ,16, 'bold' ),text="Drinks",fg="black",bd=10,anchor='w')
labelDrinks.grid(row=0,column=2)
textDrinks = Entry(frame1,font=('ariel' ,16,'bold'), textvariable=Drinks , bd=6,insertwidth=4,bg="light blue" ,justify='right')
textDrinks.grid(row=0,column=3)

labelcost = Label(frame1, font=( 'aria' ,16, 'bold' ),text="cost",fg="black",bd=10,anchor='w')
labelcost.grid(row=1,column=2)
textcost = Entry(frame1,font=('ariel' ,16,'bold'), textvariable=cost , bd=6,insertwidth=4,bg="light blue" ,justify='right')
textcost.grid(row=1,column=3)

labelService_Charge = Label(frame1, font=( 'aria' ,16, 'bold' ),text="Service Charge",fg="black",bd=10,anchor='w')
labelService_Charge.grid(row=2,column=2)
textService_Charge = Entry(frame1,font=('ariel' ,16,'bold'), textvariable=Service_Charge , bd=6,insertwidth=4,bg="light blue" ,justify='right')
textService_Charge.grid(row=2,column=3)

labelTax = Label(frame1, font=( 'aria' ,16, 'bold' ),text="Tax",fg="black",bd=10,anchor='w')
labelTax.grid(row=3,column=2)
textTax = Entry(frame1,font=('ariel' ,16,'bold'), textvariable=Tax , bd=6,insertwidth=4,bg="light blue" ,justify='right')
textTax.grid(row=3,column=3)

labelhamburgertotal = Label(frame1, font=( 'aria' ,16, 'bold' ),text="hamburgertotal",fg="black",bd=10,anchor='w')
labelhamburgertotal.grid(row=4,column=2)
texthamburgertotal = Entry(frame1,font=('ariel' ,16,'bold'), textvariable=hamburgertotal , bd=6,insertwidth=4,bg="light blue" ,justify='right')
texthamburgertotal.grid(row=4,column=3)

labelTotal = Label(frame1, font=( 'aria' ,16, 'bold' ),text="Total",fg="black",bd=10,anchor='w')
labelTotal.grid(row=5,column=2)
textTotal = Entry(frame1,font=('ariel' ,16,'bold'), textvariable=Total , bd=6,insertwidth=4,bg= "light blue" ,justify='right')
textTotal.grid(row=5,column=3)

#-----------------------------------------buttons------------------------------------------
labelTotal = Label(frame1,text="---------------------",fg="white")
labelTotal.grid(row=6,columnspan=3)

buttonTotal=Button(frame1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="TOTAL", bg="powder blue",command=Ref)
buttonTotal.grid(row=7, column=1)

buttonreset=Button(frame1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="RESET", bg="powder blue",command=reset)
buttonreset.grid(row=7, column=2)

buttonexit=Button(frame1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="EXIT", bg="powder blue",command=qexit)
buttonexit.grid(row=7, column=3)

def price():
    ws = Tk()
    ws.geometry("600x220+0+0")
    ws.title("Price List")
    labelinformation = Label(ws, font=('aria', 15, 'bold'), text="ITEM", fg="black", bd=5)
    labelinformation.grid(row=0, column=0)
    labelinformation = Label(ws, font=('aria', 15,'bold'), text="_____________", fg="white", anchor=W)
    labelinformation.grid(row=0, column=2)
    labelinformation = Label(ws, font=('aria', 15, 'bold'), text="PRICE", fg="black", anchor=W)
    labelinformation.grid(row=0, column=3)
    labelinformation = Label(ws, font=('aria', 15, 'bold'), text="Fries Meal", fg="steel blue", anchor=W)
    labelinformation.grid(row=1, column=0)
    labelinformation = Label(ws, font=('aria', 15, 'bold'), text="25", fg="steel blue", anchor=W)
    labelinformation.grid(row=1, column=3)
    labelinformation = Label(ws, font=('aria', 15, 'bold'), text="Lunch Meal", fg="steel blue", anchor=W)
    labelinformation.grid(row=2, column=0)
    labelinformation = Label(ws, font=('aria', 15, 'bold'), text="40", fg="steel blue", anchor=W)
    labelinformation.grid(row=2, column=3)
    labelinformation = Label(ws, font=('aria', 15, 'bold'), text="hamburger Meal", fg="steel blue", anchor=W)
    labelinformation.grid(row=3, column=0)
    labelinformation = Label(ws, font=('aria', 15, 'bold'), text="35", fg="steel blue", anchor=W)
    labelinformation.grid(row=3, column=3)
    labelinformation = Label(ws, font=('aria', 15, 'bold'), text="Pizza Meal", fg="steel blue", anchor=W)
    labelinformation.grid(row=4, column=0)
    labelinformation = Label(ws, font=('aria', 15, 'bold'), text="50", fg="steel blue", anchor=W)
    labelinformation.grid(row=4, column=3)
    labelinformation = Label(ws, font=('aria', 15, 'bold'), text="Cheese hamburger", fg="steel blue", anchor=W)
    labelinformation.grid(row=5, column=0)
    labelinformation = Label(ws, font=('aria', 15, 'bold'), text="30", fg="steel blue", anchor=W)
    labelinformation.grid(row=5, column=3)
    labelinformation = Label(ws, font=('aria', 15, 'bold'), text="Drinks", fg="steel blue", anchor=W)
    labelinformation.grid(row=6, column=0)
    labelinformation = Label(ws, font=('aria', 15, 'bold'), text="35", fg="steel blue", anchor=W)
    labelinformation.grid(row=6, column=3)

    ws.mainloop()

buttonprice=Button(frame1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="PRICE", bg="powder blue",command=price)
buttonprice.grid(row=7, column=0)

wd.mainloop()
