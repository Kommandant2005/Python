import os
import csv
def addrecord():
    print("Add a new Record")
    print("================")
    f=open('students.csv','a',newline='\r\n')
    s=csv.writer(f)
    rollno=int(input('Enter rollno='))
    name=input('Enter name=')
    marks=float(input('Enter marks='))
    rec=[rollno,name,marks]
    s.writerow(rec)
    f.close()
    print("Record Saved")
    input("Press any key to continue..")

def modifyrecord():
    print("Modify a Record")
    print("================")
    f=open('students.csv','r',newline='\r\n') 
    f1=open('temp.csv','w',newline='\r\n')
    f1=open('temp.csv','a',newline='\r\n')
    r=input('Enter rollno you want to modify')
    s=csv.reader(f)
    s1=csv.writer(f1)
    for rec in s:
        if rec[0]==r:
            print("Rollno=",rec[0])
            print("Name=",rec[1])
            print("Marks=",rec[2])
            choice=input("Do you want to modify this record(y/n)")
            if choice=='y' or choice=='Y':
                rollno=int(input('Enter New rollno='))
                name=input('Enter new name=')
                marks=float(input('Enter new marks='))
                rec=[rollno,name,marks]
                s1.writerow(rec)
                print("Record Modified")
            else:
                s1.writerow(rec)
        else:
            s1.writerow(rec)
    f.close()   
    f1.close()
    os.remove("students.csv")
    os.rename("temp.csv","students.csv")
    
    input("Press any key to continue..")

def deleterecord():
    f=open('students.csv','r',newline='\r\n') 
    f1=open('temp.csv','w',newline='\r\n')
    f1=open('temp.csv','a',newline='\r\n')
    r=input('Enter rollno you want to delete')
    s=csv.reader(f)
    s1=csv.writer(f1)
    for rec in s:
        if rec[0]==r:
            print("Rollno=",rec[0])
            print("Name=",rec[1])
            print("Marks=",rec[2])
            choice=input("Do you want to delete this record(y/n)")
            if choice=='y' or choice=='Y':
                pass
                print("Record Deleted")
            else:
                s1.writerow(rec)
        else:
            s1.writerow(rec)
    f.close()
    f1.close()
    os.remove("students.csv")
    os.rename("temp.csv","students.csv")
    
    input("Press any key to continue..")

def search():
    print("Search a Record")
    print("===================")
    f=open('students.csv','r',newline='\r\n')  #Remove new line character from output
    r=input('Enter rollno you want to search')
    s=csv.reader(f)
    for rec in s:
        if rec[0]==r:
            print("Rollno=",rec[0])
            print("Name=",rec[1])
            print("Marks=",rec[2])
    f.close()
    input("Press any key to continue..")
def viewall():
    print("List of All Records")
    print("===================")
    f=open('students.csv','r',newline='\r\n')  #Remove new line character from output
    s=csv.reader(f)
    i=1
    for rec in s:
        print(rec[0],end="\t\t")
        print(rec[1],end="\t\t")
        print(rec[2])
        i+=1
    f.close()
    input("Press any key to continue..")

def mainmenu():
    choice=0
    while choice!=6:
        print("\n")
        print("Main Menu")
        print("==========")
        print("1. Add a new Record")
        print("2. Modify Existing Record")
        print("3. Delete Existing Record")
        print("4. Search a Record")
        print("5. List all Records")
        print("6.Exit")
        choice=int(input('Enter your choice'))
        if choice==1:
            addrecord()
        elif choice==2:
            modifyrecord()
        elif choice==3:
            deleterecord()
        elif choice==4:
            search()
        elif choice==5:
            viewall()
        elif choice==6:
            print("Software Terminated")
            break
mainmenu()
