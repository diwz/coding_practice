class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """

        """
        Sliding window + Dict
        """
        if k < 1 or t < 0:
            return False
        window = collections.OrderedDict()
        for x in range(len(nums)):
            key = nums[x] / max(1, t)
            for m in (key, key-1, key+1):
                if m in window and abs(nums[x]-window[m]) <= t:
                    return True
            window[key] = nums[x]
            if x >= k:
                window.popitem(False)
        return False
