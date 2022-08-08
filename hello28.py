a=int(input("Enter Any Number (>1000): "))
b=a
reverse=0
while b:
    digit= b%10
    b==int(b/10)
    reverse = reverse*10 + digit
    b=b//10
print("Reversed number is ", reverse)
    
