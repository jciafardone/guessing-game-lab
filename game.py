"""A number-guessing game."""

# Put your code here
import random

print("Welcome to the Guessing Game!")

player_name = input("What is your name? ")
 
number = random.randint(1, 101)
print(number)