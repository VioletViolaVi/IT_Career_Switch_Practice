print("Hello world")
print("hey Python, long time no see huh :D ")

x = 10.32
print(type(x))

print(type(10.32))

print(type(10))

print(type("10"))

print(type(6.1))

print(type(-211.2871))

print(isinstance(6.1, float))

print(isinstance(6.1, int))

print(isinstance(-211.2871, float))

print(isinstance(-211.2871, int))

number = 10
print(float(number))
print(int(number))

stringItem = "kittens on a cloud"
print(isinstance(stringItem, str))
print(isinstance(stringItem, str))

some_num = "55"
print(isinstance(some_num, str))
print(int(some_num))
print(float(some_num))

some_other_num = 55.7
print(int(some_other_num))

print(isinstance(4.5, float))

print(isinstance(-4, float))

print(isinstance(-4, bool))

num = 25
print(num)
print(float(num))

someNumber = "25"
print(someNumber)
print(float(someNumber))

print(isinstance(55.0, float))

first_string = "hello it's rainy"
second_string = first_string
print("first_string: " + first_string)
print("second_string: " + second_string)

first_string = 'i "have" changed'
second_string = first_string
print("first_string: " + first_string)
print("second_string: " + second_string)

my_name = "sARah hudsoN"
print(my_name.title())
print(my_name.upper())
print(my_name.lower())

first_name = "dave"
last_name = "smith"
full_name = first_name + " " + last_name
print(full_name.title())

age = 58
sentence = full_name.title() + " is " + str(age) + " years old."
print(sentence)

colour = "                 green         "
filler_sentence = "My favourite colour is "
full_sentence = filler_sentence + colour.strip() + "."
print(full_sentence)

food = "                 cake         "
food_first_part = "I like to eat "
food_sentence = food_first_part + food.lstrip() + "."
print(food_sentence)

pet = "                 dog         "
pet_first_part = "I would like to buy a "
pet_sentence = pet_first_part + pet.rstrip() + "."
print(pet_sentence)

making_ten = 5 * 2 
equal_to_ten = 10
for_boolean_checking = making_ten == equal_to_ten
print(for_boolean_checking, bool)

true_or_false_math = 60 > 97
print(true_or_false_math, bool)

my_boolean = 200 > 500
print(my_boolean)
print(my_boolean, bool)

# this is a comment
# this is another comment
# this is the third comment now
name = "steve"
print(name)

# 1.
fifthteen = 15
print(type(fifthteen))

# 2.
decimal_num = 6.36272
print(type(decimal_num))

# 3.
boolean_variable = 79 > 12
print(boolean_variable)

# 4.
# this is yet again another comment!
item_one = "fish, "
item_two = "water "
item_three = "and sweets"
print(item_one + item_two + item_three)

# 5. (see comment for no. 4)

first, second = 56, 90
print(first)
print(second)

(third, fourth) = ("happy", 10 > 45)
print(third)
print(fourth)

pig = sheep = cow = "farm animals"
print(pig)
print(sheep)
print(cow)

python_try1 = python_try2 = python_try3 = 7893
print(python_try1)
print(python_try2)
print(python_try3)

num_list = {
    "first_number": "1",
    "second_number": "2",
    "third_number": "3",
}

for key, value in num_list.items():
    print(f"Key: {key} has a value of: {value}")

name = "dave"
age = "20"
print(f"His name is {name.title()} and he is {age} years old.")

one1,two2,three3 = 1,2,3
print(one1)
print(two2)
print(three3)

# 1.
ten, twenty, thirty = 10, 20, 30

# 2.
first1, second2, third3, fourth4 = 33, "car", 2.158, "hey"
print(first1)
print(second2)
print(third3)
print(fourth4)

# 3.
people = {
    "Dave": 41,
    "Bob": 22,
    "Mark": 38
}
for key, value in people.items():
    print(f"{key}: {value}")

print(float(22))

item = 10
print(float(item))

int(34.98)
print(int(34.98))

item2 = 874.2549
print(int(item2))

