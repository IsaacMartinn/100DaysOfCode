from art import logo, vs
from game_data import data
import random 

# print(logo)
# print(len(data))
# print(data[49])

score = 0 
game_on = True


while game_on:
    comparison_a = data[random.randint(0,len(data)-1)]
    comparison_b = data[random.randint(0,len(data)-1)]
    # print(comparison_a)
    # print(comparison_b)

    print(logo)
    print(f"Compare A: {comparison_a['name']}, {comparison_a['description']}, from {comparison_a['country']}")
    print(vs)
    print(f"Against B: {comparison_b['name']}, {comparison_b['description']}, from {comparison_b['country']}")
    user_choice = input(f"Who has more followers? Type 'A' or 'B': ").lower()
    # if statement judging follower count
    if user_choice == "a" and comparison_a['follower_count'] > comparison_b['follower_count']:
        score += 1
        print(f"You're right! Current score: {score}")
    elif user_choice == "b" and comparison_b['follower_count'] > comparison_a["follower_count"]:
        score += 1
        print(f"You're right! Current scorelol: {score}")
    elif user_choice in ("a", "b") and comparison_a['follower_count'] == comparison_b['follower_count']:
        score += 1 
        print(f"Your right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_on = False


# pretty sure all this is right now just reduce code an check against solution 

