# MIT License

# Copyright (c) 2022 [FacuFalcone]

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# ?# List of dictionaries
from typing import Tuple, Dict, List

positives: List[int] = [1, 2, 3, 4, 5]

users: Dict[str, int] = {
    "argentina": 15,
    "mexico": 10,
    "colombia": 8,
}

countries: List[Dict[str, str]] = [
    {
        "name": "Argentina",
        "people": "45000000",
    },
    {
        "name": "México",
        "people": "9000000",
    },
    {
        "name": "Colombia",
        "people": "34000000",
    }
]

# *# ----------------------------------------------------------------------------------
# ?# List of dictionaries with string keys and tuples as values

CoordinatesType = List[Dict[str, Tuple[int, int]]]

coordinates: CoordinatesType = [
    {
        "coord1": (1,2),
        "coord2": (3,5)
    },
    {
        "coord1": (0,1),
        "coord2": (2,5)
    }
]
