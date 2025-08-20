#FileNotFound
# with open("a_file.txt") as file: 
#     file.read()

#KeyError
# a_dictionary = {"key":"value"}
# value = a_dictionary["non_existent_key"]

#IndexError
# fruit_list = ["Apple","Banana","Pear"]
# fruit = fruit_list[3]

#TypeError
# text = "abc"
# print(text+5)

#FileNotFound
try:
    file = open("a_file.txt")
    a_dictionary = {"key":"value"}
    print(a_dictionary["sdfsdf"])
except FileNotFoundError:
   file = open("a_file.txt","w")
   file.write("something")
except KeyError as error_message: 
    print(f"That key {error_message} does not exists.")
else:
    content = file.read()
    print(content)
finally:
    raise TypeError("This is an error that I made up") 
    file.close()
    print("File was closed")