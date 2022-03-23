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

def bag(sizeBag: int, kilos: list, values: list, index: int):
    # Base Case 1
    if index == 0 or sizeBag == 0:
        return 0
    # Base Case 2
    elif kilos[index-1] > sizeBag:
        return bag(sizeBag, kilos, values, index-1)

    return max(values[index-1]+bag(sizeBag-kilos[index-1], kilos, values, index-1), bag(sizeBag, kilos, values, index-1))


if __name__ == "__main__":
    values = [60, 100, 120]
    kilos = [10, 20, 30]
    sizeBag = 50
    index = len(values)

    result = bag(sizeBag, kilos, values, index)
    print(result)
