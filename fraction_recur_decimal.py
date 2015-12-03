# Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
# If the fractional part is repeating, enclose the repeating part in parentheses.

# For example,

# Given numerator = 1, denominator = 2, return "0.5".
# Given numerator = 2, denominator = 1, return "2".
# Given numerator = 2, denominator = 3, return "0.(6)".


class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        neg = False
        if numerator * denominator < 0:
            neg = True
        dividend, divisor = abs(numerator), abs(denominator)
        integer, decimal, dict = "", "", {}

        if dividend > divisor:
            integer = str(dividend // divisor)
            dividend %= divisor
        else:
            integer = "0"

        if dividend > 0:
            integer = integer + "."
        idx = 0
        while dividend:
            if dividend in dict:
                decimal = decimal[:dict[dividend]] + "(" + decimal[dict[dividend]:] + ")"
                break

            dict[dividend] = idx
            idx += 1

            dividend *= 10
            decimal += str(dividend/divisor)
            dividend %= divisor

        if neg:
            return "-" + integer + decimal
        else:
            return integer + decimal
