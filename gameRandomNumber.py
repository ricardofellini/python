## Author - Ricardo Jose Fellini


import random

def play():

    print("###########################")
    print("Welcome to the random game!")
    print("###########################")


    ##Declaration of variables

    number_secret = random.randrange(1, 101) ## Random number between 1 and 101
    total_try = 0
    points = 1000

    print("What is the chosen difficulty level?")
    print("(1) Easy | (2) Normal | (3) Hard ") ## Levels of the game

    level = int(input("Choose the level.: ")) # User types the desired level

    ## Conditions

    if(level == 1):
        total_try = 20
    elif(level == 2):
        total_try = 10
    else:
        total_try = 5

    for round in range (1, total_try + 1):
        print("Try {} de {}".format(round, total_try))

        chosen_number = int(input("Enter a number from 1 to 100.: "))
        print("You choose", chosen_number)

        if(chosen_number < 1 or chosen_number > 100):
            print("You must enter a number between 1 and 100")
            continue

        correct_number = chosen_number == number_secret
        bigger_number  = chosen_number >  number_secret
        smaller_number = chosen_number < number_secret

        if(correct_number):
            print("You won! And made {} points. ".format(points))
            break
        else:
            if(bigger_number):
                print("You missed, your number is greater than the correct number. ")
            elif(smaller_number):
                print("You missed, your number is smaller than the correct number.")

            lost_points = abs(number_secret - chosen_number)
            points = points - lost_points

    print("END GAME")

if(__name__ == "__main__"):
    play()




