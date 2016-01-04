class SolutionRE(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import re
        return bool(re.match("^\s*[\+-]?((\d+(\.\d*)?)|\.\d+)([eE][\+-]?\d+)?\s*$", s))


class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i, end = 0, len(s)-1
        # remove leading space
        while i <= end and s[i] == " ":
            i += 1
        if i > en*0d:
            return False
        # remove trailing space
        while end >= i and s[end] == " ":
            end -= 1

        if s[i] == "+" or s[i] == "-":
            i += 1
        num = False
        dot = False
        exp = False


        while i <= end:
            char = s[i]
            if char.isdigit():
                num = True
            elif char == ".":
                if exp or dot:
                    return False
                dot = True
            elif char in "eE":
                if exp or not num:
                    return False
                exp = True
                num = False
            elif char in "+-":
                if s[i-1] not in "eE":
                    return False
            else:
                return False
            i += 1
        return num
