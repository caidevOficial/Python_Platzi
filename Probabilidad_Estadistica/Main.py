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
#/

from Permutations import Permutation as P
from Combinatory import Combinatoy as C
from Variation import Variation as V

def SelectOperation(option:int):
    if option == 1:
        try:
            P.SimplePermutation()
        except Exception as e:
            print(e)
    elif option == 2:
        try:
            V.SimpleVariation()
        except Exception as e:
            print(e)
    elif option == 3:
        try:
            C.SimpleCombinatory()
        except Exception as e:
            print(e)
    elif option ==4:
        try:
            P.ComposedPermutation()
        except Exception as e:
            print(e)
    elif option == 5:
        try:
            V.CompoundVariation()
        except Exception as e:
            print(e)
    elif option == 6:
        try:
            C.CompoundCombinatory()
        except Exception as e:
            print(f"Error: {e}")
    

def CombinatorialCalculus():
    appName = "Combinatorial Calculus"
    version = "v1.2.0"
    author = "Facu Falcone"
    print("Select an option from the ones below")
    print("1 - Simple Permutation.\n2 - Simple Variation.\n3 - Simple Combination.")
    print("4 - Compound Permutation.\n5 - Compound Variation.\n6 - Compound Combination.")
    try:
        option = int(input("Your option: "))
        SelectOperation(option)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print(f"\n## {appName} {version} by {author}. ##\n")


if __name__=='__main__':
    CombinatorialCalculus()
