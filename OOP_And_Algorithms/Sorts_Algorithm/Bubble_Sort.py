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

def bubbleSort(myList:list):
    """
    Sorts the list in Ascendant mode and returns it properly sorted.
    """
    listLen = len(myList)

    for i in range(listLen):
        for j in range(0, listLen-i-1): # O(n) * O(n) = O(n*n) = O(n**2)
            if (myList[j]>myList[j+1]):
                myList[j], myList[j+1] = myList[j+1], myList[j]
    return myList        

if __name__ == "__main__":
    listSize = int(input("Tell me the size of the list: "))

    numbers = [rd.randint(0,100) for i in range(listSize)]
    print("List before the sort:")
    print(numbers)
    print("\nList After being sorted:")
    print(bubbleSort(numbers))