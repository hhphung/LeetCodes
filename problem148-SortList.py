# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        left = head
        right = self.getMid(head)
        t = right.next
        right.next = None
        right = t

        left = self.sortList(left)
        right = self.sortList(right)

        return self.merge(left,right)

    def merge(self, left, right):
        tail = result = ListNode()
        while left and right:
            if left.val <right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next
        if left:
            tail.next = left
        elif right:
            tail.next = right
        return result.next

    def getMid(self, head):
        left = head
        right = head.next
        while right and right.next:
            left = left.next
            right = right.next.next
        return left
