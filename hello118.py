from tkinter import *
import calendar
def showCalender():
    gui = Tk()
    gui.config(background="black")
    gui.title("Calender of year")
    gui.geometry("550x600")
    year = int(year_field.get())
    gui_content= calendar.calendar(year)
    calYear=Label(gui, text=gui_content, font="Consolas 10 bold")
    calYear.grid(row=5,column=1)
    gui.mainloop()
    
if __name__ == "__main__":
    new = Tk()
    new.config(background="grey")
    new.title("Calender")
    new.geometry("250x140")
    cal = Label(new, text="Calendar",bg="grey",font=("times",28,"bold"))
    year = Label(new, text="Enter year", bg='dark grey')
    year_field=Entry(new)
    button=Button(new,text="Show Calendar",fg="Black",bg="Blue",command=showCalender)
    cal.grid(row=1,column=1)
    year.grid(row=2,column=1)
    year_field.grid(row=3,column=1)
    button.grid(row=4,column=1)

    new.mainloop()
