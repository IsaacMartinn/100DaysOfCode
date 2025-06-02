#functions with more than 1 input 
def greet_with(name,location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_with(name="Isaac",location = "Stouffville")
greet_with(location="Nowhere",name="Isaac")