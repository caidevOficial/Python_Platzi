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

from time import sleep

class FibonacciIter:
    
    __max_number: int = 0
    __first_number: int = 0
    __second_number: int = 0
    __counter: int = 0

    def __init__(self, max_number: int = None):
        self.Max_Number = max_number
    
    @property
    def Max_Number(self):
        return self.__max_number
    
    @property
    def First_Number(self):
        return self.__first_number
    
    @property
    def Second_Number(self):
        return self.__second_number
    
    @property
    def Counter(self):
        return self.__counter

    @Max_Number.setter
    def Max_Number(self, value: int):
        self.__max_number = value
    
    @First_Number.setter
    def First_Number(self, value: int):
        self.__first_number = value
    
    @Second_Number.setter
    def Second_Number(self, value: int):
        self.__second_number = value
    
    @Counter.setter
    def Counter(self, value: int):
        self.__counter = value
    
    def __iter__(self):
        self.First_Number = 0
        self.Second_Number = 1
        self.Counter = 0
        return self
    
    def __next__(self):
        if self.Max_Number and self.Counter >= self.Max_Number:
            raise StopIteration
        self.Counter += 1
        self.First_Number, self.Second_Number = self.Second_Number, self.First_Number + self.Second_Number
        return self.First_Number
    
if __name__ == "__main__":
    for number in FibonacciIter(10):
        print(number)
        sleep(0.1)
