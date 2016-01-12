# Given a collection of integers that might contain duplicates, nums, return all possible subsets.

# Note:
# Elements in a subset must be in non-descending order.
# The solution set must not contain duplicate subsets.
# For example,
# If nums = [1,2,2], a solution is:

# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]


class Solution1(object):
    def subsetsWithDup(self, nums):
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
                if sol not in res:
                    res.append(sol)
        return res


class Solution2(object):
    def subsetsWithDup(self, nums):
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
                if i > start and nums[i] == nums[i-1]:
                    continue
                sol.append(nums[i])
                res.append(sol[:])
                findSubset(i+1, sol, res)
                sol.pop()

        findSubset(0, sol, res)
        return res

if __name__ == '__main__':
    sol1 = Solution1()
    print sol1.subsetsWithDup([2, 1, 2])
    sol2 = Solution2()
    print sol2.subsetsWithDup([2, 1, 2])
