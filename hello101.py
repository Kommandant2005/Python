import pickle
fh1 = open("employee3.dat","rb")
str1 = pickle.load(fh1)
for a in str1:
    if str1[a] == 12 or str1[a] == 14:
        print(str1)
fh1.close()
