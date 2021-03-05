# import run

# run.greet()

##############################################################################################################################################################################
# Project #1
# Simple Calculator

print("Welcome to the state of the art calculator!\n")
print("What are doing?\n")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

operator = input("\nPick a number from the list above: ")

num_1 = input("\nPlease input the first number: ")
num_2 = input("Please input the second number: ")

if operator == '1':
    answer = str(int(num_1) + int(num_2))
    print(num_1, "+", num_2, "=", answer)

elif operator == '2':
    answer = str(int(num_1) - int(num_2))
    print(num_1, "-", num_2, "=", answer)

elif operator == '3':
    answer = str(int(num_1) * int(num_2))
    print(num_1, "*", num_2, "=", answer)

elif operator == '4':
    answer = str(int(num_1) / int(num_2))
    print(num_1, "/", num_2, "=", answer)

else:
    print("Something went wrong - make sure to use only numbers and symbols!")

##############################################################################################################################################################################
# Project #3
# Multiplication Table for one please

num = int(input("Display a multiplication table for which number? "))
print("------------------------------------------------------------")
for x in range(1, 13):
    print(num, 'x', x, '=', num*x)
