# All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.
# Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

# For example,
# Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",
# Return:
# ["AAAAACCCCC", "CCCCCAAAAA"].

class Solution1(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        lookup, res = {}, []
        for i in range(len(s)-9):
            substr = s[i:i+10]
            lookup[substr] = lookup.get(substr, 0) + 1
            if lookup[substr] == 2:
                res.append(substr)
        return res

class Solution2(object):
    def findRepeatedDnaSequences(self, s):
        dict, rolling_hash, res = {}, 0, []

        for i in xrange(len(s)):
            rolling_hash = rolling_hash << 3 & 0x3fffffff | ord(s[i]) & 7
            if rolling_hash not in dict:
                dict[rolling_hash] = True
            elif dict[rolling_hash]:
                res.append(s[i - 9: i + 1])
                dict[rolling_hash] = False
        return res
