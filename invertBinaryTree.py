# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class recursiveSolution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            self.invert(root)
        return root

    def invert(self, node):

        node.left, node.right = node.right, node.left
        if node.left:
            self.invert(node.left)
        if node.right:
            self.invert(node.right)


class iterativeSolution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        queue = []
        if root:
            queue.append(root)

        while queue:
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

            node.left, node.right = node.right, node.left

        return root
