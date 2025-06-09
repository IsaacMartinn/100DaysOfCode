import random
from logo import blackjack_art

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(u_score, c_score):
     if u_score == c_score:
          return "Draw"
     elif c_score == 0:
          return "Lose, opponent has a Blackjack"
     elif u_score == 0:
          return "Win with a Blackjack!"
     elif u_score > 21:
          return "You went over, your lose"
     elif c_score > 21: 
          return "Opponent went over, you win"
     elif u_score > c_score:
          return "You win"
     else:
          return "You lose"
     

user_cards = []
computer_cards = []
game_on = True
computer_score = -1
user_score = -1

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

user_choice1 = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
if user_choice1 == "y":
        print(blackjack_art)

        while game_on: 
            
                user_score = calculate_score(user_cards)
                computer_score = calculate_score(computer_cards)

                print(f"Your cards: {user_cards}, current score: {user_score}")
                print(f"Computer's first card: {computer_cards[0]}")

                if user_score == 0 or computer_score == 0 or user_score > 21:
                    game_on = False
                else: 
                    user_choice2 = input("Type 'y' to get another card, type 'n' to pass: ").lower()
                    if user_choice2 == "y":
                        user_cards.append(deal_card())
                    else: 
                        game_on = False
        
        while computer_score != 0 and computer_score < 17:
             computer_cards.append(deal_card())
             computer_score = calculate_score(computer_cards)
        
        print(f"Your final hand: {user_cards}, final score: {user_score}")
        print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
        print(compare(user_score,computer_score))   
    