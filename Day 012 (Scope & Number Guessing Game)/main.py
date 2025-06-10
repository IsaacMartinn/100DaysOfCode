import random

random_number = random.randint(1,100)
game_on = True

def game(random_number,lives):
    print(f"You have {lives} attempts remaining to guess the number.")
    user_guess = int(input("Make a guess: "))
    if user_guess < random_number:
        print("Too low.") 
        return True
    elif user_guess > random_number:
        print("Too high.")
        return True
    elif user_guess == random_number:
        print(f"You got it! The answer was {random_number}")
        return False
    

print("Welcome to the Number Guessing Game!")
user_difficulty_setting = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if user_difficulty_setting == "easy":
    lives = 10
elif user_difficulty_setting == "hard":
    lives = 5
else:
    print("Invalid response")

while game_on:
    x = game(random_number, lives)
    if x == True: 
        print("Guess again.")

#code is messy rn might need to fix

