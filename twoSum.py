class Solution(object):
    """docstring for Solution"""
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}
        for idx, val in enumerate(nums, start=1):
            if (target - val) not in map:
                map[val] = idx
            else:
                return (idx, map[target-val]) if idx < map[target-val] else (map[target-val], idx)
