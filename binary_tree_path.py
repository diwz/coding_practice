# Given a binary tree, return all root-to-leaf paths.
# For example, given the following binary tree:

#    1
#  /   \
# 2     3
#  \
#   5
# All root-to-leaf paths are:
# ["1->2->5", "1->3"]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution1(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        if root is None:
            return res
        self.helper(root, str(root.val), res)
        return res

    def helper(self, root, path, res):
        if root is None:
            return res
        if root.left is None and root.right is None:
            res.append(path)
            return
        if root.left:
            self.helper(root.left, path + "->" + str(root.left.val), res)
        if root.right:
            self.helper(root.right, path + "->" + str(root.right.val), res)


class Solution2(object):
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if not root:
            return []
        return [str(root.val) + '->' + path
                for kid in (root.left, root.right) if kid
                for path in self.binaryTreePaths(kid)] or [str(root.val)]


class Solution3(object):
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if root is None:
            return []
        queue = [[root, str(root.val)]]
        res = []
        while queue:
            front, path = queue.pop(0)
            if front.left is None and front.right is None:
                res.append(path)
            if front.left:
                queue.append([front.left, path + "->" + str(front.left.val)])
            if front.right:
                queue.append([front.right, path + "->" + str(front.right.val)])
        return res
