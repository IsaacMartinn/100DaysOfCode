import random

HANGMANPICS = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========''']


#1. set a variable called 'lives' to keep track of the number of lives left
#set lives to equal 6

#2. if guess is not a letter in the chosen_word then reduce lives by 1
#if lives goes down to 0 then print the game should end, and it should print "you lose"

#3. print the ASCII art from the list stages that corresponds to the ucrrent number of lives the user has remaingin


word_list = ["aardvark","baboon","camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_ "
print(placeholder)



game_on = True

correct_letters = []
lives = 6

while game_on:

    guess = input("Guess a letter: ").lower()

    display = ""

    for letter in chosen_word:
        if letter == guess:
          display += letter
          correct_letters.append(guess)
        elif letter in correct_letters:
          display += letter
        else:
           display += "_"

    print(display)

    if guess not in chosen_word:
       lives -=1
       if lives == 0:
          game_on = False
          print("You lose")



    if "_" not in display: 
       game_on = False
       print("You win!")

    print(HANGMANPICS[lives])
        
