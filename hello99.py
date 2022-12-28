import pickle
str1=""
with open("employee1.dat","rb") as fh:
    str1 = pickle.load(fh)
    lst = str1.split("o")
    print(lst[0])
    print("Successful")
