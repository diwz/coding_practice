# Given a binary tree, find the mirror of itself
# For example, t
#     1
#    / \
#   2   4
#  / \ / \
# 3  5 6  7
# Returns
#     1
#    / \
#   4   2
#  / \ / \
# 7  6 5  3


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def mirrorTreeRec(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return root
        else:
            root.left, root.right = root.right, root.left
            self.mirrorTreeRec(root.left)
            self.mirrorTreeRec(root.right)

    def mirrorTreeIte(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return root

        stack = []
        stack.append(root)

        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)


    def printTree(self, root):
        if root is None:
            return
        else:
            print " ", root.val
            self.printTree(root.left)
            self.printTree(root.right)

if __name__ == '__main__':
    root = TreeNode(8)
    root.left = TreeNode(9)
    root.right = TreeNode(6)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(7)

    node = TreeNode(8)
    sol = Solution()
    print("Before")
    sol.printTree(root)
    sol.mirrorTreeRec(root, node)
    print("After")
    sol.printTree(root)
