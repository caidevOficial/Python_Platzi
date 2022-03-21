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

from datetime import datetime as dt


def execution_time(func):
    """[summary]\n
    Decorator to calculate the execution time of a function.
    Args:
        func (function): Function to be decorated
    
    Returns:\n
        [function]: [Function to be returned decorated.]
    """
    def wrapper(*args, **kwargs):
        """[summary]\n
        A wrapper function to calculate the execution time of a function.

        Args:\n
            *args ([type]): [First argument]\n
            **kwargs ([type]): [Keys Arguments]
        """
        start = dt.now()
        func(*args, **kwargs)
        end = dt.now()
        total_time = round((end - start).total_seconds(), 2)
        print(f"{func.__name__} took {total_time} seconds to execute")
    return wrapper

@execution_time
def just_for_check():
    """[summary]\n
    A function just for check the execution time of a function.
    """
    for _ in range(10000000*25):
        pass

if __name__ == '__main__':
    print(just_for_check())
    