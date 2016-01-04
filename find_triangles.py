# Given a list of positive integers, find the number of triangles that can be formed by these integers


class Solution(object):
    def findTriangles(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        size = len(nums)
        nums.sort()

        count  = 0

        for i in range(size-2):
            k = i + 2

            for j in range(i+1, size):

                while k < size and nums[i] + nums[j] > nums[k]:
                    k += 1

                count += k - j - 1

        return count


if __name__ == '__main__':
    sol = Solution()

    print sol.findTriangles([4,3,1])
    print sol.findTriangles([2,2,4,3])
