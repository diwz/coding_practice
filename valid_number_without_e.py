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
        if i > end:
            return False
        # remove trailing space
        while end >= i and s[end] == " ":
            end -= 1

        if s[i] == "+" or s[i] == "-":
            i += 1
        dot = False

        while i <= end:
            char = s[i]
            if not char.isdigit():
                if char == ".":
                    if dot:
                        return False
                    dot = True
                else:
                    return False
            i += 1
        return True

if __name__ == '__main__':
    sol = Solution()
    print sol.isNumber("  +60.0 ")
    print sol.isNumber("  -24..3s ")
