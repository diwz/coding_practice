# There are two sorted arrays nums1 and nums2 of size m and n respectively.

# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

# Example 1:
# nums1 = [1, 3]
# nums2 = [2]

# The median is 2.0
# Example 2:
# nums1 = [1, 2]
# nums2 = [3, 4]

# The median is (2 + 3)/2 = 2.5

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)

        if (m+n) % 2 == 1:
            return self.findKth(nums1, nums2, (m+n)/2+1)
        else:
            return (self.findKth(nums1, nums2, (m+n)/2) + self.findKth(nums1, nums2, (m+n)/2+1)) * 0.5

    def findKth(self, A, B, k):
        if len(A) > len(B):
            return self.findKth(B, A, k)
        if len(A) == 0:
            return B[k-1]
        if k == 1:
            return min(A[0], B[0])

        pa = min(k/2, len(A))
        pb = k - pa
        if A[pa-1] <= B[pb-1]:
            return self.findKth(A[pa:], B, pb)
        else:
            return self.findKth(A, B[pb:], pa)
