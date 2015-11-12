# Given an integer n, return the number of trailing zeroes in n!.

# Note: Your solution should be in logarithmic time complexity.


"""
Find the number of factor 5 in the factorial number,
as factor 2 and factor 5 decide how many trailing zeroes it has.
Number of factor 5 is always less than number of factor 2.
Therefore, we can count the number of factor 5 only.
"""


class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        x = 5
        ans = 0
        while n > x:
            ans += n // x
            x *= 5
        return ans
