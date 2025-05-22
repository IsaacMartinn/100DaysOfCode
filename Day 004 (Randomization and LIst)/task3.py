#CHALLENGE: pick out a random name from the list and print it to console

import random
friends = ["Alice","Bob","Charlie","David","Emanuel"]
#1st Option 
print(random.choice(friends))

#2nd Option
random_num = random.randint(0,4)
print(friends[random_num])