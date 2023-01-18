class Solution(object):
    def xorQueries(self, arr, queries):
        n = len(arr)
        prefix = [0] * (n+1)
        result = []
        for idx, num in enumerate(arr):
            prefix[idx + 1] = prefix[idx] ^ num
        for left, right in queries:
            result.append(prefix[right + 1] ^ prefix[left])
        return result
