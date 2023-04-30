import csv
file=open("fav.csv","r",newline="\r\n")
s=csv.reader(file)
a=input("Enter name to be searched")
for r in s:
    if r[0] == a:
        print(r[0],end="\t\t")
        print(r[1],end="\t\t")
        print(r[2])
file.close()
