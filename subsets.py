# Given a set of distinct integers, nums, return all possible subsets.

# Note:
# Elements in a subset must be in non-descending order.
# The solution set must not contain duplicate subsets.
# For example,
# If nums = [1,2,3], a solution is:

# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]


class Solution1(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None:
            return None
        nums.sort()
        res = [[]]
        size = len(nums)
        for i in range(size):
            n = len(res)
            for j in range(n):
                sol = res[j][:]
                sol.append(nums[i])
                res.append(sol)
        return res

class Solution2(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None:
            return None
        nums.sort()
        size = len(nums)
        res = []

        for i in range(2**size):
            sol = [nums[x] for x in range(size) if format(i, str(size)+'b')[x:x + 1] == '1']
            res.append(sol)
        return res


class Solution3(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None:
            return None
        size = len(nums)
        nums.sort()
        sol = []
        res = [sol]

        def findSubset(start, sol, res):
            for i in range(start, size):
                sol.append(nums[i])
                res.append(sol[:])
                findSubset(i+1, sol, res)
                sol.pop()

        findSubset(0, sol, res)
        return res

if __name__ == '__main__':
    sol1 = Solution2()
    print sol1.subsets([2, 1, 3])
    sol2 = Solution2()
    print sol2.subsets([2, 1, 3])
    sol3 = Solution3()
    print sol3.subsets([2, 1, 3])
