class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        if n == 0:
            return res
        else:
            self.generate(n, n, '', res)
        return res

    def generate(self, l, r, pStr, res):
        if r < l:
            return
        if r == 0 and l == 0:
            res.append(pStr)
        if l > 0:
            self.generate(l-1, r, pStr + '(', res)
        if r > 0:
            self.generate(l, r-1, pStr + ')', res)
