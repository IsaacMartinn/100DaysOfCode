#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator!")
total_bill = input("What was the total bill? $ ")
tip_percentage = input("How much tip would you like to give? 10, 12 or 15? ")
people_split = input("How many people to split the bill? ")

total_bill = float(total_bill)
tip_percentage = int(tip_percentage)
people_split = int(people_split)

bill_with_tip = (tip_percentage/100)
x = total_bill*bill_with_tip
total_amount= x+total_bill

total_amount = (round(total_amount/people_split,2))
total_amount = "{:.2f}".format(total_amount)
print(f"Each person should pay: {total_amount}")