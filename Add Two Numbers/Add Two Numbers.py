class Solution(object):
    def addTwoNumbers(self, l1, l2):
        runned = Lists = ListNode(None)
        sum = 0
        while l1 or l2 :
            sum_val = sum
            if l1 != None:
                sum_val += l1.val
                l1 = l1.next
            if l2 != None:
                sum_val += l2.val
                l2 = l2.next
            sum = sum_val // 10
            Lists.next = ListNode(sum_val % 10)
            Lists = Lists.next

        if sum == 1:
            Lists.next = ListNode(sum)

        return runned.next
