# Find the contiguous subarray within an array (containing at least one number) which has the largest product.

# For example, given the array [2,3,-2,4],
# the contiguous subarray [2,3] has the largest product = 6.


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        cur_min = nums[0]
        cur_max = nums[0]
        global_max = nums[0]

        for i in range(1, len(nums)):
            tmpA = cur_min * nums[i]
            tmpB = cur_max * nums[i]
            cur_min = min(tmpA, tmpB, nums[i])
            cur_max = max(tmpA, tmpB, nums[i])
            global_max = max(global_max, cur_max)
        return global_max
