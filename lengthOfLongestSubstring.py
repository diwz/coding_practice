class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # store index of character
        charMap = [-1] * 256
        i, maxLen = 0, 0
        for x in xrange(0, len(s)):
            if charMap[ord(s[x])] >= i:
                i = charMap[ord(s[x])] + 1
            charMap[ord(s[x])] = x
            maxLen = max(x-i+1, maxLen)
        return maxLen
