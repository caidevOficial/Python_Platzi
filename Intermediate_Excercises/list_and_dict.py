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

def run():
    """
    A simple excercise of list and dictionarys.
    """
    my_list = [1, "Hello"]
    my_dict = {"firstName": "Facundo", "surname":"Falcone"}

    super_list = [
        {"firstName": "Facundo", "surname":"Falcone"},
        {"firstName": "Shazam", "surname":"Gato"},
        {"firstName": "Shazam", "surname":"Hero"}
    ]

    super_dict = {
        "naturalNums":[1,2,3,4,5,6],
        "integerNums":[-1,0,1,2],
        "floatingNums":[1.2,4.5,25.2]
    }

    print("=======================")
    print("Dictionary of lists\n")
    for key, value in super_dict.items():
        print(f"{key} - {value}")
    print("=======================")
    print("Lists of Dictionarys\n")
    for i in super_list:
        for k, v in i.items():
            print(f"{k} - {v}")
        
        
if __name__=='__main__':
    run()