# Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

# Only one letter can be changed at a time
# Each intermediate word must exist in the word list
# For example,

# Given:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
# As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.

# Note:
# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """

        wordList.add(endWord)
        queue = []
        queue.append((beginWord, 1))
        while queue:
            cur = queue.pop(0)
            curWord, curLen = cur[0], cur[1]
            if curWord == endWord:
                return curLen
            for i in range(len(endWord)):
                beforeChar, afterChar = curWord[:i], curWord[i+1:]
                for char in "abcdefghijklmnopqrstuvwxyz":
                    newWord = beforeChar + char + afterChar
                    if newWord in wordList:
                        queue.append((newWord, curLen + 1))
                        wordList.remove(newWord)
        return 0
