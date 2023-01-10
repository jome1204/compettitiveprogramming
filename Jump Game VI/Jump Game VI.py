class Solution(object):
    def maxResult(self, nums, k):
        length = len(nums)
        var = deque([length-1])
        for i in range(length-2, -1, -1):
            if var[0] - i > k: var.popleft()
            nums[i] += nums[var[0]]
            while len(var) and nums[var[-1]] <= nums[i]: var.pop()
            var.append(i)
        return nums[0]
