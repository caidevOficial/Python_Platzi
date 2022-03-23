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

def remove_duplicates(my_list: list) -> list:
    """
    Remove duplicates from a list and return a new list
    without the duplicated elements.
    """
    without_duplicates: list = []
    for element in my_list:
        if element not in without_duplicates:
            without_duplicates.append(element)
    without_duplicates.sort()
    return without_duplicates

def remove_duplicates_to_set(my_list: list) -> set:
    """
    Remove duplicates from a list and return a new list
    without the duplicated elements.
    """
    return list(set(my_list))

def run():
    my_list = [rd.randint(0, 8) for x in range(10)]
    print(f'List: {my_list}')
    print(f'Without duplicates: {remove_duplicates(my_list)}')
    print(f'Without duplicates using set: {remove_duplicates_to_set(my_list)}')

if __name__ == "__main__":
    run()