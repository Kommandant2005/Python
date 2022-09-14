a ={}
for i in range(0,6):
    playername=str(input("Enter the player name:"))
    score= int(input("Enter the score:"))
    a[playername] = score
print(a)
a = a.items()
for i in a:
    print(i)
                   
    
