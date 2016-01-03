# Write a program to find the node at which the intersection of two singly linked lists begins.
# For example, the following two linked lists:
# A:          a1 → a2
#                    ↘
#                      c1 → c2 → c3
#                    ↗
# B:     b1 → b2 → b3
# begin to intersect at node c1.

# Notes:
# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function returns.
# You may assume there are no cycles anywhere in the entire linked structure.
# Your code should preferably run in O(n) time and use only O(1) memory.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution1(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None

        lenA = self.getLength(headA)
        lenB = self.getLength(headB)

        diff = abs(lenA-lenB)

        if lenA > lenB:
            while diff > 0:
                headA = headA.next
                diff = diff - 1
        else:
            while diff > 0:
                headB = headB.next
                diff = diff -1

        while headA:
            if headA is headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None


    def getLength(self, node):
        count = 0;
        while node:
            node = node.next
            count = count + 1

        return count

class Solution2(object):
    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None:
            return None

        nodeA = headA
        nodeB = headB
        endA = None
        endB = None
        while True:
            # keep a copy of list end respectively
            if nodeA is None:
                nodeA = headB

            if nodeB is None:
                nodeB = headA

            if nodeA.next is None:
                endA = nodeA
            if nodeB.next is None:
                endB = nodeB

            if nodeA is nodeB:
                return nodeA

            # If two linked lists have different ends, they do not intersect
            if endA is not None and endB is not None and endA is not endB:
                return None

            nodeA = nodeA.next
            nodeB = nodeB.next
