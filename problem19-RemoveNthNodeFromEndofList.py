class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """


        node = ListNode(0, head)
        left = node
        right = head
        while n > 0 and right:
            right = right.next
            n -=1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next

        return node.next
