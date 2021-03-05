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

##############################################################################################################################################################################
# Project #4
# Which is the largest of the given numbers

num1 = int(input("What is the first number? "))
num2 = int(input("What is the second number? "))
num3 = int(input("What is the third number? "))

if (num1 > num2) and (num1 > num3):
    largest = num1
elif (num2 > num1) and (num2 > num3):
    largest = num2
else:
    largest = num3

print("The largest number is", largest)

##############################################################################################################################################################################
# Project #5
# Alphabetical Order

words = input("Enter your words here: ")

words = words.split()
words.sort()

for word in words:
   print(word)

##############################################################################################################################################################################
# Project #6
# Dice Game

import random

question = input('Would you like to play, [y/n]? ')

while question != 'n':
    if question == 'y':
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print("Your rolled a...")
        print(die1," and ",die2)
        question = input('\nWould you like to roll again, [y/n]? ')
    else:
        print('Invalid response. Please type "y" or "n".')
        question = input('Would you like to try to roll the dice again[y/n]?\n ')

print('Thank you for playing - Good Bye!')

##############################################################################################################################################################################
# Project #7
# Using a word list, pick a random word


import random

# read all the list of words
words = []
with open('first_python/text_files/demo.txt', 'r') as file:
    line = file.readline().strip()
    words.append(line)
    while line:
        line = file.readline().strip()
        words.append(line)

random_index = random.randint(0, len(words))

print("Your random word is:", words[random_index])


###  OR  ###


print(random.choice(open("first_python/text_files/demo.txt").read().split()))

##############################################################################################################################################################################
# Project #8
# Create a Rock, Paper, Scissors game

import sys
import random

player_name = input("What's your name? ")
player_choice = input(
    f"{player_name.title()}, do you want to choose rock, paper or scissors? ")

options = ["rock", "paper", "scissors"]
computer_choice = random.choice(options)


def compare(player, com):
    if player == com:
        print("You chose: " + player)
        print("Computer chose: " + com)
        print("No one won!")
        return("It's a tie!")
    elif player == 'rock':
        if com == 'scissors':
            print("You chose: " + player)
            print("Computer chose: " + com)
            print("Rock wins!")
            return(player_name.title() + " is the winner!")
        else:
            print("Paper wins!")
            return("Computer is the winner!")
    elif player == 'scissors':
        if com == 'paper':
            print("You chose: " + player)
            print("Computer chose: " + com)
            print("Scissors win!")
            return(player_name.title() + " is the winner!")
        else:
            print("Rock wins!")
            return("Computer is the winner!")
    elif player == 'paper':
        if com == 'rock':
            print("You chose: " + player)
            print("Computer chose: " + com)
            print("Paper wins!")
            return(player_name.title() + " is the winner!")
        else:
            print("You chose: " + player)
            print("Computer chose: " + com)
            print("Scissors win!")
            return("Computer is the winner!")
    else:
        return("Something went wrong! You have not entered rock, paper or scissors, try again.")
        sys.exit()


print(compare(player_choice.lower(), computer_choice.lower()))
