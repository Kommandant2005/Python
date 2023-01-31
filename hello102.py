import pickle
n=int(input("Enter How Many Entries You want To Make: "))
fh=open("employee3.dat","wb")
for i in range(n):
    a=int(input("Enter Roll No.: "))
    b=input("Enter Student Name: ")
    c=int(input("Enter Total Marks: "))
    dictionary={"RollNo":a,"Name":b,"Marks":c}
    pickle.dump(dictionary,fh)

fh.close()
