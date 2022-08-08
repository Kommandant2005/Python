a = input("Enter first string: ")
b = input("Enter second string: ")

if a in b:
    print("String 1 is in String 2")
    c = a[0:4]
    print(c + "restore")
else:
    print("String 1 in not in String 2" )
