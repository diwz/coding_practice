# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution1(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        self.preOrder(root, 0, res)
        return res

    def preOrder(self, root, level, res):
        if root:
            if len(res) < level + 1:
                res.append([])
            res[level].append(root.val)
            self.preOrder(root.left, level + 1, res)
            self.preOrder(root.right, level + 1, res)


class Solution2(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if root is None:
            return res
        cur = []
        cur.append(root)
        next = []

        vals = []
        while cur:
            node = cur.pop(0)
            vals.append(node.val)
            if node.left:
                next.append(node.left)
            if node.right:
                next.append(node.right)
            if not cur:
                cur = next
                next = []
                res.append(vals)
                vals = []
        return res

"""
Keep track of the rightmost node at each level, reduce the number of queue used
"""


class Solution3(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        queue = []
        if root is None:
            return res
        queue.append(root)

        # right most as the right most node of each level
        rightmost = root
        # prev as the right most node of prev sub tree at that level
        prev = None
        list = []
        while queue:
            node = queue.pop(0)
            list.append(node.val)

            if node is rightmost:
                res.append(list)
                list = []
                if node.right:
                    rightmost = node.right
                elif node.left:
                    rightmost = node.left
                else:
                    rightmost = prev
            if node.left:
                queue.append(node.left)
                prev = node.left
            if node.right:
                queue.append(node.right)
                prev = node.right
        return res
