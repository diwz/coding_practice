# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
# For example, this binary tree is symmetric:
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# But the following is not:
#     1
#    / \
#   2   2
#    \   \
#    3    3

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class recursiveSolution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.checker(root.left, root.right)

    def checker(self, left, right):
        if left is None and right is None:
            return True
        if left and right and left.val == right.val:
            return self.checker(left.right, right.left) and self.checker(right.right, left.left)
        else:
            return False


class iterativeSolution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        if not root.left and not root.right:
            return True
        if root.left is None or root.right is None:
            return False

        # pre-order traversal
        stack1, stack2 = [root.left], [root.right]
        while stack1 and stack2:
            node1 = stack1.pop()
            node2 = stack2.pop()
            if node1.val != node2.val:
                return False
            if (node1.left and not node2.right) or (not node1.left and node2.right):
                return False
            if (node1.right and not node2.left) or (not node1.right and node2.left):
                return False
            if node1.left and node2.right:
                stack1.append(node1.left)
                stack2.append(node2.right)
            if node1.right and node2.left:
                stack1.append(node1.right)
                stack2.append(node2.left)

        return True
