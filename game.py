"""A number-guessing game."""

# Put your code here
import random


def greeting():
    player_name = input("What is your name? ")
    return player_name

def number_guessing_game():
    print("Welcome to the Guessing Game!")

    player_name = greeting()
    print(f"Hello {player_name}! You get 10 tries to guess a secret number.")

    lowest_score = None

    while True:
        min_range = int(input("What is the lowest number to guess? "))
        max_range = int(input("What is the highest number to guess? "))
        number = random.randint(min_range, max_range)

        player_guess = None

        number_of_guesses = 0

        while number_of_guesses < 10:
            print()
            print(f"You've used {number_of_guesses} out of 10 guesses.")
            print()

            try: 
                player_guess = int(input("Guess the secret number: "))

            except: 
                print(f"Please enter a valid integer between {min_range} and {max_range}!")
                continue
            
            if player_guess not in range(min_range, max_range):
                print(f"Please enter a number between {min_range} and {max_range}.")

            elif player_guess > number:
                print("You guessed too high.")
                number_of_guesses += 1

            elif player_guess < number:
                print("You guessed too low.")
                number_of_guesses += 1

            else:
                number_of_guesses += 1
                print(f"You guessed correctly! The number is {number}. It took {number_of_guesses} tries to get the right number.")
                break
                
                
        if lowest_score == None:
            lowest_score = number_of_guesses
        elif number_of_guesses < lowest_score:
            lowest_score = number_of_guesses
        print(f"The best attempt is {lowest_score} tries.")

        continue_game = input("Do you want to play again? (Y/N) ")
        if continue_game == "Y":
            print("Lets try again!")
            continue
        else:
            print("Thanks for playing!")
            break



number_guessing_game()