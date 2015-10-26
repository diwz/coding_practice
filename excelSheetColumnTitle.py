# Given a positive integer, return its corresponding column title as appear in an Excel sheet.

# For example:

#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB


class iterativeSolution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ''
        while n:
            res = chr(ord('A') + (n-1) % 26) + res
            n = (n-1)//26
        return res


class recursiveSolution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 0:
            return ""

        return self.convertToTitle((n-1)//26) + chr(ord("A") + (n-1) % 26)
