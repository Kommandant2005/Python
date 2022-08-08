r=float(input("Enter the radius of the circle: "))
choice=input("Pls Enter 1 if you want to find area or 2 if you want to find circumference")
if choice == 1 :
    b=3.14*r*r
    print(b)
elif choice == 2 :
    c=3.14*2*r
    print(c)
else:
    print("Pls enter either area or circumference")
