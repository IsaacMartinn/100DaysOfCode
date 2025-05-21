print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("Whats your age?"))
    if age <= 12: 
        bill =5
        print(f"Child tickets are ${bill}.")
    elif age <= 18: 
        bill = 7
        print(f"Youth tickets are ${bill}.")
    elif age >= 45 and age <= 55: 
        bill = 0
    else: 
        bill=12
        print(f"Adult tickets are ${bill}")

    wants_photo = input("Do you want a photo taken? Type y for Yes and n for No. ")
    if wants_photo == 'y':
        bill += 3
        
    print(f"Your final pay is ${bill}.")
   
   
else: 
    print("Sorry you have to grow taller before you can ride.")