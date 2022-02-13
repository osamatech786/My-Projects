'''
Guess the seasion
summer, autumn, fall, winter
31/03/2020
Core concepts: Dictinary data structure & Random module.
'''

import random as ra


# Title
print("\t*"*11)
print("\t"*4, "*"*30)
print("\t"*4, ""*4, " *"*13)
print("\t"*4, " "*5, "Guess the seasion")
print("\t"*4, ""*4, " *"*13)
print("\t"*4, "*"*30)
print("\t*"*11)


seasions = {
    1: "summer",
    2: "autumn",
    3: "fall",
    4: "winter"
}
seasion = seasions[ra.randrange(1, 5)]  # selects random season from dictionary


def process():
    var = input("\nEnter your guess here : ")
    check = var.isalpha()  # validates input
    if check == False:
        print("Wrong input")
        ch = int(input("Enter 1 for help and 2 to try again : "))
        if ch == 2:
            process()
        elif ch == 1:
            help()
            process()
        else:
            print("\nAGAIN WRONG INPUT!!!!")
            print("Check your keyboard!!!!")
            print("EXITING . . . .")
            exit()
    else:
        guess = var.lower()
        print(">>>", guess)
        if guess == seasion:
            print("Viola! You're right.")
            print(f"It's {seasion} :)")
            input("\n\nEnter any key to exit")
            exit()
        else:
            print("Sorry! Your guess is wrong :/")
            end()


def help():
    print("\n4 seasons are")
    for i in seasions:
        print(seasions[i])


def end():
    choice = int(input("Enter 1 to try again or 0 to exit & 3 for help : "))
    if choice == 0:
        print("Exiting . . . .")
        exit()
    elif choice == 1:
        process()
    elif choice == 3:
        help()
        process()
    else:
        print("Wrong input")
        end()


print("\nI'm thinking of a seasion, can u guess the name of that season?")
process()
