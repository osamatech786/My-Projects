# 27th Feb 2022
# Task:
# Number Guessing Game
# game will ask the user to guess a number between 1 and 100
# check with your secret number if the guess is right
# if he made a wrong guess check if the guess was smaller than your secret number
# if its small, change the lower limit. If it's larger change the upper limit
# give user a total of five tries to guess the secret number
# at the end ask the user if he wants to play the game again

import random as r

welcome_text = "\nWelcome to Guessing Game :)"
print(f"{welcome_text}\n", '*'*len(welcome_text), '\n', sep='')


def game():
    lower_limit, upper_limit = 1, 100
    secret_num = r.randrange(1, 101)
    chance = 5

    while chance >= 0:
        guess = int(
            input(f"\nEnter your guess between {lower_limit} and {upper_limit}: "))
        chance -= 1

        if guess != secret_num and chance > 0:                  # wrong choice
            print(f"Left chances: {chance}")
            if guess > secret_num:
                upper_limit = guess
            else:
                lower_limit = guess
        elif guess != secret_num and chance == 0:               # loose
            choice = input(
                f"\nSorry but no more chance left\nSecret Number was: {secret_num}\n\nWould you like to restart? (y/n)\n")
            if choice.lower() == 'y':
                print("Keep going and Never give up!")
                game()
            else:
                print("Better luck next time :)")
                exit()
        else:                                                   # win
            print('\n\n', '*'*10, "Congratulations! Your guess is correct.", '*'*10)
            choice = input("\nWould you like to play again? (yes/no)\n")
            if choice.lower() == 'yes':
                game()
            else:
                print("Take care :)")


game()
