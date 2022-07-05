class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next :
            return head
        cur = head
        next = head.next
        temp =None
        head.next = None
        while next:
            temp = next.next
            next.next = cur
            cur = next
            next = temp
        return cur
