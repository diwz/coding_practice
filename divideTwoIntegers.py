class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign = 1 if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0) else -1
        dividend, divisor, quotient = abs(dividend), abs(divisor), 0

        while dividend >= divisor:
            k, tmp = 0, divisor
            while dividend >= tmp:
                quotient += 1 << k
                dividend -= tmp
                tmp <<= 1
                k += 1
        return quotient * sign if quotient * sign < 2147483647 else 2147483647
