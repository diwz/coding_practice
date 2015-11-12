# Reverse bits of a given 32 bits unsigned integer.

# For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).


"""
It is actually rotate the binary number entirely
"""


class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        rev = 0
        for i in range(32):
            rev = (rev << 1) | (n & 1)
            n = n >> 1
        return rev
