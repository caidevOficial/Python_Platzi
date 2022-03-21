# Copyright (C) <2021 FacuFalcone - CaidevOficial>
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

from Points_Mod import Points

class Polynomial:
    __determinant: float = None
    __axis: Points = None
    __vertices: Points = None

    def __init__(self, determinant, axis:Points, vertices:Points):
        """
        Builds the polynomial.
        """
        self.determinant = determinant
        self.axis = axis
        self.vertices = vertices
    
# Getters
    @property
    def determinant(self):
        """
        Gets the determinant of the polynomial.
        """
        return self.__determinant

    @property
    def axis(self):
        """
        Gets the axis of the polynomial.
        """
        return self.__axis

    @property
    def vertices(self):
        """
        Gets the vertices of the polynomial.
        """
        return self.__vertices

# Setters

    @determinant.setter
    def determinant(self, determinant):
        """
        Sets the determinant of the polynomial.
        """
        self.__determinant = determinant

    @vertices.setter
    def vertice(self, Vertice: Points):
        """
        Sets the vertices of the polynomial.
        """
        self.__vertices._xAxis = Vertice.xAxis
        self.__vertices._yAxis = Vertice.yAxis

    @axis.setter
    def axis(self, Axis: Points):
        """
        Sets the axis of the polynomial.
        """
        self.__axis.xAxis = Axis.xAxis
        self.__axis.yAxis = Axis.yAxis
