# Find the contiguous subarray within an array (containing at least one number) which has the largest product.

# For example, given the array [2,3,-2,4],
# the contiguous subarray [2,3] has the largest product = 6.


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxCur = nums[0]
        minCur = nums[0]

        res = nums[0]

        for i in range(1, len(nums)):
            tmpA = nums[i] * maxCur
            tmpB = nums[i] * minCur
            tmpC = nums[i]

            maxCur = max(tmpA, tmpB, tmpC)
            minCur = min(tmpA, tmpB, tmpC)

            res = max(res, maxCur)
        return res
