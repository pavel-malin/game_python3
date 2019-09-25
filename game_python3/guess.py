# Это игра по угадыванию чисел.
import random

guessesTaken = 0

print('Привет! Как тебя зовут?')
myName = input()

number = random.randint(1, 20) # 1-100
print('Что ж ,' + myName + ', я загадыва. число от 1 до 20.') # 1-100

for guessesTaken in range(4):
    print('Попробуй угадать.')

    guess = input()
    guess = int(guess)

    if guess < number:
        print('Твое число слишком маленькое.')

    if guess > number:
        print('Твое число большое.')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print('Отлично, ' + myName + '! Ты справился за ' + guessesTaken + ' попытки!')

if guess != number:
    number = str(number)
    print('Увы. Я загадала число ' + number + '.')