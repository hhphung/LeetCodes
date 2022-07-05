class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # [1,2,3,3,4,4,5]
        # [1,2,5]



        result = ListNode(0, next=head)
        cur = result
        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                cur.next = head.next
            else:
                cur = cur.next
            head = head.next

        return result.next
