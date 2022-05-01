# MIT License
#
# Copyright (c) 2022 [FacuFalcone]
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

def create_symbols(message: str, symbol: str = '#') -> str:
    """
    Creates a string with the same length of the message,\n
    with the symbol 'symbol'.
    
    Args:
        message (str): Message to get its length
        symbol (str, optional): Symbol to be repeated with the same length of the message.\n
        Defaults to '#'.
        
    Returns:
        str: String with the same length of the message,
        with the symbol repeated.
    """
    symbols_str = ''
    for _ in message:
        symbols_str += symbol

    return symbols_str

def binary_to_decimal(bin_list: list) -> None:
    """[summary]
    Reads a list of binary numbers, then converts them to decimal\n
    to see what char from ascii table they represent

    Args:
        bin_list (list): List of binary numbers
    """
    message = ''
    symbols = ''
    for i in bin_list:
        message += chr(int(i, 2))
    symbols = create_symbols('#', message)
    print('Secret message: ')
    print(symbols)
    print(message)
    print(symbols)


if __name__ == "__main__":
    bin_list = [
        '01100110', '01101001', '01101110', '01100100', '00101110',
        '01100110', '01101111', '01101111', '00101111', '01000111',
        '01101111', '01101111', '01100111', '01101100', '01100101',
        '01000011', '01100101', '01110010', '01110100', '01110011'
    ]

    binary_to_decimal(bin_list)
    # Output: find.foo/GoogleCerts
