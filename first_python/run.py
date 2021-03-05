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

one1, two2, three3 = 1, 2, 3
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
body_parts = ["hands", "head", "neck", "hip",
              "toe", "eyes", "nails", "knee", "arms"]
body_parts.sort()
print(body_parts)

# reverses items in list based on alphabet
body_parts = ["hands", "head", "neck", "hip",
              "toe", "eyes", "nails", "knee", "arms"]
body_parts.sort(reverse=True)
print(body_parts)

# reverses items in list based on how it's original displayed
body_parts = ["hands", "head", "neck", "hip",
              "toe", "eyes", "nails", "knee", "arms"]
body_parts.reverse()
print(body_parts)

# think of sorted() as a preview that shows the changed list but the OG list itself has not been changed like that
body_parts = ["hands", "head", "neck", "hip",
              "toe", "eyes", "nails", "knee", "arms"]
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

nums = [1, 2, 3, 4, 5, 6]
print(nums[2:5])

vehicles = ["car", "truck", "bike", "train", "plane", "limo"]
print(vehicles[2:5])

players = ["bob", "steve", "michael", "tom", "eli"]
print("These are the players in the team: ")
for player in players[0:3]:
    print(player.title())

vehicles = ["car", "truck", "bike", "train", "plane", "limo"]
print("My favourite means of transport are: ")
for vehicle in vehicles[1:5]:
    print(vehicle)

cities = ["New York", "Leeds", "Manchester", "Bristol", "Liverpool", "Kigali"]
print("Print out the British cities only: ")
for city in cities[1:5]:
    print(city)

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(number_list[1:10:2])

tv_shows = ["arthur", "biker grove", "hey arnold",
            "big cook little cook", "powerpuff girls"]
print("These are cartoons: ")
print(tv_shows[0:5:2])

print("These are NOT cartoons: ")
for non_cartoon in tv_shows[1:4:2]:
    print(non_cartoon)

clothes = ["hat", "scarf", "shoes", "socks",
           "belt", "shirt", "sunglasses", "shorts"]
print(clothes[2:8])
for clothing in clothes[2:8]:
    print(clothing)

clothes = ["hat", "scarf", "shoes", "socks",
           "belt", "shirt", "sunglasses", "shorts"]
print(clothes[1:8:2])

get_odd_nums_only = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(len(get_odd_nums_only))
print(get_odd_nums_only[0:len(get_odd_nums_only):3])
for odd_num in get_odd_nums_only[0:9:3]:
    print(odd_num)

# 1.
one_to_eight_nums = [1, 2, 3, 4, 5, 6, 7, 8]
print(one_to_eight_nums[2:5])
for single_num in one_to_eight_nums[2:5]:
    print(single_num)

# 2.
get_odd_nums_only = [1, 2, 3, 4, 5, 6, 7, 8]
print(get_odd_nums_only[0:8:2])
for odd_num in get_odd_nums_only[0:8:2]:
    print(odd_num)

x = 24 + 88
print(x)

x = 4
y = 8
z = x + y
print(z)

x = 405
y = 89
z = x - y
print(z)

x = 5
y = 10
z = x - y
print(z)

x = 405 / 5
print(x)
print(int(x))

x = 3 * 11
print(x)

x = 2
y = 5
z = (x * y) + (y / x)
print(z)

print(3 ** 2)

x = 2
y = 5
z = x ** y
print(z)

x = 2 ** 8
print(x)

a = 1
a += 5
print(a)

a = 10
a -= 6
print(a)

a = 3
a *= 4
print(a)

a = 200
a /= 5
print(a)
print(int(a))

a = 2
a **= 3
print(a)

b = 3
c = 4
print(b == c)

b = 30
c = 30
print(b == c)

b = "30"
c = 30
print(b == c)

b = 67
c = 67
print(b != c)

b = 89
c = 5
print(b != c)

b = 100
c = 60
print(b > c)

b = 2
c = 78
print(b > c)

b = 1
c = 55
print(b < c)

b = 66
c = 3
print(b < c)

b = 66.98
c = 66.92
print(b < c)

d = 66.98
e = 66.92
print(d <= e)

d = 66.98
e = 66.98
print(d <= e)

d = 5
e = 10
print(d >= e)

d = 500
e = 10
print(d >= e)

d = 3.0
e = 3
print(d >= e)

f = 4
print(f > 3 and f > 9)

f = 10
print(f > 3 and f > 9)

