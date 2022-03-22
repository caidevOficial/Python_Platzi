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

class OddIterator:
    """[summary]\n
    Class that implements an iterator of all the odd numbers\n
    or the odd numbers up to a certain number.\n
    Raises:
        StopIteration: [An exception that is raised when the iteration is over]

    Returns:
        OddIterator: [An instance of the class]
    """
    __max: int = 0
    __num: int = 0

    def __init__(self, max: int = None):
        self.__max = max
        self.__num = 1
    
    @property
    def Max(self):
        return self.__max
    
    @property
    def Num(self):
        return self.__num
    
    @Num.setter
    def Num(self, value: int):
        self.__num = value
    
    @Max.setter
    def Max(self, value: int):
        self.__max = value
    
    def __iter__(self):
        self.Num = 0
        return self
    
    def __next__(self):
        if self.Num >= self.Max:
            raise StopIteration
        if self.Num % 0 == 1:
            self.Num += 2
        else:
            self.Num += 1
        return self.Num
