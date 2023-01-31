import csv
fh=open("student.csv","w")
studwriter=csv.writer(fh)
studwriter.writerow(["RollNo.","Name","Marks"])
studwriter.writerows([[101,"Param",342.45],[102,"Nisha",347.565]])
'''n=int(input("Enter no of records to be entered: "))
for i in range(n):
    print("Student Record",(i+1))
    rollno=int(input("Enter Roll No. "))
    name=input("Enter Name: ")
    marks=float(input("Enter Marks: "))
    studrec=[rollno,name,marks]
    studwriter.writerow(studrec)'''
fh.close()
    
