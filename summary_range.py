# Given a sorted integer array without duplicates, return the summary of its ranges.
# For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].


class Solution1(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        x, size = 0, len(nums)
        res = []
        while x < size:
            c, r = x, str(nums[x])
            while x + 1 < size and nums[x+1] - nums[x] == 1:
                x += 1
            if x > c:
                r += "->" + str(nums[x])
            res.append(r)
            x += 1
        return res


class Solution2(object):
    def summaryRanges(self, nums):
        ranges, r = [], []
        for n in nums:
            if n-1 not in r:
                r = []
                ranges += r,
            r[1:] = n,
        return ['->'.join(map(str, r)) for r in ranges]


class Solution3(object):
    def summaryRanges(self, nums):
        ranges = r = []
        for n in nums:
            if str(n-1) not in r:
                r = []
                ranges += r,
            r[1:] = str(n),
        return map('->'.join, ranges)