f = 20
print(f > 50 and f > 30)

f = 5
print(f < 50 and f > 3)

f = 58
print(f > 10 and f < 4)

f = 7
print(f > 2 or f > 8)

f = 5
print(f < 2 or f > 8)

f = 11
print(f < 89 or f > 90)

f = 11
print(f > 89 or f < 90)

f = 11
print(f > 89 or f > 90)

f = 11
print(f < 89 or f < 90)

f = 10
print(not(f > 80 and f > 90))

g = 5
h = 3
i = g
j = h

print("g is h: " + str(g is h))
print("h is g: " + str(h is g))

print("g is i: " + str(g is i))
print("i is g: " + str(i is g))

print("h is i: " + str(h is i))
print("h is g: " + str(h is g))

print("j is h: " + str(j is h))
print("h is j: " + str(h is j))

h = 99
print(j)
print("j is h: " + str(j is h))

k = 1
l = 2
m = 3
n = k
o = l

print(o is not k)
print(o is not l)
print(n is not l)
print(n is not k)

print(l is not o)
print(l is not m)
print(l is not k)

print(k is not n)
print(k is not m)
print(k is not l)

body_parts = ["hands", "head", "neck", "hip",
              "toe", "eyes", "nails", "knee", "arms"]

print("teeth" in body_parts)
print("arms" in body_parts)
print("feet" in body_parts)
print("hands" in body_parts)

fruits = ["apple", "pear", "lemon", "peach", "passionfruit"]

print("passionfruit" not in fruits)
print("coconut" not in fruits)
print("apple" not in fruits)
print("fish" not in fruits)
print("watermelon" not in fruits)

a = 24
b = 60
print(a & b)
print(bin(a))
print(bin(b))

x = 223
y = 111
print(x & y)
print(bin(x))
print(bin(y))

a = 24
b = 60
print(a | b)
print(bin(a))
print(bin(b))

x = 223
y = 111
print(x | y)
print(bin(x))
print(bin(y))

a = 24
b = 60
print(a ^ b)
print(bin(a))
print(bin(b))

x = 223
y = 111
print(x ^ y)
print(bin(x))
print(bin(y))

print(10 % 2)
print(11 % 2)

a = 10
b = 2
c = a // b
print(c)

# 1.
a = 7 + (4 * 3) - 9 / 5 + 2 ** 2
print(a)


a = 2
b = 4
c = 3

print(a * a + c)
print(a + b * c)
print(a * b + c)
print(a / b * c)
print(a - b + c)

x = 50
y = 400
if x > y:
    print("x is bigger than y")
else:
    print("x is smaller than y")

z = 1
a = 10

if z > a:
    print("z is bigger than a")
elif z == a:
    print("z and a are the SAME")
else:
    print("z is smaller than a")

z = 1000
a = 1000

if z > a:
    print("z is bigger than a")
elif z < a:
    print("z is smaller than a")
else:
    print("z and a are the SAME")

smoothie_ingredients = ["banana", "nuts", "ice-cream"]

if "banana" in smoothie_ingredients:
    print("you added banana to your smoothie")

if "nuts" not in smoothie_ingredients:
    print("DO NOT added nuts to the smoothie ")

if "nuts" in smoothie_ingredients:
    print("you added nuts to your smoothie")

if "cake pieces" in smoothie_ingredients:
    print("added cake pieces to your smoothie")

if "ice-cream" in smoothie_ingredients:
    print("you added ice-cream to your smoothie")

print("enjoy your smoothie")

# 1.
temp = 11

if temp >= 75:
    print("today is a hot day")
elif temp <= 74 and temp > 11:
    print("today is a warm day")
else:
    print("today is a cold day")

fruits = ["apple", "pear", "lemon", "peach", "passionfruit"]
for fruit in fruits:
    print(fruit)

for single_num in range(5):
    print(single_num)

for single_num in range(0, 15):
    print(single_num)

for single_num in range(0, 11, 2):
    print(single_num)

# 1.
fav_foods = ["pizza", "cake", "sweets"]
for fav in fav_foods:
    print(fav)

# 2.
for odd_nums in range(1, 30, 2):
    print(odd_nums)

timer = 1
while timer < 4:
    print("you still have time")
    timer += 1
print("time's up!")

greeting = "hello, there everyone"
counter = 1
while counter < 5:
    print(greeting)
    counter += 1

