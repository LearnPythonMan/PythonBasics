s = "444996, 699990, 666690, 096904, 600644, 640646, 606469, 409694, 666094, 606490"

# Suppose you have 4 numbers: '0', '9', '6', '4' and 3 strings composed with them:
#
# s1 = "6900690040"
# s2 = "4690606946"
# s3 = "9990494604"
# Compare s1 and s2 to see how many positions they have in common: 0 at index 3, 6 at index 4, 4 at index 8 ie 3 common positions out of ten.
#
# Compare s1 and s3 to see how many positions they have in common: 9 at index 1, 0 at index 3, 9 at index 5 ie 3 common positions out of ten.
#
# Compare s2 and s3. We find 2 common positions out of ten.
#
# So for the 3 strings we have 8 common positions out of 30 ie 0.2666... or 26.666...%
#
# Given n substrings (n >= 2) in a string s our function pos_average will calculate the average percentage of positions that are the same between the (n * (n-1)) / 2 sets of substrings taken amongst the given n substrings. It can happen that some substrings are duplicate but since their ranks are not the same in s they are considered as different substrings.
#
# The function returns the percentage formatted as a float with 10 decimals but the result is tested at 1e.-9 (see function assertFuzzy in the tests).
#
# Example:
# Given string s = "444996, 699990, 666690, 096904, 600644, 640646, 606469, 409694, 666094, 606490" composing a set of n = 10 substrings (hence 45 combinations), pos_average returns 29.2592592593.
#
# In a set the n substrings will have the same length ( > 0 ).

def pos_average(s):
    substrings = s.split(', ')
    sum = 0
    for i, substring in enumerate(substrings):
        for j, letter in enumerate(substring):
            for x in range(i+1,len(substrings)):
                if letter == substrings[x][j]:
                    sum += 1
    return sum/(len(substrings)*(len(substrings)-1)/2*len(substrings[0]))*100

print(pos_average(s))

# from statistics import mean
# from itertools import combinations
#
# def pos_average(s):
#     return mean(a == b for combo in combinations(s.split(', '), 2) for a, b in zip(*combo)) * 100.

# from itertools import combinations
#
# def pos_average(s):
#     numbers   = s.split(", ")
#     n         = len(numbers)
#     combos    = (n * (n-1)) / 2
#     positions = combos * len(numbers[0])
#     matches   = sum( sum(dig_a == dig_b for dig_a, dig_b in zip(num_a, num_b))
#                   for num_a, num_b in combinations(numbers, 2))
#     return matches / positions * 100