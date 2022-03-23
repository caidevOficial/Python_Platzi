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

import random as rd


def mergeSort(myList: list):
    """
    Sorts the entire list by creating smallers sublist and re-combines them. Divide and conquer!
    """
    if (len(myList) > 1):
        middle = len(myList)//2
        leftList = myList[:middle]
        rightList = myList[middle:]
        print(leftList, '*'*5, rightList)

        # Recursion
        mergeSort(leftList)
        mergeSort(rightList)

        # Iterators to cycle through the two sublists.
        i = 0
        j = 0
        # main list iterator
        k = 0

        while i < len(leftList) and j < len(rightList):
            if leftList[i] < rightList[j]:
                myList[k] = leftList[i]
                i += 1
            else:
                myList[k] = rightList[j]
                j += 1
            k += 1

        while i < len(leftList):
            myList[k] = leftList[i]
            i += 1
            k += 1

        while j < len(rightList):
            myList[k] = rightList[j]
            j += 1
            k += 1

        # To show step by step the making of the final list.
        print(f'Left List: {leftList}, Right List {rightList}')
        print(myList)
        print('-'*10)

        return myList


if __name__ == "__main__":
    listSize = int(input("Tell me the size of the list: "))
    numbers = [rd.randint(0, 100) for i in range(listSize)]

    print("List before the sort:")
    print(numbers)
    print("\nList After being sorted:")
    print(mergeSort(numbers))
