# You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        dummy = ListNode(-1)
        node = dummy
        while l1 or l2:
            val1 = val2 = 0
            if l1:
                val1 = l1.val
            if l2:
                val2 = l2.val
            val = carry + val1 + val2
            carry = val // 10
            val %= 10
            node.next = ListNode(val)
            node = node.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        # insert additonal carry if extra digit is added from addtion
        if carry:
            node.next = ListNode(carry)
        return dummy.next
