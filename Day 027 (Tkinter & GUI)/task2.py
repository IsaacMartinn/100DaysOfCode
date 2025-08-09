#Unlimited Positional Arguments

def add(*args):
    # print(args)
    sum = 0 
    for n in args:
        sum+= n
    return sum

print(add(5,3,6,7))