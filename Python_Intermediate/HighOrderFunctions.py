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

from functools import reduce as rd


def oddNumbersUsingFilter(myList: list) -> list:
    """
    Simple filter function for odds numbers using filter and lambda.
    """
    odd = list(filter(lambda x: x % 2 != 0, myList))
    return odd


def cubeUsingMap(myList: list) -> list:
    """
    Simple map function for cube of numbers in the list using map and lambda.
    """
    odd = list(map(lambda x: x**3, myList))
    return odd


def reduceNumbers(myList: list) -> list:
    """
    Simple reduce function for numbers in the list using reduce and lambda.
    """
    allMultiplied = rd(lambda a, b: a*b, myList)
    return allMultiplied


if __name__ == '__main__':
    myList = [1, 2, 5, 4, 3]
    myList = sorted(myList)

    print(oddNumbersUsingFilter(myList))
    print(cubeUsingMap(myList))
    print(reduceNumbers(myList))
