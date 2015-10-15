class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        elif num % 9 == 0:
            return 9
        elif num % 9 != 0:
            return num % 9
        """
        a more straighforward way
        while num > 9:
            cur = 0
            while num:
                cur += num % 10
                num //= 10
            num = cur
        return num
        """
