a=int(input("Enter the coeff. of x^2: "))
b=int(input("Enter the coeff. of x: "))
c=int(input("Enter the constant: "))

d = (b**2) - (4*a*c)

root1 = (-b + d**0.5)/2*a
root2 = (-b - d**0.5)/2*a

print("The two roots are : " , root1 , root2)
