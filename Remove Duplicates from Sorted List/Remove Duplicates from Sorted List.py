class Solution(object):
    def deleteDuplicates(self, head):
        if head == None or head.next == None:
            return head

        list = head

        while(list.next!=None):
            if list.val == list.next.val:
                list.next = list.next.next
            else:
                list = list.next

        return head
