import random
import time


def displayIntro():
    print('''You are in the lands inhabited by dragons.
    In front of you you see two caves. In one of them - a friendly dragon,
    who is ready to share with you his treasures. In the second -
    greedy and hungry dragon that will eat you.''')
    print()


def chosenCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave will you enter? (press 1 or 2 key)')
        cave = input()

    return cave


def checkCave(chosenCave):
    print('You are approaching a cave ...')
    time.sleep(2)
    print('Большой дракон выпрыгивает перед вами! Он ракрывает раскрывает \
           свою пасть и ...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('... sharing with you his treasures!')
    else:
        print('... instantly eats you up!')


playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = chosenCave()
    checkCave(caveNumber)

    print('Will you try your luck again? (Yes or no?)')
    playAgain = input()