# must be written like this to avoid infinite looping
x = 0
while x < 6:
    x += 1
    if x == 4:
        continue
    print(x)

x = 0
while x < 6:
    x += 1
    if x != 4:
        continue
    print(x)

figure_num = 5
while figure_num < 10:
    print(figure_num)
    figure_num += 1

number_again = 10
while number_again > 0:
    print(number_again)
    number_again -= 1

breaking = 0
while breaking < 10:
    breaking += 1
    if breaking == 2:
        continue
    if breaking == 7:
        break
    print(breaking)

a = 1
while a < 14:
    a += 1
    print(a)
    if a == 4:
        break

# 1.
encouragement = 0
while encouragement < 3:
    print("Great Job")
    encouragement += 1

# 2.
counting = 1
while counting < 11:
    print(counting)
    counting += 1
    if counting == 7:
        break
print("it's over")

a = 1
while a < 4:
    print(a)
    a += 1

outer = ["outer 1", "outer 2", "outer 3"]
inner = ["inner 1", "inner 2", "inner 3"]

for out in outer:
    print("--------------")
    for inn in inner:
        print(out, inn)

numbers = [1, 2, 3]
letters = ["a", "b", "c"]

for num in numbers:
    print("--------------")
    print(num)
    for letter in letters:
        print(letter)

outer = ["outer 1", "outer 2", "outer 3"]
inner = ["inner 1", "inner 2", "inner 3", "inner 4", "inner 5"]

for out in outer:
    print(out)
    print("--------------")
    for inn in inner:
        print(inn)
    print("\n")

# 1.
outer = ["outer 1", "outer 2", "outer 3"]
inner = ["inner 1", "inner 2", "inner 3", "inner 4", "inner 5"]

for out in outer:
    print("--------------")
    print(out)
    print("--------------")
    for inn in inner:
        print(inn)

a = open("first_python/text_files/demo.txt", "r")
print(a.read())
a.close()

a = open("first_python/text_files/demo.txt", "r")
print(a.readline())
a.close()

a = open("first_python/text_files/demo.txt", "r")
print(a.read(7))
a.close()

a = open("first_python/text_files/demo.txt", "r")
print(a.read(3))
a.close()

with open("first_python/text_files/demo.txt") as myFile:
    contents = myFile.read()
    print(contents)

##################################################################################################################
# opens file and appends .write() text in the demo.txt file
a = open("first_python/text_files/demo.txt", "a")
a.write("\nHere is another line in our text file")
a.close()

# this opens the file with the newly appended text take from the .write() method in the code above
with open("first_python/text_files/demo.txt") as myFile:
    contents = myFile.read()
    print(contents)
##################################################################################################################

##################################################################################################################
with open("first_python/text_files/demo.txt") as myFile:
    contents = myFile.read()
    print(contents)

a = open("first_python/text_files/demo.txt", "w")
a.write("this will overwrite the text in the demo.txt file!")
a.close()

with open("first_python/text_files/demo.txt") as myFile:
    contents = myFile.read()
    print(contents)
##################################################################################################################

y = open("", "x")

# 1.
new_file = open("first_python/text_files/new_file.txt", "x")
new_file.close() # needed!

new_file = open("first_python/text_files/new_file.txt", "a") # "a" not "w"
new_file.write("this text was written for the practice task")
new_file.close()

new_file = open("first_python/text_files/new_file.txt", "r")
print(new_file.read())
new_file.close()

with open("first_python/text_files/new_file.txt") as myFile:
    contents = myFile.read()
    print(contents)

# 2.
new_file2 = open("first_python/text_files/new_file2.txt", "x")
new_file2.close() # needed!

start = 1
new_file2 = open("first_python/text_files/new_file2.txt", "a") # "a" not "w"
while start < 4:
    new_file2.write(
        "this will overwrite the text in the new_file2.txt file! \n")
    start += 1
new_file2.close()

new_file2 = open("first_python/text_files/new_file2.txt", "r")
print(new_file2.read())
new_file2.close()

import shutil
src = "first_python/text_files/demo3.txt"  # must be an existing file in directory to create new file below
dat = "first_python/text_files/demo4.txt" # creates new file
shutil.copy(src, dat) # copy's file

import os
# renames file
os.rename("first_python/text_files/demo4.txt", "first_python/text_files/LetItBe.txt")

import os
# deletes files
os.remove("first_python/text_files/LetItBe.txt")


