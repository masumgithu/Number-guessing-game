#Number Guessing Game
import random

RandomNumber = random.randrange(1,200)

print(RandomNumber)

userInput = int(input("Guess the number:"))

if userInput > RandomNumber:
    print("the number is to high")

elif RandomNumber > userInput:
    print("the number is to low")

else:
    print("yes, you matchedvthe number")