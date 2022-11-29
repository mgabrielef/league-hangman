import random
import string
from words import *

def hangman():
    difficulty = input("Choose a difficulty level\nE - easy, M - medium, H - hard:\n")
    difficulty = difficulty.lower()  
    if difficulty == 'e':
      word = random.choice(easy_words)
      word = word.upper()
    elif difficulty == 'm':
      word = random.choice(medium_words)
      word = word.upper()
    elif difficulty == 'h':
      word = random.choice(hard_words)
      word = word.upper()
    else:
      print("I don't get what you're saying")
      return hangman()
      
    word_letters = set(word)  
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  

    lives = 6
    

    
  

    
    while len(word_letters) > 0 and lives > 0:
    
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1  
                print('\nYour letter,', user_letter, 'is not in the word.')

        elif user_letter in used_letters:
            print('\nYou have already used that letter. Guess another letter.')

        else:
            print('\nThat is not a valid letter.')
        if lives == 6:
          print("""
         +---+
             |
             |
             |
            ===""")
        elif lives == 5:
          print("""
          +---+
          O   |
              |
              |
             ===""")
        elif lives == 4:
          print("""
          +---+
          O   |
          |   |
              |
             ===""") 
        elif lives == 3:
          print("""
          +---+
          O   |
         /|   |
              |
             ===""")
        elif lives == 2:
          print("""
          +---+
          O   |
         /|\  |
              |
             ===""")
        elif lives == 1:
          print("""
          +---+
          O   |
         /|\  |
         /    |
             ===""")

    if lives == 0:
        print("""
          +---+
          O   |
         /|\  |
         / \  |
             ===""")
        print('You died. The word was', word)
    else:
        print('Congrats! You guessed the word', word, '!')

    playagain = input("Want to play again?\nY - yes, N - no:\n")
    playagain = playagain.lower()
  
    if playagain == 'y':
      hangman()
    elif playagain == 'n':
      exit()
    else:
      print("I don't get what you're saying. I'll just leave")
      
      

hangman()