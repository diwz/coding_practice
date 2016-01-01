# Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

# For example,
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

# Given word1 = "coding", word2 = "practice", return 3.
# Given word1 = "makes", word2 = "coding", return 1.

# Note:
# You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.


class Solution1(object):
    def shortestDistance(self, words, word1, word2):
        last, min_dist = -1, len(words)
        for i in range(len(words)):
            if words[i] in (word1, word2):
                if last != -1 and words[last] != words[i]: # if current matched word is different from last matched word
                    min_dist = min(min_dist, i-last)
                last = i
        return min_dist

class Solution2(object):
    def shortestDistance(self, words, word1, word2):
        idx1, idx2, min_dist = -1, -1, len(words)
        for i in range(len(words)):
            if words[i] == word1:
                idx1 = i
            elif words[i] == word2:
                idx2 = i
            if idx1 != -1 and idx2 != -1:
                min_dist = min(min_dist, abs(idx1-idx2))

        return min_dist

if __name__ == '__main__':
    sol = Solution2()
    res = sol.shortestDistance(["practice", "makes", "perfect", "coding", "makes"], "coding", "makes")
    print res
