# Given two strings s and t, determine if they are isomorphic.

# Two strings are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

# For example,
# Given "egg", "add", return true.

# Given "foo", "bar", return false.

# Given "paper", "title", return true.

# Note:
# You may assume both s and t have the same length.


class Solution1(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hash_s = {}
        hash_t = {}
        for se, te in zip(s, t):
            hash_s[se] = hash_s.get(se, te)
            hash_t[te] = hash_t.get(te, se)
            if hash_s[se] != te:
                return False
            if hash_t[te] != se:
                return False
        return True


class Solution2(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return map(s.find, s) == map(t.index, t)


class Solution3(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))
