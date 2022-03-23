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

def fibonacci_gen(max_number: int = None):
    a, b, counter = 0, 1, 0
    while not max_number or counter < max_number:
        yield a
        a, b = b, a + b
        counter += 1
        
   
if __name__ == '__main__':
    range_num: int = 20
    fib = fibonacci_gen()
    print(f'Fibonacci sequence in range {range_num}:')
    for i in range(15):
        print(f'{i+1}° Number: {next(fib)}')
        sleep(0.1)
    
    range_num = 10
    print(f'Fibonacci sequence in range with limit {range_num}:')
    fib_2 = fibonacci_gen(range_num)
    for i in range(range_num):
        print(f'{i + 1}° Number: {next(fib_2)}')
        sleep(0.1)
