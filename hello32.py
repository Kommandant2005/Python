a=input("Enter any name: ")
#print(a)
length=len(a)
b=0
for i in range(-1,(-length-1),-1):
    print(a[b] ,"\t" ,a[i])
    b=b+1
