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


import random

def password_generator():
    uppercases= ["A", "B", "C", "D", "E", "F", "G"]
    lowercases = ["a", "b", "c", "d", "e", "f", "g"]
    symbols =[":","#","%","/","(",")","}"]
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8","9","0"]

    characters = f'{uppercases}{lowercases}{symbols}{numbers}'
    new_password=[]

    for _ in range(15):
        random_character = random.choice(characters)
        new_password.append(random_character)

    # ?# Generates a password from the original string.
    created_password = "".join(new_password) 
    return created_password

def run():
    password = password_generator()
    print(f"Your new password is: {password}")

if __name__=="__main__":
    run()