# Given a sorted integer array where the range of elements are [lower, upper] inclusive, return its missing ranges.

# For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, return ["2", "4->49", "51->74", "76->99"].

class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        pre = lower - 1
        res = []
        for i in range(len(nums) + 1):
            if i == len(nums):
                post = upper + 1
            else:
                post = nums[i]
            if pre + 2 == post:
                res += str(pre+1),
            elif pre + 2 < post:
                res += str(pre+1) + "->" + str(post-1),
            pre = post
        return res
