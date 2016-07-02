# Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
# For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.
#

import math


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        """
        A natural number is

        - a square if and only if each prime factor occurs to an even power
        in the number's prime factorization

        - a sum of two squares if and only if each prime factor
        that's 3 modulo 4 occurs to an even power in the number's prime factorization

        - a sum of three square if and only if it's not in the form of
        4^a(8*b+7) with integers a and b

        - a sum of four squares. No condition, you never need more than 4 square
        """
        upper = int(math.ceil(math.sqrt(n)))
        for a in range(upper+1):
            for b in range(a, upper+1):
                if a*a + b*b > n:
                    continue
                c = int(math.ceil(math.sqrt(n - a*a-b*b)))
                if a*a + b*b + c*c == n:
                    res = 3
                    if a == 0:
                        res -= 1
                    if b == 0:
                        res -= 1
                    if c == 0:
                        res -= 1
                    return res
        return 4

sol = Solution()
sol.numSquares(12)
