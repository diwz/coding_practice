# Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

# For example, given
# s = "leetcode",
# dict = ["leet", "code"].

# Return true because "leetcode" can be segmented as "leet code".


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """

        """
        dp[i] = true if s[o,i] is in dict
              = true if dp[k] is true and s[k+1,i] is in dict, 0< k< i
              = false no such k
        """

        dp = [False for i in range(len(s)+1)]
        dp[0] = True

        for i in range(1, len(s)+1):
            for k in range(i):
                if dp[k] and s[k:i] in dict:
                    dp[i] = True

        return dp[len(s)]
