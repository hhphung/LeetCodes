
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
       
        result = ListNode(0,head)
        pe = result
        while head and head.next:
            ne = head.next.next
            se = head.next
            se.next = head
            head.next = ne
            pe.next = se
            pe = head
            head =ne


        return result.next
