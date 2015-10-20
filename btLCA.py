# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class recursiveSolution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or root is p or root is q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left is None:
            return right
        elif right is None:
            return left
        else:
            return root


class iterativeSolution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        pathP, pathQ = self.getPath(root, p), self.getPath(root, q)
        minLen = min(len(pathP), len(pathQ))
        ans = None
        for i in range(minLen):
            if pathP[i] is pathQ[i]:
                ans = pathP[i]
        return ans

    def getPath(self, node, target):
        # use post-order, because we want to have to root elem being placed last
        stack = []
        lastVisit = None
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                peek = stack[-1]
                if peek.right and lastVisit != peek.right:
                    node = peek.right
                else:
                    if peek is target:
                        return stack
                    lastVisit = stack.pop()
                    node = None
        return stack
