class Solution(object):
    def reverseList(self, head):
        prev=None
        while head:
            new_node = head.next
            head.next=prev
            prev = head           
            head = new_node
        return prev
