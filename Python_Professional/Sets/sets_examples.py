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

# ?########## Print basic sets examples
set_example_1 = {1, 2, 3, (4, 5, 6)}
print(f'Set example 1: {set_example_1}')

set_example_2 = {1, 3, 'Hello World', True, 25.02, 2022}
print(f'Set example 2: {set_example_2}')

try:
    # !# This set it's wrong because the list is a mutable object.
    set_example_3 = {[1, 2, 3], 4}
    print(f'Set example 3: {set_example_3}')
except Exception as e:
    print(f'Error -> {e}')

# ?########## Print sets types
empty_set = set()
# *### There are two ways to print the type of a set:
print(f'Empty set using __class__: {empty_set.__class__}')
print(f'Empty set using type(): {type(empty_set)}')

# ?########## Regarding castings to set
# *### This is a good example to understand the casting to set.
# *### The casting to set is a good way to convert a list to a set.
list_example = [1, 2, 3, 4, 4, 4, 7, 7, 7, 10]
print(f'List example: {list_example}')
print(f'List example casted to set: {set(list_example)}')

# *### Also we can cast a tuple to set
tuple_example = (1, 2, 'Hello world', True, 25.02, 2022, 1, 2, 3)
print(f'Tuple example: {tuple_example}')
print(f'Tuple example casted to set: {set(tuple_example)}')

# ?########## Regarding update and intersection methods
# *### The update method is used to add elements to a set.
# *### The intersection method is used to find the common elements between two sets.
set_example_1.update([1, 2, 3, 4, 5, 6])
print(f'Set example 1 after update: {set_example_1}')

# *### The intersection method is used to find the common elements between two sets.
set_example_4 = set_example_2.intersection(set_example_1)
print(f'Set example 2 after intersection: {set_example_2}')

# *### The difference method is used to find the elements that are in the 
# *### first set but not in the second set.
set_example_5 = set_example_1.difference(set_example_2)
print(f'Set example 1 after difference: {set_example_5}')

# *### Also we can add multiple elements to a set using the update method.
set_example_1.update(['Hello', 'World', 'i am'], {'updating', 'the', 'set'}, [8, 10])
print(f'Set example 1 after update: {set_example_1}')

# ?########## Regarding set operations: Remove, discard
# *### The remove method is used to remove an element from a set.
set_example_1.discard(1)
print(f'Set example 1 after discard: {set_example_1}')
# *### The discard method is used to remove an element from a set if it exists.
# !# If the element doesn't exist, the discard method will not raise an error.
set_example_1.remove(2)
print(f'Set example 1 after remove: {set_example_1}')

# *### To remove all elements from a set, we can use the clear method.
set_example_1.clear()
print(f'Set example 1 after clear: {set_example_1}')