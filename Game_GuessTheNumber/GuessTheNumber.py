import random

def GuessThePyNumber():
    """
    Mini game where you need to guess the number choosen by the machine.
    """
    randomNumber = random.randint(1,101)
    lifes = 10
    choosenNumber = int(input("Please, choose a number between 1-100: "))
    while (choosenNumber!= randomNumber):
        if(choosenNumber<randomNumber):
            print("-> The number is bigger! select wisely <-")
            lifes-=1
        else:
            print("-> The number is smaller! select wisely <-")
            lifes-=1
        if (lifes==0):
            print("Game over buddy, the number was: ",randomNumber, " Beter luck next time!")
            break
        else:
            print("Be careful, you have",lifes,"lifes left!")
            choosenNumber = int(input("\nPlease, choose a number between 1-100: "))
    print("\nFinally! you won the game, congratz!\nThe number was ",randomNumber)

# Test
GuessThePyNumber()