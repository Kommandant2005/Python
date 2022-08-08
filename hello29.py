x = float(input("Enter Value of x: "))
n = int(input("Enter Value of n: "))
s = 0

for a in range(n + 1):
    if a%2 == 0:
        s += x**a
    else:
        s -= x**a
print("The Sum Of The Series is: ", s)
