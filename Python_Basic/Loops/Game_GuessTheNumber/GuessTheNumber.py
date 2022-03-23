# MIT License
#
# Copyright (c) 2021 [FacuFalcone]
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import random

def GuessThePyNumber():
    """
    Mini game where you need to guess the number choosen by the machine.
    """
    randomNumber = random.randint(1, 101)
    lifes = 10
    choosenNumber = int(input("Please, choose a number between 1-100: "))
    while (choosenNumber != randomNumber):
        if(choosenNumber < randomNumber):
            print("-> The number is bigger! select wisely <-")
        else:
            print("-> The number is smaller! select wisely <-")
        lifes -= 1
        if (lifes == 0):
            print(f"Game over buddy, the number was: {randomNumber}")
            print("Beter luck next time!")
            break
        else:
            print(f"Be careful, you have {lifes} lifes left!")
            choosenNumber = int(input("\nPlease, choose a number between 1-100: "))
    print(f"\nFinally! you won the game, congratz!\nThe number was {randomNumber}")


if __name__ == "__main__":
    GuessThePyNumber()
