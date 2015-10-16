# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        nums = []
        node = head

        while node:
            nums.append(node.val)
            node = node.next

        return self.helper(nums, 0, len(nums)-1)

    def helper(self, nums, start, end):
        if start > end:
            return None
        mid = (start + end)//2
        root = TreeNode(nums[mid])
        root.left = self.helper(nums, start, mid-1)
        root.right = self.helper(nums, mid+1, end)
        return root
