# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        even = head
        odd = ListNode(head.next.val,None)
        first = ListNode(0, even)
        second = ListNode(0, odd)

        head = head.next.next

        while head:
            if head.next:

                even.next = head
                even = even.next

                odd.next = ListNode(head.next.val,None)
                odd = odd.next
                head = head.next.next
            else:
                even.next = head
                even = even.next
                head = head.next
        even.next = second.next

        return first.next
