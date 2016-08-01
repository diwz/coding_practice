# Suppose a sorted array is rotated at some pivot unknown to you beforehand.

# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

# Find the minimum element.

# You may assume no duplicate exists in the array.


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums)-1
        while l < r:
            if nums[l] < nums[r]:
                return nums[l]
            m = l + (r-l)//2
            if nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m
        return nums[l]
