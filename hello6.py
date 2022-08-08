a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
if a>b>c:
    print("First>Second>Third")
elif c>a>b:
    print("Third>First>Second")
elif a>c>b:
    print("First>Third>Second")
elif c>b>a:
    print("Third>Second>First")
elif b>a>c:
    print("Second>First>Second")
else:
    print("Second>Third>First")
