print(""" _____________________
|  _________________  |
| |              0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | ÷ | |
| |___|___|___| |___| |
|_____________________|
""")

calculator_on = True

def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


n1 = int(input("What's the first number?: "))
while calculator_on:
    for i in operations: 
        print(i)
    key = input("Pick an operation: ")
    n2 = int(input("What's the next number?: "))

    final_num = operations[key](n1,n2)


    print(f"{n1} {key} {n2} = {final_num}")
    end_calculator = input("Do you want to continue type 'y' or 'n': ")
    if end_calculator == 'n':
        print("Take care!")
        calculator_on = False
    else:
        user_choice =input(f"Type 'y' to continue calculating with {final_num}, or type 'n' to start a new calculation: ").lower()
        if user_choice == "y":
            n1 = final_num
        else: 
            n1 = int(input("What's the first number?: "))


    
    


