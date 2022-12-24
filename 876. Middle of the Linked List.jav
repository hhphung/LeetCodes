class Solution {
    public ListNode middleNode(ListNode head) {
        int length = 0;
        ListNode curr = head;
        while (curr != null){
            length+=1;
            curr = curr.next;
        }
        length = length /2;
        curr = head;
        while(length >0){
            curr = curr.next;
            length-=1;
        }

        return curr;
    }
   
}
