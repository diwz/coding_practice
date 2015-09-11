class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        diff = 0
        if len(nums) < 2:
            return diff
        nums.sort()
        for x in range(1, len(nums)):
            if nums[x] - nums[x-1] > diff:
                diff = nums[x] - nums[x-1]
        return diff