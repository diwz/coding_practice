# Given a singly linked list, determine if it is a palindrome.

# Follow up:
# Could you do it in O(n) time and O(1) space?


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return True

        fast = slow = head
        # find the mid point
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half
        p, curr = slow.next, None
        while p:
            next = p.next
            p.next = curr
            curr, p = p, next

        # check palindrome
        p1, p2 = curr, head
        while p1 and p1.val == p2.val:
            p1, p2 = p1.next, p2.next

        return p1 is None
