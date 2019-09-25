import random

number1 = random.randint(1, 10)
number2 = random.randint(1, 10)
print('How much will: ' + str(number1) + ' + ' + str(number2) + '?')
answer = input()
if int(answer) == number1 + number2:
    print('Right!')
else:
    print('Not! Correct answer -' + str(number1 + number2))
