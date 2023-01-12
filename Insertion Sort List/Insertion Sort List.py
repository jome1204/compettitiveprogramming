class Solution(object):
    def insertionSortList(self, head):
        nums=[]
        while(head):
            nums.append(head.val)
            head=head.next
        nums.sort()
        head=None
       
        for val in nums:
            if not head:
                head=ListNode(val, None)
                prv=head
            else:
                node=ListNode(val, None)
                prv.next=node
                prv=node
        return head
