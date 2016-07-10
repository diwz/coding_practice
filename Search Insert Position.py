# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You may assume no duplicates in the array.

# Here are few examples.
# [1,3,5,6], 5 → 2
# [1,3,5,6], 2 → 1
# [1,3,5,6], 7 → 4
# [1,3,5,6], 0 → 0

class Solution1(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0 or target <= nums[0]:
            return 0
        for i in range(1, len(nums)):
            if nums[i] == target or nums[i-1] < target < nums[i]:
                return i
        if target > nums[-1]:
            return len(nums)

class Solution2(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low, high = 0, len(nums)-1
        while low <= high:
            mid = (low+high)//2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                high = mid -1
            else:
                low = mid + 1
        return low


