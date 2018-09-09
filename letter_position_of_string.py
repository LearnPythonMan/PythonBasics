#Zadanie z codewars "Replace With Alphabet Position" https://www.codewars.com/kata/546f922b54af40e1e90001da/train/python


#In this kata you are required to, given a string, replace every letter with its position in the alphabet.
#If anything in the text isn't a letter, ignore it and don't return it.
#a being 1, b being 2, etc.

import unicodedata

test = "! !"

def alphabet_position(text):
    positionList = ""
    for letter in text:
        if letter.isalpha() == True:
            positionList=positionList+" "+str((ord(letter.lower())-96))
    return positionList[1:]


print(alphabet_position(test))