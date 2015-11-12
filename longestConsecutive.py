# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

# For example,
# Given [100, 4, 200, 1, 3, 2],
# The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

# Your algorithm should run in O(n) complexity.


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: inta
        """
        if not nums:
            return 0

        nums_set = set(nums)
        max_len = 1

        for num in nums:
            if len(nums_set) == 0:
                break

            cur_len = 0
            cur_num = num

            # Search consecutive number in increasing direction
            while cur_num in nums_set:
                # remeber to remove the visited number
                nums_set.remove(cur_num)
                cur_len += 1
                cur_num += 1

            cur_num = num - 1
            # Serach consecutive number in decreasing direction
            while cur_num in nums_set:
                nums_set.remove(cur_num)
                cur_len += 1
                cur_num -= 1

            max_len = max(max_len, cur_len)

        return max_len