# 1.
import shutil
src = "first_python/text_files/demo3.txt"
dat = "first_python/text_files/carefulWhatYouWishFor.txt"
shutil.copy(src, dat)

import os
os.rename("first_python/text_files/carefulWhatYouWishFor.txt", "first_python/text_files/writtenInTheStars.txt")


# 2.
new_file = open("first_python/text_files/writtenInTheStars.txt", "x")
new_file.close()

start2 = 1
new_file2 = open("first_python/text_files/writtenInTheStars.txt", "a")
while start2 < 4:
    new_file2.write(
        "here are a few lines of text for the written in the stars text file \n")
    start2 += 1
new_file2.close()

import shutil
src = "first_python/text_files/writtenInTheStars.txt"
dat = "first_python/text_files/carefulWhatYouWishFor.txt"
shutil.copy(src, dat)

new_file = open("first_python/text_files/carefulWhatYouWishFor.txt", "a")
new_file.write("appended new text to this copied file yay \n")
new_file.close()

new_file = open("first_python/text_files/writtenInTheStars.txt", "r")
print(new_file.read())
new_file.close()

new_file = open("first_python/text_files/carefulWhatYouWishFor.txt", "r")
print(new_file.read())
new_file.close()


with open("first_python/text_files/hello.txt", "w") as file:
    file.write("hey there!")

x = open("first_python/text_files/text_files/hello.txt", "r")
print(x.read())
x.close()


with open("first_python/text_files/names.txt", "r") as name_file:
    with open("first_python/text_files/messages.txt", "r") as message_file:
        body= message_file.read()
        for name in name_file:
            mail = "Hello " + name + body
            with open("first_python/text_files/" + name.strip() + ".txt", "w") as message_file:
                message_file.write(mail) 

with open("first_python/text_files/justine.txt", "r") as justine:
    print(justine.read())


txt = input("can you see this? yes or no")
print("you said:", txt)

txt = input("give me a number:")
num = int(txt)
print("the number you gave was:", num)

txt = int(input("give me a number:"))
print("the number you gave was:", txt)

txt = input("give me number please:")
try:
    num = int(txt)
    print("the number you gave was:", num)
except ValueError:
    print("please put in a real number, not a string or text")
    txt = input("PLEASE TRY AGAIN! give me another number please:")
num = int(txt)
print("the number you gave was:", num)

salary = 80000
txt = "you make £{} dollars a year"
print(txt.format(salary))

# {field_name:conversion} "{0, s}"

string = "Dave teaches {} {}."
print(string.format("cyber", "security"))

string2 = "The primary colours are: {}, {} and {}."
print(string2.format("red", "yellow", "blue"))

eating = "People like to eat {}, {} and {} on the {}th of December."
print(eating.format("turkey", "mashed potatoes", "chocolate pudding", 25))

dancing = "Dancing the {} requires {} people with {} outfits in a dancing {} with an {}."
print(dancing.format("hall", "audience", "sparkling", 2, "Cha Cha", "hall"))

dancing = "Dancing the {4} requires {3} people with {2} outfits in a dancing {5} with an {1}."
print(dancing.format("hall", "audience", "sparkling", 2, "Cha Cha", "hall"))

dancing = "Dancing the {4} requires {3} people with {adj_1} outfits in a dancing {4} with an {1}."
print(dancing.format("hall", "audience", 2, "Cha Cha", "hall", adj_1="sparkling"))

string = "Bob likes to play {act} and eat {1} {0}"
print(string.format("dogs", "hot", act="games"))

print("Bob likes to play {act} and eat {1} {0}".format("dogs", "hot", act="games"))

import sys
print("The name of our file is: ", (sys.argv[0]))

import sys
print("The name of our file is: ", (sys.argv[0]))
print("Number of arguments: ", len(sys.argv))
print("The arguments are: ", str(sys.argv))

############################################# Defining Functions #############################################
def first_function():
    x = 1
    while x < 4:
        print("Hello World!")
        x += 1
first_function()

def second_function(fname):
    print("Hello " + fname)
second_function("Justine")
second_function("Tracy")
second_function("Crash")

def third_function(food):
    print(f"I like to eat {food}.")
third_function("eggs")
third_function("fish")
third_function("beans")

def my_age(age):
    print(f"I'm {age} years old.")
my_age(2)
my_age(7)
my_age(56)

def greet():
    print("Hello there, how are you today?")
greet()

############################################# Using Default Argument #############################################

