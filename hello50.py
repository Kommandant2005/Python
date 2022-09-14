x=int(input("Enter a number: "))
y=int(input("Enter a number: "))
z=int(input("Enter a number: "))
sum1 = x + y + z
sum2 = 0
if x == y == z:
    sum2 = 0
elif x==y:
    sum2 = z
elif y==z:
    sum2 = x 
elif z==x:
    sum2 = y
else:
    sum2 = sum1

print(sum1)
print(sum2)

    
