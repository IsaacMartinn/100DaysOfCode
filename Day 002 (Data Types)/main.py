#Tip Calculator FINAL PROJECT
print("Welcome to the tip Calculator!")
total_bill = float(input("What was the total bill? $"))
tip = float(input("How much tip would you like to give? 10, 12, or 15? "))
num_of_guests = int(input("how many people to split the bill? "))

total_tip_amount = (tip/100) * total_bill
complete_bill = round((total_bill + total_tip_amount)/num_of_guests,2)
print(f"Each person should pay: ${complete_bill}")