class Solution(object):
    def kClosest(self, points, k):
        return heapq.nsmallest(k, points, lambda (var1, var2): var1 * var1 + var2 * var2)
