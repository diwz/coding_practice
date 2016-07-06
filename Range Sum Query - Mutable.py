# Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

# The update(i, val) function modifies nums by updating the element at index i to val.
# Example:
# Given nums = [1, 3, 5]

# sumRange(0, 2) -> 9
# update(1, 2)
# sumRange(0, 2) -> 8
# Note:
# The array is only modifiable by the update function.
# You may assume the number of calls to update and sumRange function is distributed evenly.


class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = nums
        self.n = len(nums)
        self.bit = [0 for i in range(len(nums) + 1)]
        for i in range(self.n):
            self.init(i, self.nums[i])

    def init(self, i, val):
        i += 1
        while i <= self.n:
            self.bit[i] += val
            i += (i & -i)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        diff = val - self.nums[i]
        self.nums[i] = val
        self.init(i, diff)

    def getSum(self, i):
        sum = 0
        i += 1
        while i > 0:
            sum += self.bit[i]
            i -= (i & -i)
        return sum

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.getSum(j) - self.getSum(i-1)


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.update(1, 10)
# numArray.sumRange(1, 2)
