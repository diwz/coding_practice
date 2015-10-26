# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

# You may assume that the array is non-empty and the majority element always exist in the array.

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        cnt = 0

        for num in nums:
            if cnt == 0:
                majority = num
                cnt = 1
            elif num == majority:
                cnt += 1
            else:
                cnt -= 1

        return majority
