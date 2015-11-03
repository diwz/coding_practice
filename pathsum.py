# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

# For example:
# Given the below binary tree and sum = 22,
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \      \
#         7    2      1
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class recursiveSolution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
        elif root.val == sum and root.left is None and root.right is None:
            return True
        else:
            return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)


class iterativeSolution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        queue = []
        valQ = []

        if root is None:
            return False

        queue.append(root)
        valQ.append(root.val)

        while queue:
            node = queue.pop(0)
            curSum = valQ.pop(0)

            if node.left is None and node.right is None and curSum == sum:
                return True
            if node.left:
                queue.append(node.left)
                valQ.append(curSum + node.left.val)
            if node.right:
                queue.append(node.right)
                valQ.append(curSum + node.right.val)

        return False
