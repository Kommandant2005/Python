n=int(input("Enter The Number Of Rows"))
for i in range(0,n):
    for j in range(0,n-i-1):
        print(end=" ")
    for j in range(0,i+1):
        print("*",end=" ")
    print("\r")


for i in range(n,0,-1):
    for j in range(0,n-i):
        print(end=" ")
    for j in range(0,i):
        print("*",end=" ")
    print("\r")

        
