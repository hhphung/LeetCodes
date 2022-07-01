class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head_A = l1; head_B = l2
        
        if head_A is None:
            return head_B
        elif head_B is None:
            return head_A
        else:
            if head_A.val <= head_B.val:
                head = head_A
                head_A = head_A.next
            else:
                head = head_B
                head_B = head_B.next

            head.next = self.mergeTwoLists(head_A, head_B)

            return head
