import random
HANGMAN_PICS = ['''
    +---+
        |
        |
        |
       ===''', '''
    +---+
    O    |
         |
         |
        ===''', '''
    +---+
    O   |
    |   |
        |
       ===''', '''
    +---+
    O   |
   /|   |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
       ===''']
words = 'grass stork shark baboon ram badger beaver bull rerbuled wolf sparrow raven otter pigeon goose toad zebra snake turkey whale goat goat goat coyote cow cat rabbit rat chicken lama weasel swan lion fox salmon elk frog bear clam moth mole yrrke moo spider python parrot puma salmon skunk dog ova tiger triton seal duck trout ferret turtle hawk lizard'.split()

def getRandomWord(wordList):
    # This function returns a random string from the translated list.
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Erroneous letters:', end='')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)): # replaces omissions with these letters.
        if secretWord[i] in correctLetters:
            blanks = blanks[i] + secretWord[i] + blanks[i+1:]
    
    for letter in blanks: # Shows the secret word with spaces between letters.
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    # Returns the letter entered by the player. This function checks that the player has entered only one letter and nothing else.
    while True:
        print('Enter a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter one letter.')
        elif guess in alreadyGuessed:
            print('You already called this letter. Name another.')
        elif guess not in 'abvgdeeziyklnoprstufkhtschshschyyyuyuya':
            print('Please enter a LETTER.')
        else:
            return guess

def playAgain():
    # This function returns true if the player wants to play again; otherwise returns False.
    print('Want to play more? (Yes or no)')
    return input().lower().startswith('y')

print(' G A L L O W S ')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)

    # Allows the player to enter a letter.
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # Checks if a player has won.
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('YES! Secret word "' + secretWord + '"! You guessed!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        # Checks if a player has exceeded the limit of attempts and lost.
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have exhausted all attempts!\nNot guessed letters: ' + str(len(missedLetters)) + '.The word was made"' + secretWord + '".')
            gameIsDone = True

        # Asks if the player wants to play again (only if the game is over.)
        if gameIsDone:
            if playAgain():
                missedLetters = ''
                correctLetters = ''
                gameIsDone = False
                secretWord = getRandomWord(words)
            else:
                break