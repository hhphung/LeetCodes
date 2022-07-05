class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """

        if head == None or head.next == None or left == right:
            return head
        dummy = ListNode(0, next = head)

        start = head
        end = head
        second = None
        first = dummy

        while right > 1:
            if left > 1:
                start = start.next
                first= first.next
            if right >1:
                end = end.next
            right -= 1
            left -= 1
        second = end.next
        end.next = None

        temp = None
        nxt = start.next
        last = start
        start.next = None
        while nxt:
            temp = nxt.next
            nxt.next = start
            start = nxt
            nxt = temp
        first.next = start
        last.next = second
        return dummy.next
