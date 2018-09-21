class RomanNumerals:
    import re

    @staticmethod
    def to_roman(num):

        def small_dig_to_roman(dig, nine, five, four, one):
            if dig == 9:
                return nine
            elif dig > 4:
                return five + one * (dig - 5)
            elif dig == 4:
                return four
            else:
                return one * dig

        roman = ""
        roman += ('M' * (num // 1000))
        roman += (small_dig_to_roman(num // 100 % 10, 'CM', 'D', 'CD', 'C'))
        roman += (small_dig_to_roman(num // 10 % 10, 'XC', 'L', 'XL', 'X'))
        roman += (small_dig_to_roman(num % 10, 'IX', 'V', 'IV', 'I'))
        return roman

    @staticmethod
    def from_roman(str):

        def small_roman_to_dig(str, nine, four, five):
            if nine in str:
                return -2
            elif four in str:
                return 3
            elif five in str:
                return 5
            else:
                return 0

        arab = 0
        # if re.match(r'^([MDCLXVI]+)', str):
        #    return "Not a Roman number"
        arab += str.count('M') * 1000
        arab += small_roman_to_dig(str, 'CM', 'CD', 'D') * 100
        arab += str.count('C') * 100
        arab += small_roman_to_dig(str, 'XC', 'XL', 'L') * 10
        arab += str.count('X') * 10
        arab += small_roman_to_dig(str, 'IX', 'IV', 'V')
        arab += str.count('I')
        return arab