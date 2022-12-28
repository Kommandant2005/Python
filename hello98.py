import pickle
string="This is my first line.This is my second line."
with open("employee1.dat","wb") as fh:
    pickle.dump(string,fh)
    print("Success")
