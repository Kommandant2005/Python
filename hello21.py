ch=input("Enter a single character: ")
if ch>="A" and ch<="Z":
    print("You entered an Uppercase Character")
elif ch>="a" and ch<="z":
    print("You entered a Lowercase Character")
elif ch>="0" and ch<="9":
    print("You entered a Number")
else:
    print("You have entered a special character")
    
