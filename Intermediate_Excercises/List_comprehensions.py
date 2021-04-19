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

def SimpleListFunction():
    """
    Simple excercise of lists
    """
    squares = []
    for i in range(1, 101):
        if (i%3 != 0):
            squares.append(i**2)
            print(f"{i} -> square: {i**2}")

def ListComprehension():
    squares = [i**2 for i in range(1,101) if i % 3 != 0]
    print("\nList Comprehension:\n")
    print(squares)

def ListComprehension_Hard():
    mults = [i for i in range(1,100000) if (i % 4 is 0 and i%6 is 0 and i%9 is 0)]
    print("\nList Comprehension: Mult of 4, 6 and 9\n")
    print(mults)

if __name__=='__main__':
    SimpleListFunction()
    ListComprehension()
    ListComprehension_Hard()