class Solution(object):
    def deleteDuplicates(self, head):
        if not head or not head.next :
            return head
        front = head
        while front.next and front.val == front.next.val:
            front = front.next
        if front != head:
            head = front.next
            return self.deleteDuplicates(head)
        head.next = self.deleteDuplicates(head.next)
        return head
