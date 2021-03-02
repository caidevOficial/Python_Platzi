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


def insertionSort(myList: list):

    for index in range(1, len(myList)):
        actualValue = myList[index]
        actualPosition = index

        while actualPosition > 0 and myList[actualPosition - 1] > actualValue:
            myList[actualPosition] = myList[actualPosition - 1]
            actualPosition -= 1

        myList[actualPosition] = actualValue
    return myList


if __name__ == "__main__":
    listSize = int(input("Tell me the size of the list: "))
    numbers = [rd.randint(0, 100) for i in range(listSize)]
    
    print("List before the sort:")
    print(numbers)
    print("\nList After being sorted:")
    print(insertionSort(numbers))
