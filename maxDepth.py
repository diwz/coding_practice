# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution1(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


class Solution2(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        queue = deque()
        levels = deque()

        queue.appendleft(root)
        levels.appendleft(1)

        while queue:
            node = queue.pop()
            level = levels.pop()
            if node.left:
                queue.appendleft(node.left)
                levels.appendleft(level + 1)
            if node.right:
                queue.appendleft(node.right)
                levels.appendleft(level + 1)
            if not queue:
                return level
        return 0
