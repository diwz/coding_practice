class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()
        words = s.split(' ')
        words.reverse()
        res = []
        for word in words:
            if word != "":
                res.append(word)
        return " ".join(res)