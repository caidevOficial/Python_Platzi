# Copyright (C) 2020 FacuFalcone - CaidevOficial.
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

def BuildsFormatTables():
    """
    Builds tables with all the possibles styles
    """
    for style in range(8):
        for textColor in range(30, 38):
            cad_cod = ''
            for backgroundColor in range(40, 48):
                fmto = ';'.join([str(style),
                                 str(textColor),
                                 str(backgroundColor)])
                cad_cod += "\033["+fmto+"m "+fmto+" \033[0m"
            print(cad_cod)
        print('\n')

# Test
BuildsFormatTables()