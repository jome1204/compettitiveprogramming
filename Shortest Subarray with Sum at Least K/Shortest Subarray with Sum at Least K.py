class Solution(object):
    def shortestSubarray(self, nums, k):
        dp = [0] * (len(nums) + 1)

        for i in range(1, len(dp)):
            dp[i] = dp[i - 1] + nums[i - 1]

        res = len(nums) + 1

        coll = collections.deque()

        for i in range(len(dp)):
            while coll and dp[i] - dp[coll[0]] >= k:
                res = min(res, i - coll.popleft())
            while coll and dp[i] < dp[coll[-1]]:
                coll.pop() 
            coll.append(i)

        return res if res != len(nums)+1 else -1
