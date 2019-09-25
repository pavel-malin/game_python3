import random

print("I'll throw a coin 1000 times. Guess how many times the 'Eagle' \
       falls? " + "(Жми клавишу Enter, чтобы начать)")
input()
flips = 0
heads = 0
while flips < 1000:
    if random.randint(0, 1) == 1:
        heads = heads + 1
    flips = flips + 1

    if flips == 900:
        print("900 popping up and 'Eagle' fell " + str(heads) + ' time.')
    if flips == 100:
        print("At 100 shots, the 'Eagle' fell " + str(heads) + ' time.')
    if flips == 500:
        print("Halfway passed and the 'Eagle' fell " + str(heads) + ' time.')

print()
print("Out of 1000 coin flips, the 'Eagle' has fallen " + str(heads) + 'time.')
print("How close are you to the correct answer?")
