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

def my_decorator_1(func):
    """[summary]\n
    An example of a decorator
    Args:
        func (function): [The function to be decorated]
    
    Returns:\n
        [function]: [Function to be returned decorated.]
    """
    def wrapper():
        """[summary]\n
        A wrapper function
        """
        print('Before_1')
        func()
        print('After_1')
    return wrapper

def my_decorator_2(func):
    """[summary]\n
    An example of a decorator

    Args:\n
        func (function): [The function to be decorated]

    Returns:\n
        [type]: [description]
    """
    def wrapper(*args, **kwargs):
        """[summary]\n
        A wrapper function
        
        Args:\n
            *args ([type]): [First argument]\n
            **kwargs ([type]): [Keys Arguments]
            
        Returns:\n
            [function]: [Function to be returned decorated.]
        """
        print('Before_2')
        result = func(*args, **kwargs)
        print('After_2')
        return result
    return wrapper

def simple_function():
    """[summary]\n
    A simple function that prints a basic msg.
    """
    print('I am a simple function')

@my_decorator_1
def another_simple_function():
    """[summary]\n
    A simple function that prints a basic msg but decorated with my_decorator_1
    """
    print('I am another simple function')

if __name__ == '__main__':
    print('\nFirst decorator:')
    simple_function_1 = my_decorator_1(simple_function)
    simple_function_1()

    print('\nSecond decorator:')
    simple_function_2 = my_decorator_2(simple_function)
    simple_function_2()

    print('\nThird decorator with sugar syntax:')
    another_simple_function()
