# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        slow, fast = head, head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        l1 = head
        l2 = slow.next
        slow.next = None
        l1 = self.sortList(l1)
        l2 = self.sortList(l2)

        return self.mergeLists(l1, l2)

    def mergeLists(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        dummy = ListNode(-1)
        tmp = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tmp.next = l1
                tmp = tmp.next
                l1 = l1.next
            else:
                tmp.next = l2
                tmp = tmp.next
                l2 = l2.next
        if not l1:
            tmp.next = l2
        else:
            tmp.next = l1
        return dummy.next
