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


import random as rd
import os
from unicodedata import normalize

def clear ():
    os.system("clear")

def read():
    words=[]
    with open("./Data/data.txt", "r", encoding="utf-8") as f:
        for line in f: # ?# Reads the file line by line
            # ?# Removes spaces and convert the string to uppercase
            normalised_words = line.strip().upper()
            words.append(normalised_words)
    return words

def selected_word():
    words = read()
    random_number = rd.randint(1, 171)
    selected_word=words[random_number]
    # ?# Removes the accents from the string
    trans_tab = dict.fromkeys(map(ord, u'\u0301\u0308'), None)
    selected_word = normalize('NFKC', normalize('NFKD', selected_word).translate(trans_tab))
    return selected_word

def fill_spaces():
    spaces=[]
    input_character=[]
    selected_word=list(selected_word())
    amount_characters=len(selected_word)
    # ?# Counts the amount of spaces in the selected word
    for _ in range(0,amount_characters):
        spaces.append("__")

    # ?# Main Logic
    while spaces != selected_word:
        print("________________________Hangman Game________________________\n")
        print(f'{spaces}\n')
        print(f"Characters amount of the word: {amount_characters}\n")
        input_character=input(str("Write a character: "))
        input_character=input_character.upper()
        print(f"Character Wrote: {input_character}")
        for j in range(0,amount_characters):
            if input_character == selected_word[j]:
                spaces[j] = input_character    
        print(spaces)
        clear()
    print("Congratulations! U won!")
    print(f"The word was: {selected_word}")

def run():
    fill_spaces()

if __name__ == "__main__":
     run()
