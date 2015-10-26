# Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).

# For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.


class Solution1(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        while n:
            ans += n & 1
            n >>= 1
        return ans

class Solution2(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        while n:
            n &= n - 1
            ans += 1
        return ans
