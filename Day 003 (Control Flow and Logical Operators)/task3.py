print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ").lower()
pepperoni = input("Do you want peppersoni on your pizza? Y or N: ").lower() 
extra_cheese = input("Do you want extra cheese? Y or N: ").lower()

amount = 0

if size == "s": 
    amount =+ 15
    if pepperoni == "y":
        amount += 2
elif size == "m":
    amount += 20
    if pepperoni == "y":
        amount += 3
elif size == "l": 
    amount += 25
else: 
    print("You typed in the wrong inputs")

if extra_cheese == "y":
    amount += 1

print(f"Your final bill is: ${amount}")


#todo: workout how much they need to pay based on their size choice.

#todo: work out how much to add ot hteir bill based on their pepperoni choice

#todo: workout their final amount based on whether if they want extra cheese