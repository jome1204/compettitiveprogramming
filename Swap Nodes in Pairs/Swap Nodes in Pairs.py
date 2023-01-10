class Solution(object):
    def swapPairs(self, head):
        var = head
        while head and head.next:
            head.val, head.next.val = head.next.val, head.val
            head = head.next.next
        return var
