# MIT License

# Copyright (c) 2022 [FacuFalcone]

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import random as rd

def basic_generator():
    """
    Basic generator example.
    """
    print("Start of the generator")
    counter = 0
    yield counter

    print("Middle of the generator")
    counter = 1
    yield counter

    print("End of the generator")
    counter = 2
    yield counter

if __name__ == '__main__':
    basic_gen = basic_generator()

    for _ in range(3):
        next(basic_gen)
    
    # ?## Another way to create a generator bassed in a list.
    basic_list = [rd.randint(0, 20) for x in range(10)]
    iter_double_values = (x*2 for x in basic_list)

    for number in iter_double_values:
        print(number)
