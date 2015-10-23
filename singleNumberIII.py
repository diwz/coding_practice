import functools


class Solution1(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor_res = functools.reduce(lambda x, y: x ^ y, nums)
        last_set_bit = xor_res & -xor_res

        ans = functools.reduce(lambda x, y: x ^ y, (x for x in nums if x & last_set_bit))
        return [ans, ans ^ xor_res]


class Solution2(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = nums[0]
        for i in range(1, len(nums)):
            res ^= nums[i]

        last_set = res & -res
        init = 0
        for num in nums:
            if num & last_set:
                init ^= num

        return [init, init ^ res]
