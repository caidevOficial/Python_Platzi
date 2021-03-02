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

# Goal: Understand stack frames iteratively.

import random as rd


def binSearch(myList, start, end, objetive, iter_bin=0):
    """
    Searches the objetive number in the list, if cannot find the number, it will make the list smaller to search again.
    """
    print(f'Searching {objetive} between {myList[start]} and {myList[end-1]}:')
    iter_bin+=1
    if start > end:
        return (False, iter_bin)
    middle = (start+end)//2 # divides the size into 2 to find the middle

    if myList[middle] == objetive:          # Found case
        return (True, iter_bin)
    elif myList[middle] < objetive:         # if the objetive number is bigger than the middle
        return binSearch(myList, middle+1, end, objetive, iter_bin=iter_bin)
    else:                                   # if the objetive number is smaller than the middle
        return binSearch(myList, start, middle-1, objetive, iter_bin=iter_bin)


def binarySearch():
    # ----- Config ----- #
    listSize = int(input("Tell me the size of the list: "))
    objetive = int(input("What number do you want to find?: "))

    # ----- Creates the list ----- #
    myList = sorted([rd.randint(0, 1500) for i in range(listSize)])
    (found,iter_bin) = binSearch(myList, 0, len(myList), objetive)

    # ----- Message area ----- #
    print("# List generated #")
    print(myList)
    print(f'The element {objetive} {"is" if found else "is not"} in the list!')
    print(f'Iterations quantity of binary search: {iter_bin}')


if __name__ == "__main__":
    binarySearch()
