class Solution(object):
    def merge(self, intervals):
        result = []
        for interval in sorted(intervals):
            if not result or result[-1][1] < interval[0]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1], interval[1])
        return result
