programming_dictionary = {
    "Bug": "An error in a program",
    "Function": "A piece of code that you can easily call over and over again.",
}

# print(programming_dictionary["Bug"])

programming_dictionary["Loop"] = "The action of doing something over and over again."

#wiping an existing dictionary

# programming_dictionary = {}
# print(programming_dictionary)

#Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."


#Loop through a dictionary
for key in programming_dictionary:
    print(programming_dictionary[key])