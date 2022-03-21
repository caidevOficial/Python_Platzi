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


def headerMessage(colorCode: str, colorPy: str, colorThon: str) -> None:
    """
    Prints in console the header of the Mini App
    """
    print(f"{colorCode} ####   Quadratic App  ####")
    print(f"{colorCode} #### {colorPy}     PYT{colorThon}HON     {colorCode} ####")
    print(f"{colorCode} #### By CaidevOficial ####")


def inputNumber(string: str):
    """
    Request a number from the user.
    """
    number = input(f"\033[;36mWrite the {string} term: ")
    try:
        number = float(number)
    except:
        return False
    return number


def validateFirstTerm(colorWarning: str, termA: int):
    """
    Validates the first term of the equation is zero (returns true) or a bigger number (returns false).
    """
    if(termA == 0):
        print(f"{colorWarning}If the quadratic term is 0, then the polynomial loses its degree 2 \nand will become a linear formula, it does not make sense \nto keep asking you for numbers.")
        return True
    return False


def calculateDeterminant(termA: int, termB: int, termC: int):
    """
    Calculates the determinant and returns the correct value or -1 if is a negative number.
    """
    firstCalc: float = math.pow(termB, 2) - (4*termA*termC)
    if(firstCalc < 0):
        return -1
    else:
        determinant: float = math.sqrt(firstCalc)
        return determinant


def calculateXVertice(termA: int, termB: int):
    """
    Calculates the value of the vertice X.
    """
    vertice: float = ((-termB)/(2*termA))
    return vertice


def calculateYVertice(termA: int, termB: int, termC: int, xVertice: float):
    """
    Calculates the value of the vertice Y.
    """
    vertice = ((termA*(pow(xVertice, 2)) + (termB*xVertice) + termC))
    return vertice


def finalMessage(colorCode: str, poly: PM):
    """
    Prints in console the results of all equations.
    """
    print(f"{colorCode}\n### Roots ###")
    print(f"{colorCode}X1: {poly.axis().xAxis()}")
    print(f"{colorCode}X2: {poly.axis().yAxis()}")
    print(f"{colorCode}### Vertices ###")
    print(f"{colorCode}Vertice X: {poly.vertice().xAxis()}")
    print(f"{colorCode}Vertice Y: {poly.vertice().yAxis()}")


def QuadraticApp():
    """
    Computes the values of both roots, vertices and prints them to the console.
    """
    # Polynomial
    x_AxisObject = P(0, 0)
    y_AxisObject = P(0, 0)
    polyn = PM(0, None, None)

    # Colors
    code = '\u001b'
    colorError = f"{code}[1;31;40m"     # Red.
    colorWarning = f"{code}[1;33;40m"   # Yellow.
    colorResult = f"{code}[1;32;40m"    # Green.
    colorApp = f"{colorResult}"         # Green.
    colorPy = f"{code}[1;34;40m"        # Blue
    colorThon = colorWarning            # Yellow

    # Message
    headerMessage(colorApp, colorPy, colorThon)

    # Inputs
    termA = inputNumber("Ax²")     # Blue.
    if(not validateFirstTerm(colorWarning, termA)):
        termB = inputNumber("Bx")  # Violet.
        termC = inputNumber("C")   # Cyan.

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

                    x_AxisObject.xAxis = x1
                    x_AxisObject.yAxis = x2

                    # !Fix ASAP
                    # y_AxisObject.setter(xVertice, yVertice)

                    polyn(determinant, x_AxisObject, y_AxisObject)
                    finalMessage(colorResult, polyn)
    else:
        print("Please, restart the App!")


# Test
if __name__ == '__main__':
    QuadraticApp()
