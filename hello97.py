import pickle
c={}
emp=open("employee.dat","rb")
c=pickle.load(emp)
print(c)
print("Successful")
emp.close()

