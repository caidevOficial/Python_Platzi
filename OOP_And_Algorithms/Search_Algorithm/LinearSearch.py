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


def linearSearch(myList, objetive, iter_lin=0):
    """
    Searches in the list, the objetive number in a iteratively way.
    """
    match = False

    for element in myList:
        iter_lin += 1
        if element == objetive:
            match = True
            break

    return (match, iter_lin)


def linear_Search():
    # ----- Config ----- #
    listSize = int(input("Tell me the size of the list: "))
    objetive = int(input("What number do you want to find?: "))

    # ----- Creates the list ----- #
    myList = sorted([rd.randint(0, 1500) for i in range(listSize)])
    (found, iter_lin) = linearSearch(myList, objetive)

    # ----- Message area ----- #
    print("# List generated #")
    print(myList)
    print(f'The element {objetive} {"is" if found else "is not"} in the list!')
    print(f'Iterations quantity of Linear search: {iter_lin}')


if __name__ == "__main__":
    linear_Search()
