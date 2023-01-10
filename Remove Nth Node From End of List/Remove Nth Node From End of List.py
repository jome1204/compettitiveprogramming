class Solution(object):
    def removeNthFromEnd(self, head, n):
        low_speed = high_speed = head

        for i in range(n):
            high_speed = high_speed.next 

        if not high_speed:
            return head.next 

        while high_speed and high_speed.next:
            low_speed = low_speed.next 
            high_speed = high_speed.next 

        low_speed.next = low_speed.next.next 
        return head
