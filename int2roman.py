# Given an integer, convert it to a roman numeral.

# Input is guaranteed to be within the range from 1 to 3999.


class Solution:
    # @return a string
    def intToRoman(self, num):
        values = [1000, 900, 500, 400,
                  100, 90, 50, 40, 10, 9, 5, 4, 1]
        signs = ["M", "CM", "D", "CD", "C", "XC", "L",
                 "XL", "X", "IX", "V", "IV", "I"]

        roman = ''
        for i in range(len(values)):
            while num >= values[i]:
                num -= values[i]
                roman += signs[i]
        return roman
