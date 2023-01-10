class Solution(object):
    def reverseKGroup(self, head, k):
        sum = 0
        pointed = head

        while(pointed):
            sum += 1
            pointed = pointed.next


        prev = None
        pointed = head
        count = 0
        while(pointed and count < k ):
            next = pointed.next
            pointed.next = prev
            prev = pointed

            pointed = next
            count += 1


        sum -= k
        if sum >= k:
            head.next = self.reverseKGroup(next,k)

        else:
            head.next = next

        return prev
