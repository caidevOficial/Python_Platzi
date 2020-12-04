# Copyright (C) 2020 FacuFalcone - CaidevOficial.
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

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