import random

# Title
print("\t*"*11)
print("\t"*4, " *"*13)
print("\t"*5, "Luck Tester")
print("\t"*5, "*"*11)
print("\t*"*11)


n1, n2 = int(input(
    "Enter your 2 Most Favourite/Lucky numbers EXCEPT Binary (0 & 1) \n")), int(input())


def luck():
    g = 0
    ng = 0
    l = [0, 1]
    l.append(n1)
    l.append(n2)
    for i in l:
        n = random.choice(l)

        if(n == n1 or n == n2):
            g += 1
        else:
            ng += 1

    # percentage: obtained/total*100
    print("\nYour good luck is : ", str(int(g/len(l)*100))+'%')
    print("Your bad luck is  : ", str(int(ng/len(l)*100))+'%')

    if(g == 4):
        # 100/0
        print("\nUnbeliveable!!!! :O")
        print("You are 100% lucky right now\n\n")
    elif(g == 3):
        # 75/25
        print("\nHurrah Kudos :D")
        print("You are Stronger than your Bad Luck\n\n")
    elif(g == 2):
        # 50/50
        print("\nBad luck isn't stronger than you :)\n\n")
    elif(g == 1):
        # 25/75
        print("\nYou just need to believe in yourself :)\n\n")
    else:
        # 0/100
        print("\nThink good and good will happen\n\n")


luck()


def end():
    ch = int(input("Enter 1 to test again OR 0 to exit : "))
    if(ch == 1):
        luck()
        end()
    elif(ch == 0):

        exit()
    else:
        print("Don't be sad and Enter Correct number :/")
        end()


end()
