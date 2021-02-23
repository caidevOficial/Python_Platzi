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

from ..Points.Points import Points

class Polynomial:
    #determinant: float
    #axis: Points
    #vertices: Points

    def __init__(self, determinant, axis:Points, vertices:Points):
        """
        Builds the polynomial.
        """
        self._determinant = determinant
        self._axis = axis
        self._vertices = vertices
    
# Getters
    @property
    def determinant(self):
        """
        Gets the determinant of the polynomial.
        """
        return self._determinant

    @property
    def axis(self):
        """
        Gets the axis of the polynomial.
        """
        return self._axis

    @property
    def vertices(self):
        """
        Gets the vertices of the polynomial.
        """
        return self._vertices

# Setters

    @determinant.setter
    def determinant(self, determinant):
        """
        Sets the determinant of the polynomial.
        """
        self._determinant = determinant

    @vertices.setter
    def vertice(self, xVertice, yVertice):
        """
        Sets the vertices of the polynomial.
        """
        self._vertices.xAxis = xVertice
        self._vertices.yAxis = yVertice

    @axis.setter
    def axis(self, xAxis, yAxis):
        """
        Sets the axis of the polynomial.
        """
        self._axis.xAxis = xAxis
        self._axis.yAxis = yAxis
