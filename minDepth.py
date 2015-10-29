# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution1(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            # empty tree
            return 0
        elif root.left is None:
            # node with only right child
            return self.minDepth(root.right) + 1
        elif root.right is None:
            # node with only left child
            return self.minDepth(root.left) + 1
        else:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1


class Solution2(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        queue = deque()
        queue.appendleft(root)
        levels = deque()
        levels.appendleft(1)

        while queue:
            node = queue.pop()
            level = levels.pop()
            if node.left:
                queue.appendleft(node.left)
                levels.appendleft(level+1)
            if node.right:
                queue.appendleft(node.right)
                levels.appendleft(level+1)
            if node.left is None and node.right is None:
                return level
        return 0
