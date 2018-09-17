def first_non_repeating_letter(string):
    return next(iter([char for char in string if string.lower().count(char.lower()) == 1]),"")

# Write a function named firstNonRepeatingLetter† that takes a string input, and returns the first character that is not repeated anywhere in the string.
#
# For example, if given the input 'stress', the function should return 't', since the letter t only occurs once in the string, and occurs first in the string.
#
# As an added challenge, upper- and lowercase letters are considered the same character, but the function should return the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.
#
# If a string contains all repeating characters, it should return the empty string ("").

#Best practice:
# def first_non_repeating_letter(string):
#     string_lower = string.lower()
#     for i, letter in enumerate(string_lower):
#         if string_lower.count(letter) == 1:
#             return string[i]
#
#     return ""

#optimalized one row:
# def first_non_repeating_letter(string):
#     return next((x for x in string if string.lower().count(x.lower())==1), '')