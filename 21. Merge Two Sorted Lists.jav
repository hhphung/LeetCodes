import java.util.List;

class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        if(list1 == null){
            return list2;
        }
        if(list2 == null){
            return list1;
        }
        if(list1 == null && list2 == null){
            return null;
        }
        ListNode head= new ListNode(0,null);
        ListNode currentOne = list1;
        ListNode currentTwo = list2;
        ListNode curr = head;

        while(currentOne != null && currentTwo != null){
            if(currentOne.val <= currentTwo.val){
                curr.next = currentOne;
                curr=curr.next;
                currentOne = currentOne.next;
            }else{
                curr.next = currentTwo;
                curr= curr.next;
                currentTwo = currentTwo.next;
            }
        }
        if(currentOne!= null){
            curr.next = currentOne;
        }
        if(currentTwo!= null){
            curr.next = currentTwo;
        }




        return head.next;
    }
    
}
