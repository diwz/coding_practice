# Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

# Example:
# Given "bcabc"
# Return "abc"

# Given "cbacdcbc"
# Return "acdb"


class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        vis, cnt = [False] * 26, [0] * 26
        ans = []
        for c in s:
            cnt[ord(c) - 97] += 1  # ord(a) =97
        for c in s:
            index = ord(c) - 97
            cnt[index] -= 1
            if vis[index]:
                continue
            while ans and ans[-1] > c and cnt[ord(ans[-1]) - 97]:
                vis[ord(ans.pop()) - 97] = False
            ans.append(c)
            vis[index] = True

        return ''.join(ans)
