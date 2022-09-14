a=float(input("Enter the first number: "))
b=float(input("Enter the second number: "))
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exponent")
c=int(input("Enter your choice........ "))
def add():
    print(a+b)
def subtract():
    print(a-b)
def multiply():
    print(a*b)
def divide():
    print(a/b)
def expo():
    print(a**b)

if c==1:
    add()
elif c==2:
    subtract()
elif c==3:
    multiply()
elif c==4:
    divide()
elif c==5:
    expo()
else:
    print("Invalid Choice")
