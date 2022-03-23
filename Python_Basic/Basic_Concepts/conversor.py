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

def print_menu():
    MENU ="""
    Simply Money Conversor
    1 - Colombians Pesos
    2 - Argentinians Pesos
    3 - Mexicans Pesos
    Select an option: 
    """
    return MENU

def conversor(ars_type, usd_value):
    argentinian_pesos = input(f"how many {ars_type} do you have?:")
    # ?# Cast a number to float
    argentinian_pesos = float(argentinian_pesos) 
    bucks = argentinian_pesos/usd_value
    # ?# Round a number to 2 decimal places
    bucks = round(bucks, 2) 
    bucks = str(bucks)
    print(f"You have ${bucks} Bucks")

def run():
    selected_option =int(input(print_menu()))
    if selected_option == 1:
        conversor("Colombians", 3875)
    elif selected_option ==2:
        conversor("Argentinians", 109)
    elif selected_option ==3:
        conversor("Mexicans", 24)
    else:
        print("Select an option")

if __name__ == "__main__":
    run()