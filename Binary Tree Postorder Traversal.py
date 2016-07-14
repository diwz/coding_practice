# Given a binary tree, return the postorder traversal of its nodes' values.

# For example:
# Given binary tree {1,#,2,3},
#    1
#     \
#      2
#     /
#    3
# return [3,2,1].

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        lastNodeVisted = None
        node = root
        res = []
        while len(stack) != 0 or node is not None:
            if node is not None:
                stack.append(node)
                node = node.left
            else:
                peekNode = stack[-1]
                if peekNode.right is not None and lastNodeVisted is not peekNode.right:
                    node = peekNode.right
                else:
                    res.append(peekNode.val)
                    lastNodeVisted = stack.pop()
        return res
