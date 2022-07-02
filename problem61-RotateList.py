class Solution(object):
    def rotateRight(self, head, k):

        if not head:
            return head

        leng = 1
        end = head
        while end.next:
            end = end.next
            leng+=1
        k = k%leng
        if k == 0:
            return head
        at_k = head
        for i in range(leng-k-1):
            at_k = at_k.next
        new = at_k.next
        at_k.next = None
        end.next = head
        return new
