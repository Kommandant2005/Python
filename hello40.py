sentence=input("Enter a string: ")
alpha=0
digit=0
specialcharacter=0
lower=0
upper=0
for i in range(len(sentence)):
    if (sentence[i].isdigit()):
        digit = digit + 1
    elif (sentence[i].isupper()):
        upper = upper + 1
    elif (sentence[i].islower()):
        lower = lower + 1
    elif (sentence[i].islower() or sentence[i].isupper()):
        alpha = alpha + 1
    else:
        specialcharacter = specialcharacter + 1
print("No of alphabets = " , alpha)
print("No of digits = " , digit)
print("No of special characters = " , specialcharacter)
print("No of uppercase letters  = " , upper)
print("No of lowercase letters  = " , lower)

