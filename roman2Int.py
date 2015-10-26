# Given a roman numeral, convert it to an integer.

# Input is guaranteed to be within the range from 1 to 3999.


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        numbers = {"M": 1000, "D": 500, "C": 100,
                   "L": 50, "X": 10, "V": 5, "I": 1}
        total = 0

        s = s[::-1]
        last = None
        for x in s:
            if last and numbers[x] < last:
                total -= 2*numbers[x]
            total += numbers[x]
            last = numbers[x]

        return total
