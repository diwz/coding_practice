class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import re
        return bool(re.match("^\s*[\+-]?((\d+(\.\d*)?)|\.\d+)([eE][\+-]?\d+)?\s*$", s))
        