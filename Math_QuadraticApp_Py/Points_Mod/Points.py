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

class Points:
    #xAxis: float
    #yAxis: float

    def __init__(self, xAxis:float, yAxis:float):
        """
        Builds the entity.
        """
        self._xAxis = xAxis
        self._yAxis = yAxis

# Getters
    @property
    def xAxis(self):
        """
        Gets the x axis of the entity.
        """
        return self._xAxis
    
    @property
    def yAxis(self):
        """
        Gets the y axis of the entity.
        """
        return self._yAxis

# Setters
    @xAxis.setter
    def set_xAxis(self, xAxis:float):
        """
        Sets the x axis of the entity.
        """
        self._xAxis = xAxis
    
    @yAxis.setter
    def set_yAxis(self, yAxis:float):
        """
        Sets the y axis of the entity.
        """
        self._yAxis = yAxis
