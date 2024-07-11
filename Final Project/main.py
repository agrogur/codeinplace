"""
File: word_guess.py
-------------------
# WordGuess Game: A simple word guessing game 
where the player tries to guess a randomly
chosen word by entering single letters, with 
limited guesses allowed.
You can play the game at this link: https://codeinplace.stanford.edu/cip3/share/n8v2zBB4ytpnCCvX7ygM
"""

import random

# Constants
LEXICON_FILE = "Lexicon.txt"
INITIAL_GUESSES = 8

# Function to choose a random word
def get_word():
    with open(LEXICON_FILE, "r") as file:
        word_list = file.readlines()
    word_list = [word.strip() for word in word_list]
    return random.choice(word_list)

# Rest of the code remains the same...


# Function to initialize the partially guessed word
def initialize_guessed_word(secret_word):
    return "-" * len(secret_word)

# Function to update the partially guessed word
def update_guessed_word(secret_word, guessed_word, letter):
    updated_word = ""
    for i in range(len(secret_word)):
        if secret_word[i] == letter:
            updated_word += letter
        else:
            updated_word += guessed_word[i]
    return updated_word

# Function to play the game
def play_game(secret_word):
    guessed_word = initialize_guessed_word(secret_word)
    guesses_left = INITIAL_GUESSES

    print("Welcome to WordGuess!")
    print("The word now looks like this:", guessed_word)
    print("You have", guesses_left, "guesses left")

    while guesses_left > 0:
        guess = input("Type a single letter here, then press enter: ").upper()

        if len(guess) != 1:
            print("Guess should only be a single character.")
            continue

        if guess in secret_word:
            guessed_word = update_guessed_word(secret_word, guessed_word, guess)
            print("That guess is correct.")
        else:
            guesses_left -= 1
            print("There are no", guess + "'s in the word")
        
        print("The word now looks like this:", guessed_word)
        print("You have", guesses_left, "guesses left")

        if guessed_word == secret_word:
            print("Congratulations, the word is:", secret_word)
            return
        
    print("Sorry, you lost. The secret word was:", secret_word)

# Main function
def main():
    secret_word = get_word()
    play_game(secret_word)

# Run the program
if __name__ == "__main__":
    main()
