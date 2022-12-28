import pickle
n=int(input("Enter How many entries you want to make: "))
emp=open("employee1.dat","wb")
for i in range(n):
    a=int(input("Enter employee number: "))
    b=input("Enter employee name: ")
    c=int(input("Enter employee age: "))
    d=int(input("Enter employee salary: "))
    emp1= {"empno":a,"name":b,"age":c,"salary":d}
    pickle.dump(emp1,emp)
print("Successful")
emp.close()
