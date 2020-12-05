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

import math


def headerMessage(colorCode, colorPy, colorThon):
    """
    Prints in console the header of the Mini App
    """
    print(colorCode + "####   Quadratic App  ####")
    print(colorCode + "#### " + colorPy + "     PYT" +
          colorThon + "HON     " + colorCode + " ####")
    print(colorCode + "#### By CaidevOficial ####")


def inputNumber(colorCode, string):
    """
    Request a number from the user.
    """
    number = input(colorCode + "Write the " + string + " term: ")
    try:
        number = int(number)
    except:
        return False
    return number


def validateFirstTerm(colorWarning, termA):
    if(termA is 0):
        print(colorWarning + "If the quadratic term is 0, then the polynomial loses its degree 2 \nand will become a linear formula, it does not make sense \nto keep asking you for numbers.")
        return True
    return False


def calculateDeterminant(termA, termB, termC):
    """
    Calculates the determinant and returns the correct value or -1 if is a negative number.
    """
    firstCalc = math.pow(termB, 2) - (4*termA*termC)
    if(firstCalc < 0):
        return -1
    else:
        determinant = math.sqrt(firstCalc)
        return determinant


def calculateXVertice(termA, termB):
    """
    Calculates the value of the vertice X.
    """
    vertice = ((-termB)/(2*termA))
    return vertice


def calculateYVertice(termA, termB, termC, xVertice):
    """
    Calculates the value of the vertice Y.
    """
    vertice = ((termA*(pow(xVertice, 2)) + (termB*xVertice) + termC))
    return vertice


def finalMessage(colorCode, x1, x2, xVertice, yVertice):
    """
    Prints in console the results of all equations.
    """
    print(colorCode+"\n### Roots ###")
    print(colorCode+"X1: ", x1)
    print(colorCode+"X2: ", x2)
    print(colorCode+"### Vertices ###")
    print(colorCode+"Vertice X: ", xVertice)
    print(colorCode+"Vertice Y: ", yVertice)

def QuadraticApp():
    """
    Computes the values of both roots, vertices and prints them to the console.
    """
    colorError = "\033[1;31;40m"    # Red.
    colorWarning = "\033[1;33;40m"  # Yellow.
    colorResult = "\033[1;32;40m"   # Green.
    colorApp = "\033[1;32;40m"      # Green.
    colorPy = "\033[1;34;40m"       # Blue
    colorThon = "\033[1;33;40m"     # Yellow
    headerMessage(colorApp, colorPy, colorThon)
    termA = inputNumber("\033[1;34;40m", "Ax²")     # Blue.
    if(not validateFirstTerm(colorWarning, termA)):
        termB = inputNumber("\033[1;35;40m", "Bx")  # Violet.
        termC = inputNumber("\033[1;36;40m", "C")   # Cyan.

        if(termA is False or termB is False or termC is False):
            print(colorError + "Something was wrong with at least one of the terms, try write the numbers again, please.")
        else:
            if(termA == 0):
                print("")
            else:
                determinant = calculateDeterminant(termA, termB, termC)
                if(determinant == -1):
                    print(
                        colorWarning + "The determinant is negative, \nso it is not possible to find a square root, \ntherefore it has imaginary roots!")
                else:
                    x1 = round(((-termB + determinant)/(2*termA)), 2)
                    x2 = round(((-termB - determinant)/(2*termA)), 2)
                    xVertice = round(calculateXVertice(termA, termB), 2)
                    yVertice = round(calculateYVertice(
                        termA, termB, termC, xVertice), 2)

                    finalMessage(colorResult, x1, x2, xVertice, yVertice)

# Test
QuadraticApp()
