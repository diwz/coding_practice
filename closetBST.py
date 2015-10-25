class Solution(object):
    def closestBST(self, root, target):
        if not root:
            return None
        if root.val == target:
            return root

        if target < root.val:
            if not root.left:
                return root
            node = self.closestBST(root.left, target)
            return node if abs(root.val-target) > abs(node.val-target) else root
        else:
            if not root.right:
                return root
            node = self.closestBST(root.right, target)
            return node if abs(root.val-target) > abs(node.val-target) else root


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def insert(self, val):
        if self.val:
            if val < self.val:
                if not self.left:
                    self.left = TreeNode(val)
                else:
                    self.left.insert(val)
            elif val > self.val:
                if not self.right:
                    self.right = TreeNode(val)
                else:
                    self.right.insert(val)
        else:
            self.val = val

if __name__ == '__main__':
    root = TreeNode(8)
    root.insert(3)
    root.insert(10)
    root.insert(1)
    root.insert(6)
    root.insert(4)
    root.insert(7)
    root.insert(14)
    root.insert(13)

    sol = Solution()
    print(sol.closestBST(root, 3.4).val)
