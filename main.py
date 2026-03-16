import random
import string

def pick_word():
 words =["pizza", "burger", "sushi", "waffle", "fish", "steak"]
 return random.choice(words)

def display_word(secret_word, geussed_letters):
 result = ""
 for letter in secret_word:
  if letter in geussed_letters:
   result += letter + " "
  else:
   result += "_ "
 print(result.strip())

def validate_input():
 guess = input("Guess a letter: ").lower()
 while len(guess) != 1 or not guess.isalpha():
  guess = input("Enter a single letter: ").lower()
 return guess

def get_auto_guess(guessed_letters):
  remaining = []

def play_game():
    mode = input("Type Auto to activate the auto play mode: ")
    secret_word = pick_word()
    guessed_letters = []
    turns_left = 6

    while turns_left > 0:
        display_word(secret_word, guessed_letters)
        print("Turns left:", turns_left)
        guess = validate_input()

        if guess in guessed_letters:
            print("Already guessed.")
            continue
        guessed_letters.append(guess)

        if guess not in secret_word:
            turns_left -= 1
            print("Wrong guess.")

        if all(letter in guessed_letters for letter in secret_word):
            print("You won! The word was:", secret_word)
            return

    print("You lost! The word was:", secret_word)

play_game()