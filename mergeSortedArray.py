class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

        i, j, idx = m-1, n-1, -1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[idx] = nums1[i]
                i -= 1
                idx -= 1
            else:
                nums1[idx] = nums2[j]
                j -= 1
                idx -= 1

        while j >= 0:
            nums1[idx] = nums2[j]
            j -= 1
            idx -= 1

        return nums1
