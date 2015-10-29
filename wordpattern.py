# Given a pattern and a string str, find if str follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

# Examples:
# pattern = "abba", str = "dog cat cat dog" should return true.
# pattern = "abba", str = "dog cat cat fish" should return false.
# pattern = "aaaa", str = "dog cat cat dog" should return false.
# pattern = "abba", str = "dog dog dog dog" should return false.
# Notes:
# You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.


class Solution1(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str = str.split(' ')
        if len(str) != len(pattern):
            return False
        hash_p = {}
        hash_s = {}
        for p, s in zip(pattern, str):
            hash_p[p] = hash_p.get(p, s)
            hash_s[s] = hash_s.get(s, p)
            if hash_p[p] != s:
                return False
            if hash_s[s] != p:
                return False
        return True


class Solution2(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """

        s = pattern
        t = str.split()
        if len(s) != len(t):
            return False
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))


class Solution3(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """

        s = pattern
        t = str.split()
        if len(s) != len(t):
            return False
        return map(s.find, s) == map(t.index, t)
