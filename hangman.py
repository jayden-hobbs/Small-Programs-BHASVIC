import random
from collections import Counter

# List of words
someWords = '''apple banana mango strawberry
orange grape pineapple apricot lemon coconut watermelon
cherry papaya berry peach lychee muskmelon'''

someWords = someWords.split(' ')
# Randomly choose a secret word from our list.
word = random.choice(someWords)

if __name__ == '__main__':
    print('Guess the word! HINT: The word is a name of a fruit.')

    # Display underscores for each letter of the word
    for i in word:
        print('_', end=' ')
    print()

    playing = True
    letterGuessed = ''  # List for storing guessed letters
    chances = len(word) + 2  # Number of chances
    flag = False  # Flag to check if the word is guessed correctly

    try:
        while chances > 0 and not flag:
            print()
            chances -= 1

            guess = input('Enter a letter to guess: ').lower()

            # Input validation
            if not guess.isalpha():
                print('Enter only a letter!')
                continue
            elif len(guess) > 1:
                print('Enter only a single letter!')
                continue
            elif guess in letterGuessed:
                print('You have already guessed that letter!')
                continue

            # If the letter is guessed correctly
            if guess in word:
                letterGuessed += guess  # Add guessed letter to the list

            # Display the word with guessed letters
            for char in word:
                if char in letterGuessed:
                    print(char, end=' ')
                else:
                    print('_', end=' ')
            print()

            # Check if the word is completely guessed
            if set(word) == set(letterGuessed):
                print(f"\nThe word is: {word}")
                print('Congratulations, You won!')
                flag = True
                break  # Break out of the while loop

        # If no chances left and word is not guessed
        if chances == 0 and not flag:
            print(f"\nYou lost! The word was '{word}'.")

    except KeyboardInterrupt:
        print("\nGame interrupted. Bye!")
        exit()
