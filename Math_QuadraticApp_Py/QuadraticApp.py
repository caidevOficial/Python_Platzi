# Copyright (C) 2021 <FacuFalcone - CaidevOficial>
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

from Polynomial_Mod.Polynomial import Polynomial as PM
from Points_Mod.Points import Points as P


def headerMessage(colorCode: str, colorPy: str, colorThon: str):
    """
    Prints in console the header of the Mini App
    """
    print(colorCode + " ####   Quadratic App  ####")
    print(colorCode + " #### " + colorPy + "     PYT" +
          colorThon + "HON     " + colorCode + " ####")
    print(colorCode + " #### By CaidevOficial ####")


def inputNumber(colorCode, string):
    """
    Request a number from the user.
    """
    number = input("\033[;36m" + "Write the " + string + " term: ")
    try:
        number = float(number)
    except:
        return False
    return number


def validateFirstTerm(colorWarning, termA):
    if(termA == 0):
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


def finalMessage(colorCode, poly: PM):
    """
    Prints in console the results of all equations.
    """
    print(colorCode+"\n### Roots ###")
    print(colorCode+"X1: ", poly.axis().xAxis())
    print(colorCode+"X2: ", poly.axis().yAxis())
    print(colorCode+"### Vertices ###")
    print(colorCode+"Vertice X: ", poly.vertice().xAxis())
    print(colorCode+"Vertice Y: ", poly.vertice().yAxis())


def QuadraticApp():
    """
    Computes the values of both roots, vertices and prints them to the console.
    """
    # Polynomial
    x_Axis = P(0, 0)
    y_Axis = P(0, 0)
    polyn = PM(0, None, None)

    # Colors
    code = "\033"
    colorError = code + "[1;31;40m"    # Red.
    colorWarning = code+"[1;33;40m"  # Yellow.
    colorResult = code+"[1;32;40m"   # Green.
    colorApp = code+colorResult              # Green.
    colorPy = code+"[1;34;40m"       # Blue
    colorThon = colorWarning            # Yellow

    # Message
    headerMessage(colorApp, colorPy, colorThon)

    # Inputs
    termA = inputNumber("\033[1;34;40m", "Ax²")     # Blue.
    if(not validateFirstTerm(colorWarning, termA)):
        termB = inputNumber("\033[1;35;40m", "Bx")  # Violet.
        termC = inputNumber("\033[1;36;40m", "C")   # Cyan.

        if(termA is False or termB is False or termC is False):
            print(colorError + "Something was wrong with at least one of the terms, try write the numbers again, please.")
        else:
            if(termA == 0):
                print(
                    "If the term A is 0, you will lose the quadratic term, leaving you with a linear equation.")
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

                    x_Axis.set_xAxis(x1)
                    x_Axis.set_yAxis(x2)

                    y_Axis.setter(xVertice, yVertice)

                    polyn(determinant, x_Axis, y_Axis)
                    finalMessage(colorResult, polyn)
    else:
        print("Please, restart the App!")


# Test
if __name__ == '__main__':
    QuadraticApp()
