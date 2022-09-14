import random
import math

lower = int(input("Enter Lower Limit :- "))
upper = int(input("Enter Upper Limit :- "))

x = random.randint(lower, upper)
print("\n\tYou've only ",
      round(math.log(upper - lower + 1, 2)),
      "chances to guess the integer!\n")

count=0

while count < math.log(upper - lower + 1, 2):
    count += 1

    guess = int(input("Guess a number :- "))

    if x == guess:
        print("Congratulations you did it in ",count, "try")
        break
    elif x > guess:
        print("You have guessed too small!!")
    elif x < guess:
        print("You have guessed too big!!")

if count > math.log(upper - lower +1, 2):
    print("\nThe number is %d" % x)
    print("Better Luck Next Time!")
