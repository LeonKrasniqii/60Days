import random

randomnumber = random.randint(0, 1000)
Guess = int(input("Guess the number from 0-1000 :"))
if Guess == randomnumber:
    print("Great you won")
else:
    print("Wrong number try again!!")
    Guess = int(input("Guess the number from 0-1000 :"))