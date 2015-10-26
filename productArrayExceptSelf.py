# Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

# Solve it without division and in O(n).

# For example, given [1,2,3,4], return [24,12,8,6].


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = right = 1
        size = len(nums)
        res = [1] * size
        for i in range(size-1):
            left *= nums[i]
            res[i+1] *= left

        for i in range(size-1, 0, -1):
            right *= nums[i]
            res[i-1] *= right

        return res
