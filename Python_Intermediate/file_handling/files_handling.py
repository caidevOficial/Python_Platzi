# MIT License
#
# Copyright (c) 2021 [FacuFalcone]
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

def read():
    numbers=[]
    with open("./Data/numbers.txt", "r", encoding="utf-8") as f:
        for line in f: # ?# Reads the file line by line
            numbers.append(int(line))
    print(numbers)

def write():
    names = ["Facu", "Poseidon", "Ragnar", "Valhalla", "Neptune"]
    # ?# Creates a file with the data of the list of names 
    # *# The 'a' parameter is used to append the data to the file
    # *# instead of overwriting it with 'w'
    with open("./Data/names.txt", "w", encoding="utf-8") as f: 
        for name in names:
            f.write(f'{name}\n')

def run():
    write()

if __name__ == "__main__":
    run()
