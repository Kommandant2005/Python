count=0
while True:
    username=input("Enter the username: ")
    password=input("Enter the password: ")
    email=input("Enter the email-id: ")
    count+=1
    if username=="param" and password=="1234" and email=="pmshah2020@gmail.com":
        print("Welcome")
        break
    
    elif count==3:
        print("Out of attempts")
        break

    else:
        print("Try Again")
        


