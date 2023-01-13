class Solution {
    public void reorderList(ListNode head) {
        if(head == null || head.next == null)
            return;
        //split the list
        ListNode fast = head, slow = head;
        while(fast.next != null && fast.next.next != null){
            fast = fast.next.next;
            slow = slow.next;
        }
        ListNode secondHead = slow.next;
        slow.next = null;
        //reverse the second list
        ListNode prev = null;
        ListNode current = secondHead;
        while(current != null){
            ListNode next = current.next;
            current.next = prev;
            prev = current;
            current = next;
        }
        secondHead = prev;
        //merge the list
        ListNode first = head;
        while(first != null && secondHead != null){
            ListNode fNext = first.next;
            ListNode sNext = secondHead.next;
            
            first.next = secondHead;
            first = secondHead.next = fNext;
            secondHead = sNext;
        }
    }
}
