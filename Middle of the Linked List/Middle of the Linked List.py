class Solution(object):
    def middleNode(self, head):
        low = head
        high = head

        while high and high.next:
            low = low.next
            high = high.next.next

        return low