def student(fname, lname="Lawson", subject="ICT"):
    print(fname, lname, "studies", subject)
student("Tony")
student("Timmy", "Phillips", "Maths")
student("Paul", "Smith")

def greeting(name, msg="How are you today?"):
    print("Hey", name + "" + msg)
greeting(name="Andy. ", msg="Have you seen Paris?")
greeting(msg="Have you seen Paris?", name="Andy. ")
greeting("Sammie. ", msg="Have you seen Paris?")
greeting("Tracy. ")

############################################# Handling Exceptions #############################################

try:
    print(0/0) # ZeroDivisionError
except ZeroDivisionError:
    print("You cannot divide by zero :(")

number = int(input("put in a number between 1-10:"))
print("You put the number: ", number)  

import sys
try:
    num = int(input("put in a number between 1-10:"))
except ValueError:
    print("You didn't put in a number :(")
    print("Please use a number")
    sys.exit()
print("You put the number: ", num)  

import sys
try:
    num = int(input("put in a number between 1-10 below:\n"))
    if num <= 0:
        print("This number is too low!")
        sys.exit()
    if num >= 11:
        print("This number is too high!")
        sys.exit()
except ValueError:
    print("You didn't put in a number :(")
    print("Please use a number")
    sys.exit()
print("You put the number: ", num) 

############################################# Using Math and Random Modules #############################################

import random

print("prints a random number")
print(random.random())
print("\n")

print("prints a random float between the 2 given parameters")
print(random.uniform(89, 90))
print("\n")

print("prints a random number within range of the 2 given parameters")
print(random.uniform(2, 5))
print("\n")

randomise_list = ["apple", "banana", "citrus", "dragonfruit"]
random.shuffle(randomise_list)
print(randomise_list)
print("\n")

print("prints a random int number e.g: (0, 10) between 0 and 10 inclusively")
print(random.randint(1, 5))
print("\n")

print("prints a random int number e.g: (0, 10) between 0 and 9, 10 not included")
print(random.randrange(1, 5))
print("\n")

print("prints random ODD number")
print(random.randrange(1, 11, 2))
print("\n")

print("prints random EVEN number")
print(random.randrange(2, 11, 2))
print("\n")

print("random EVEN and ODD number")
print(random.randrange(1, 11, 2))
print(random.randrange(2, 11, 2))
print("\n")


import math

floor_num = float(input(print("Enter a number and I'll round it down to the ground for you :) ")))
print(str(floor_num) + " has been rounded down to " + str(math.floor(floor_num)) + ".")

square_num = int(input(print("Enter a number and I'll tell you the square root of the number :)")))
print(str(math.sqrt(square_num)) + " " + "is the square root of " + str(square_num) + ".")

print("rounds number upwards: ceil")
print(math.ceil(4.1))
print(math.ceil(5.7))
print(math.ceil(6.3))
print("\n")

print("rounds number downwards: floor")
print(math.floor(7.3))
print(math.floor(1.5))
print(math.floor(9.2))
print("\n")

print("prints square root of number")
print(math.sqrt(100))
print(math.sqrt(81))
print(int(math.sqrt(49)))
print("\n")

print("prints number to the power of")
print(math.pow(10,5))
print(math.pow(2,7))
print(math.pow(0,4))
print("\n")

print("prints remainder of x/y")
print(math.fmod(94,5))
print(math.fmod(15,7))
print(math.fmod(27,4))
print("\n")

from datetime import date
from datetime import time
from datetime import datetime

today = date.today()
date_time = datetime.now()
print("Today's date is: ", today)
print("All together now: ", date_time)


import os

directory_path = os.getcwd()
print("Your current directory is: " + directory_path)
foldername = os.path.basename(directory_path)
print("The directory name is: " + foldername)

import os
print("\n")
print(os.stat("app.py"))
print("\n")

print(float(16))

#Module 25 - Displaying Datetime and Working Directory

#import all your modules!

from datetime import date
from datetime import time
from datetime import datetime

today = date.today()
date_time = datetime.now()

print("Today's date is: ", today)
print("Can you be more specific please? ", date_time)
print("Break it down....")
print("The hour ", date_time.hour)
print("The minute ", date_time.minute)
print("The seconds ", date_time.second)

#Working directory
print("\n")
import os

dirpath = os.getcwd()
print("Your current working directory is: " + dirpath)

foldername = os.path.basename(dirpath)
print("The specific folder is: " + foldername)
