class Solution(object):
    def mergeKLists(self, lists):
        heap = []
        root = result = ListNode(None)

        for l in lists:
            while l:
                heappush(heap, l.val)
                l = l.next

        while heap:
            result.next = ListNode(heappop(heap))
            result = result.next
        return root.next
