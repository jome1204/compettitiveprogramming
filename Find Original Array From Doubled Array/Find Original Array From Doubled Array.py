class Solution(object):
    def findOriginalArray(self, changed):
        res = []
        coll = collections.deque()

        for num in sorted(changed):
            if coll and num == coll[0]:
                coll.popleft()
            else:
                coll.append(num * 2)
                res.append(num)

        return [] if coll else res