print(str(783))

print(str(54557))

# 1.
print(float(12))

# 2.
print(int(321.88))

# 3.
print(str(99))

employees = ["Tara", "Becky", "Kurt", "Stacy"]
print(employees[0])
print(employees[1])
print(employees[2])
print(employees[3])

employees = ["Tara", "Becky", "Kurt", "Stacy"]
print(employees[-1] + " is a great employee!")
print(employees[-2] + " is a great employee!")
print(employees[-3] + " is a great employee!")
print(employees[-4] + " is a great employee!")

# 1.
list_of_food_items = ["eggs", "bacon", "pizza", "pie"]

# 2.
print(list_of_food_items[1])
print(list_of_food_items[3])
 
# 3.
print(list_of_food_items[2], type(list_of_food_items[2]))

even_nums = ["2", "4", "6", "8"]
odd_num = ["1", "3", "5", "7"]
print(even_nums + odd_num)

employees_again = ["Peter", "Tara", "Becky", "Kurt", "Stacy"]
employees_again[-1] = "Joey"
print(employees_again)

employees_again = ["Peter", "Tara", "Becky", "Kurt", "Stacy"]
employees_again = employees_again + ["Paul"]
print(employees_again)

employees_again = ["Peter", "Tara", "Becky", "Kurt", "Stacy"]
employees_again.insert(2, "Lucy")
print(employees_again)

employees_again = ["Peter", "Tara", "Becky", "Kurt", "Stacy"]
del employees_again[3]
print(employees_again)

employees_again = ["Peter", "Tara", "Becky", "Kurt", "Stacy"]
employees_again.remove("Tara")
print(employees_again)

employees_again = ["Peter", "Tara", "Becky", "Kurt", "Stacy"]
for employees in employees_again:
    print(employees)

employees_again = ["Peter", "Tara", "Becky", "Kurt", "Stacy"]
if "Stacy" in employees_again:
    print("Yay! You found Stacy!")

employees_again = ["Peter", "Tara", "Becky", "Kurt", "Stacy"]
if "Becky" in employees_again:
    employees_again.remove("Becky")
    print(employees_again)
    print("You removed Becky!")

employees_again = ["Peter", "Tara", "Becky", "Kurt", "Stacy"]
print(len(employees_again))

# 1.
fruits = ["apple", "pear", "lemon", "peach", "passionfruit"]
print(fruits)
fruits[3] = "carrot"
print(fruits)

# 2.
fruits = ["apple", "pear", "lemon", "peach", "passionfruit"]
del fruits[2]
print(fruits)

# 3.
fruits = ["apple", "pear", "lemon", "peach"]
print(fruits)
fruits.insert(3, "watercress")
print(fruits)

# orders items in list based on alphabet
body_parts = ["hands", "head", "neck", "hip", "toe", "eyes", "nails", "knee", "arms"]
body_parts.sort()
print(body_parts)

# reverses items in list based on alphabet
body_parts = ["hands", "head", "neck", "hip", "toe", "eyes", "nails", "knee", "arms"]
body_parts.sort(reverse=True)
print(body_parts)

# reverses items in list based on how it's original displayed
body_parts = ["hands", "head", "neck", "hip", "toe", "eyes", "nails", "knee", "arms"]
body_parts.reverse()
print(body_parts)

# think of sorted() as a preview that shows the changed list but the OG list itself has not been changed like that 
body_parts = ["hands", "head", "neck", "hip", "toe", "eyes", "nails", "knee", "arms"]
print(body_parts)
print(sorted(body_parts))
print(body_parts)

sorting_ages = ["23", "78", "345", "9"]
sorting_ages.sort()
print(sorting_ages)

sorting_ages = ["23", "78", "345", "9"]
sorting_ages.sort(reverse=True)
print(sorting_ages)

# 1.
furniture = ["chair", "sink", "table", "door"]
furniture.sort()
print(furniture)

# 2.
furniture = ["chair", "sink", "table", "door"]
furniture.sort(reverse=True)
print(furniture)




