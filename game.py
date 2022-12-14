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



def computer_playing():
    secret_number = int(input("Choose a number between 1 and 20: "))
    print("I'm the computer. I'm going to guess a number.")
    # computer_guess = random.randint(1,21)
    min_parameter = 1
    max_parameter = 20

    computer_guess_attempts = []

    while True:
        computer_guess = random.randint(min_parameter, max_parameter)
        print(f"My guess is {computer_guess}.")
        next_guess = input("Was the computer too high, too low, or correct? ").lower()
        # if next_guess != "too high" or next_guess != "too low" or next_guess != "correct":
        #     print("Invalid answer.")
        if computer_guess not in computer_guess_attempts:
            print(next_guess)
            if next_guess == "too low":
                computer_guess_attempts.append(computer_guess)
                min_parameter = computer_guess
            elif next_guess == "too high":
                computer_guess_attempts.append(computer_guess)
                max_parameter = computer_guess
            elif next_guess == "correct":
                print("You won!")
                break
        # elif next_guess != "too high" or next_guess != "too low" or next_guess != "correct":
        # else:
        #     continue

#try, except, ValueError

computer_playing()
#number_guessing_game()