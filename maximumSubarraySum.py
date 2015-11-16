# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

# For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
# the contiguous subarray [4,−1,2,1] has the largest sum = 6.


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_end = 0
        global_max = nums[0]

        for num in nums:
            # since at least one number needs to be in the array
            max_end = max(max_end+num, num)
            global_max = max(global_max, max_end)
        return global_max
