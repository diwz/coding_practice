# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            # empty tree
            return 0
        elif root.left is None and root.right is None:
            # a leaf
            return 1
        elif root.left is None:
            # node with only right child
            return self.minDepth(root.right) + 1
        elif root.right is None:
            # node with only left child
            return self.minDepth(root.left) + 1
        else:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
