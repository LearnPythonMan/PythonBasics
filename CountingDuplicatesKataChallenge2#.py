# Count the number of Duplicates
# Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits
# that occur more than once in the input string. The input string can be assumed to contain only alphabets
# (both uppercase and lowercase) and numeric digits.

# e.g. "abcde" -> 0 # no characters repeats more than once,
# "aabbcde" -> 2 # 'a' and 'b',
# "aabBcde" -> 2 # 'a' occurs twice and 'b' twice (bandB),
# "indivisibility" -> 1 # 'i' occurs six times

import re
test = 'aAbbCc!!__' #4


def duplicate_count(text):
    no_duplicates = 0
    for letter in set(re.sub(r'[\W_]+', '', text.lower())):
        if text.lower().count(letter) > 1:
            no_duplicates = no_duplicates+1
    return no_duplicates


print(duplicate_count(test))


# optimal solution: return len([c for c in set(s.lower()) if s.lower().count(c)>1])
