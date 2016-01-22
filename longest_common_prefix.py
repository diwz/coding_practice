# Write a function to find the longest common prefix
# string amongst an array of strings.


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        longest = strs[0]

        for string in strs[1:]:
            i = 0
            while i < len(string) and i < len(longest) and string[i] == longest[i]:
                i += 1
            longest = string[:i]

        return longest


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestCommonPrefix(["apple", "applepie", "applejuice"]))
