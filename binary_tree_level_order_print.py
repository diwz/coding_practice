# Level Order print binary tree
class Solution():
    def printLevelOrder(self, root):
        res = []
        if root is None:
            return res
        cur = []
        cur.append(root)
        next = []

        while cur:
            node = cur.pop(0)
            if node is None:
                print "#",
            else:
                print node.val,
                next.append(node.left)
                next.append(node.right)
            if not cur:
                cur = next
                next = []
                print "->",


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
    print sol.levelOrder(root)

