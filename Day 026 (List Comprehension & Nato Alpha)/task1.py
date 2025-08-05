#List Comprehension
numbers = [1,2,3]
new_list = [num+1 for num in numbers]

name = "Angela"
new_list2 = [letter for letter in name]


new_list3 = [num * 2 for num in range(1,5)]

#List comprehension with Test
names = ["Alex","Beth","Caroline","Dave","Elanor","Freddie"]
long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)

