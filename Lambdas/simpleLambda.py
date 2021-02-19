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

def simpleLambda(s:list, h:list, e:list, l:list, L:list, c:list, o:list, d:list, E:list):
    """
    Prints a message by decoding a hexa into a char.
    """
    msg = ''
    for li in map(lambda x: [
            chr(y) for y in x], [s, h, e, l, L, c, o, d, E]):
        for ch in li:
            msg += ch
    print(msg)


if __name__ == '__main__':
    s = [0x4d, 0x53, 0x41, 0x20, 0x3c]
    h = [0x33, 0x20, 0x50, 0x79, 0x74]
    e = [0x68, 0x6f, 0x6e, 0x20, 0x2d]
    l = [0x20, 0x72, 0x72, 0x68, 0x68]
    L = [0x40, 0x6d, 0x73, 0x61, 0x2e]
    c = [0x63, 0x6f, 0x6d, 0x2e, 0x61]
    o = [0x72, 0x20, 0x2d, 0x20, 0x6a]
    d = [0x6f, 0x69, 0x6e, 0x20, 0x75]
    E = [0x73, 0x20, 0x21, 0x21, 0x21]

    simpleLambda(s, h, e, l, L, c, o, d, E)
