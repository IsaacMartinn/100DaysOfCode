from coffee_data import MENU,resources

coffee_machine_on = True
total_money_earned = 0 

water_resources = resources["water"]
milk_resources = resources["milk"]
coffee_resources = resources["coffee"]



# print(MENU["espresso"]["cost"])

def process_coins():
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickels = int(input("How many nickels?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    total_coins = quarters  + dimes + nickels + pennies
    return total_coins

def check_resources(user_choice):
    if water_resources < MENU[user_choice]["ingredients"]["water"]:
        print("Sorry there is not enough water.")
        return False
    elif milk_resources < MENU[user_choice]["ingredients"]["milk"]:
        print("Sorry there is not enough milk.")
        return False
    elif coffee_resources < MENU[user_choice]["ingredients"]["coffee"]:
        print("Sorry there is not enough coffee.")
        return False
    else:
        return True

def update_resources(user_choice):
     global water_resources, milk_resources, coffee_resources
     water_resources -= MENU[user_choice]["ingredients"]["water"]
     milk_resources -= MENU[user_choice]["ingredients"]["milk"]
     coffee_resources -= MENU[user_choice]["ingredients"]["coffee"]


   
        
while coffee_machine_on:
    user_choice = input("What would you like? ($1.50 espresso/ $2.50 latte/ $3.00 cappuccino): ").lower()
    if user_choice == "report":
            print(f"Water: {water_resources}ml")
            print(f"Milk: {milk_resources}ml")
            print(f"Coffee: {coffee_resources}g")
            print(f"Money ${total_money_earned}")
    elif user_choice == "off":
            coffee_machine_on = False
    else: 
        sufficient_resources = check_resources(user_choice=user_choice)
        if sufficient_resources == True:
            total_inserted_coins = process_coins()
            drink_price = MENU[user_choice]["cost"]
            if total_inserted_coins < drink_price:
                 print("Sorry that's not enough money. Money refunded.")
            elif total_inserted_coins == drink_price:
                 total_money_earned += drink_price
                 update_resources(user_choice=user_choice)
                 print(f"Here is your {user_choice} ☕️. Enjoy!")
            else:
                 total_money_earned += drink_price
                 extra_money = total_inserted_coins - drink_price
                 update_resources(user_choice=user_choice)
                 print(f"Here is ${extra_money} dollars in change.")
                 print(f"Here is your {user_choice} ☕️. Enjoy!")
                 
