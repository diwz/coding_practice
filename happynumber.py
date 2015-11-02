# Write an algorithm to determine if a number is "happy".
# A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.
# Example: 19 is a happy number

# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1


class Solution1(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        prev = set([n])
        while n != 1:
            n = sum([int(x)**2 for x in str(n)])
            if n in prev:
                return False
            prev.add(n)
        return True


class Solution2(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        prev = set()
        while n != 1 and n not in prev:
            prev.add(n)
            sum = 0
            while n:
                digit = n % 10
                sum += digit ** 2
                n //= 10
            n = sum
        return n == 1
