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

set_example_2 = {1, 3, 'Hello World', True, 2, (4, 5)}
print(f'Set example 2: {set_example_2}')

# ?###### Unions
# *###### There are two ways to do this:
set_union = set_example_1 | set_example_2
set2_union = set_example_1.union(set_example_2)
print(f'First way union: {set_union}')
print(f'Second way union: {set2_union}')

# ?###### Intersections
# *###### There are two ways to do this:
set_intersection = set_example_1 & set_example_2
set2_intersection = set_example_1.intersection(set_example_2)
print(f'First way intersection: {set_intersection}')
print(f'Second way intersection: {set2_intersection}')

# ?###### Difference
# *#### From the first set we can remove all the elements from the second set.
# *###### There are two ways to do this:
set_difference = set_example_1 - set_example_2
set2_difference = set_example_2.difference(set_example_1)
print(f'First way difference: {set_difference}')
print(f'Second way difference: {set2_difference}')

# ?###### Symmetric difference
# *###### From the first set we can remove all the elements that exist in both sets.
# *###### There are two ways to do this:
set_symmetric_difference = set_example_1 ^ set_example_2
set2_symmetric_difference = set_example_2.symmetric_difference(set_example_1)
print(f'First way symmetric difference: {set_symmetric_difference}')
print(f'Second way symmetric difference: {set2_symmetric_difference}')
