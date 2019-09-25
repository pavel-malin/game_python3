# This is a guessing number game.
import random

guessesTaken = 0

print("Hello! What's your name?")
myName = input()

number = random.randint(1, 20)
print("Well, " + myName + ", Im's guessing. number from 1 to 20.")

for guessesTaken in range(6):
    print("Try to guess.")

    guess = input()
    guess = int(guess)

    if guess < number:
        print("Your number is too small.")

    if guess > number:
        print("Your number is big.")
    
    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print("Fine, " + myName + "! You managed for " + guessesTaken + " attempts!")

if guess != number:
    number = str(number)
    print("Alas. I made a number " + number + ".")