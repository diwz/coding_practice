# Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.


class Solution1(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        # DP
        n = len(s)
        longestBegin = 0
        maxLen = 1
        dp = [[False] * 1000 for i in range(1000)]

        for i in range(n):
            dp[i][i] = True

        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                longestBegin = i
                maxLen = 2

        for l in range(3, n+1):
            for i in range(n-l+1):
                j = i+l-1
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    longestBegin = i
                    maxLen = l

        return s[longestBegin:longestBegin+maxLen]


class Solution2(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)

        def expandAroundCenter(l, r):
            while l >= 0 and r <= n-1 and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]

        if n == 0:
            return ""

        longest = s[:1]
        for i in range(n-1):
            p1 = expandAroundCenter(i, i)
            if len(p1) > len(longest):
                longest = p1

            p2 = expandAroundCenter(i, i+1)
            if len(p2) > len(longest):
                longest = p2

        return longest


class Solution3(object):
    def preProcess(self, s):
        """
        Transform S into T.
        For example, S = "abba", T = "^#a#b#b#a#$".
        ^ and $ signs are sentinels appended to each end to avoid bounds checking
        """
        n = len(s)
        if n == 0:
            return "^$"
        res = "^"
        for i in range(n):
            res += "#" + s[i]

        res += "#$"
        return res

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        T = self.preProcess(s)
        n = len(T)
        p = [0]*n

        C, R = 0, 0
        for i in range(1, n-1):
            i_mirror = 2*C - i

            if R > i:
                p[i] = min(R-i, p[i_mirror])

            while T[i+1+p[i]] == T[i-1-p[i]]:
                p[i] += 1

            if i+p[i] > R:
                C = i
                R = i + p[i]

        maxLen = 0
        centerIdx = 0
        for i in range(1, n-1):
            if p[i] > maxLen:
                maxLen = p[i]
                centerIdx = i

        return s[(centerIdx - 1- maxLen)//2:(centerIdx - 1 + maxLen)//2]
